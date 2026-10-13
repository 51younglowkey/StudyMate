from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT / "90_scripts_tools" / "project_workspace"
sys.path.insert(0, str(WORKSPACE))


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


dashboard = load("guided_dashboard", WORKSPACE / "render_dashboard.py")
sessions = load("guided_sessions", WORKSPACE / "session_handoff.py")
installer = load("guided_installer", ROOT / "90_scripts_tools" / "threading" / "install_skill.py")
doctor = load("guided_doctor", ROOT / "90_scripts_tools" / "threading" / "doctor.py")


class GuidedStartTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="threading-guided-test-")
        self.root = Path(self.temp.name)
        self.project = self.root / "project"
        self.project.mkdir()
        (self.project / "CURRENT.md").write_text("# Current\n\n## Next move\n\n[DECISION PENDING]\n\nTemplate rule must not become a task.\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def test_placeholder_does_not_promote_instruction_to_next_move(self):
        text = (self.project / "CURRENT.md").read_text(encoding="utf-8")
        self.assertEqual(dashboard.first_section_value(text, "Next move", "[DECISION PENDING]"), "[DECISION PENDING]")
        self.assertEqual(dashboard.first_section_value(text.replace("\n", "\r\n"), "Next move", "missing"), "missing")

    def test_first_section_is_bounded_by_next_heading(self):
        text = "## Next move\n\n## Rules\n\nThis is not a next move.\n"
        self.assertEqual(dashboard.first_section_value(text, "Next move", "missing"), "missing")
        linked_task = "## Next move\n\n[Review the prototype](outputs/prototype.md)\n"
        self.assertEqual(dashboard.first_section_value(linked_task, "Next move", "missing"), "[Review the prototype](outputs/prototype.md)")

    def test_empty_and_populated_decision_tables_count_only_records(self):
        path = self.root / "decisions.md"
        path.write_text("| Date | Decision | Status |\n| :--- | ---: | :---: |\n", encoding="utf-8")
        self.assertEqual(dashboard.table_data_rows(path), 0)
        with path.open("a", encoding="utf-8") as handle:
            handle.write("| 2026-10-13 | Compare two concepts | candidate |\n\nStatuses: candidate.\n")
        self.assertEqual(dashboard.table_data_rows(path), 1)

    def test_placeholder_source_is_not_a_registered_record(self):
        path = self.root / "sources.md"
        path.write_text("| ID | Pointer |\n|---|---|\n| S-001 | [SOURCE TO VERIFY] |\n| S-002 | brief.pdf |\n", encoding="utf-8")
        self.assertEqual(dashboard.table_data_rows(path), 1)

    def test_independent_sessions_preserve_current_and_reject_repeated_finish(self):
        before = (self.project / "CURRENT.md").read_bytes()
        first = sessions.start(self.project, "Compare concepts", "conversation-a")
        second = sessions.start(self.project, "Review course requirements", "conversation-b")
        self.assertNotEqual(first, second)
        path, changed = sessions.finish(self.project, first.name, ["Saved candidate comparison"],
                                        "Ask owner to select a test", ["S-001 / named section only"], ["Direction not confirmed"])
        self.assertFalse(changed)
        saved = path.read_bytes()
        with self.assertRaises(FileExistsError):
            sessions.finish(self.project, first.name, ["Different work"], "Different next move", [], [])
        self.assertEqual(path.read_bytes(), saved)
        self.assertEqual((self.project / "CURRENT.md").read_bytes(), before)
        state = json.loads((second / "start.json").read_text(encoding="utf-8"))
        self.assertEqual(state["workspace"], str(self.project.resolve()))

    def test_changed_snapshot_creates_reviewable_handoff_without_overwrite(self):
        folder = sessions.start(self.project, "Review criteria", "conversation-c")
        current = self.project / "CURRENT.md"
        current.write_text("# Owner-confirmed new state\n", encoding="utf-8")
        before = current.read_bytes()
        path, changed = sessions.finish(self.project, folder.name, ["Drafted a criteria map"], "Reconcile map", [], [])
        self.assertTrue(changed)
        self.assertIn("Status: needs-reconciliation", path.read_text(encoding="utf-8"))
        self.assertEqual(current.read_bytes(), before)

    def test_dashboard_displays_only_explicitly_selected_session(self):
        sessions.start(self.project, "Compare concepts", "selected-session")
        sessions.finish(self.project, "selected-session", ["Saved comparison"], "Review comparison", [], [])
        sessions.start(self.project, "Unrelated work", "other-session")
        sessions.finish(self.project, "other-session", ["Unrelated result"], "Unrelated next move", [], [])
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            dashboard.render_project(self.project, session_id="selected-session")
        self.assertIn("Saved comparison", capture.getvalue())
        self.assertIn("candidate", capture.getvalue())
        self.assertNotIn("Unrelated result", capture.getvalue())

    def test_session_binding_cannot_cross_projects_or_escape(self):
        folder = sessions.start(self.project, "Frame question", "conversation-d")
        record = folder / "start.json"
        state = json.loads(record.read_text(encoding="utf-8"))
        state["workspace"] = str(self.root)
        record.write_text(json.dumps(state), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "binding"):
            sessions.finish(self.project, folder.name, ["Draft"], "Review", [], [])
        for value in ("../other", "", "a/b", "a\\b"):
            with self.assertRaises(ValueError):
                sessions.start(self.project, "Task", value)

    def test_automatic_copy_fallback_is_idempotent_and_preserves_local_copy(self):
        home = self.root / "test-home"
        args = argparse.Namespace(home=home, platform="all", mode="auto", update=False)
        with patch.object(installer, "parse_args", return_value=args), \
             patch.object(Path, "symlink_to", side_effect=OSError("symlink privilege unavailable")), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(installer.main(), 0)
            skill = home / ".agents" / "skills" / "threading"
            pointer = skill / "references" / "core-path.txt"
            self.assertEqual(Path(pointer.read_text(encoding="utf-8").strip()).resolve(), ROOT)
            marker = skill / "local-marker.txt"
            marker.write_text("preserve me", encoding="utf-8")
            self.assertEqual(installer.main(), 0)
            self.assertEqual(marker.read_text(encoding="utf-8"), "preserve me")
        result = subprocess.run([sys.executable, str(ROOT / "90_scripts_tools/threading/doctor.py"), "--home", str(home)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_course_and_web_pointers_do_not_import_materials(self):
        source = self.root / "private-course.txt"
        source.write_text("synthetic private teaching original", encoding="utf-8")
        before = source.read_bytes()
        result = subprocess.run([
            sys.executable, str(WORKSPACE / "adopt_project.py"), "--slug", "course-project",
            "--title", "Synthetic Course Project", "--pack", "none", "--course-source", str(source),
            "--web-source", "https://course.invalid/courses/example/assignment",
            "--output-root", str(self.root / "projects"), "--allow-external-root",
        ], capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        project = self.root / "projects/course-project"
        registry = (project / "sources/source_registry.md").read_text(encoding="utf-8")
        self.assertIn("course-material", registry)
        self.assertIn("web-page", registry)
        self.assertIn("not requested", registry)
        state = json.loads((project / "threading.json").read_text(encoding="utf-8"))
        self.assertFalse(state["gsa_pack"]["enabled"])
        self.assertEqual(source.read_bytes(), before)
        self.assertFalse(any(path.name == source.name for path in project.rglob("*")))

    def test_zip_privacy_check_discloses_unverified_git_state(self):
        with patch.object(doctor.subprocess, "run", side_effect=FileNotFoundError("Git unavailable")):
            ok, detail = doctor.privacy_check()
        self.assertTrue(ok)
        self.assertIn("declaration only", detail)
        self.assertIn("verification unavailable", detail)

    def test_session_cli_round_trip_and_repository_doctor(self):
        env = dict(os.environ, PYTHONUTF8="1")
        base = [sys.executable, str(WORKSPACE / "session_handoff.py")]
        common = ["--project", str(self.project), "--allow-external-project", "--session-id", "cli-session"]
        started = subprocess.run(base + ["start"] + common + ["--goal", "Review draft"], capture_output=True, text=True, encoding="utf-8", env=env)
        self.assertEqual(started.returncode, 0, started.stderr)
        finished = subprocess.run(base + ["finish"] + common + ["--completed", "Recorded limitations", "--next-move", "Review limitations"], capture_output=True, text=True, encoding="utf-8", env=env)
        self.assertEqual(finished.returncode, 0, finished.stderr)
        self.assertTrue((self.project / "sessions/cli-session/handoff.md").is_file())
        checked = subprocess.run([sys.executable, str(ROOT / "90_scripts_tools/threading/doctor.py"), "--platform", "repo", "--home", str(self.root / "empty-home")], capture_output=True, text=True)
        self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)


if __name__ == "__main__":
    unittest.main()
