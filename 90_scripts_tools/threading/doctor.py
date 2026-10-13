#!/usr/bin/env python3
"""Report StudyMate core, skill, project and linked-pack health."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REQUIRED_WORKSPACE_PATHS = (
    "AGENTS.md",
    "CURRENT.md",
    "project.md",
    "packs.md",
    "threading.json",
    "sources/source_registry.md",
    "sources/chats/chat_inventory.md",
    "sources/chats/candidate_records.md",
    "sources/figma/evolution_map.md",
    "sources/local-files/README.md",
    "evidence/evidence_log.md",
    "decisions/decision_log.md",
    "iterations/iteration_log.md",
    "outputs/README.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check StudyMate installation and project health.")
    parser.add_argument("--project", type=Path)
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--platform", choices=("all", "codex", "claude", "repo"), default="all",
                        help="repo checks core only; other values also verify selected Skill registrations")
    return parser.parse_args()


def check(label: str, ok: bool, detail: str) -> bool:
    print(f"{'PASS' if ok else 'FAIL'}  {label}: {detail}")
    return ok


def privacy_check() -> tuple[bool, str]:
    try:
        repository = subprocess.run(["git", "rev-parse", "--is-inside-work-tree"],
                                    cwd=ROOT, capture_output=True, text=True, check=False)
        if repository.returncode == 0:
            result = subprocess.run(["git", "check-ignore", "-q", "projects/local/example"],
                                    cwd=ROOT, capture_output=True, check=False)
            return result.returncode == 0, "projects/local ignore verified by Git"
    except FileNotFoundError:
        pass
    ignore = ROOT / ".gitignore"
    declared = ignore.is_file() and "/projects/local/" in ignore.read_text(encoding="utf-8").splitlines()
    return declared, "projects/local ignore declaration only; Git verification unavailable in this ZIP/non-Git environment"


def main() -> int:
    args = parse_args()
    results: list[bool] = []
    version_path = ROOT / "VERSION"
    results.append(check("core", version_path.is_file(), str(ROOT)))
    version = version_path.read_text(encoding="utf-8").strip() if version_path.exists() else "missing"
    results.append(check("version", version != "missing", version))
    privacy_ok, privacy_detail = privacy_check()
    results.append(check("local privacy", privacy_ok, privacy_detail))

    home = args.home.expanduser().resolve()
    skill_locations = (
        ("Codex skill", home / ".agents" / "skills" / "threading"),
        ("Claude Code skill", home / ".claude" / "skills" / "threading"),
    )
    for label, skill in skill_locations:
        if args.platform == "repo" or (args.platform == "codex" and label != "Codex skill") or (args.platform == "claude" and label != "Claude Code skill"):
            continue
        installed = (skill / "SKILL.md").is_file()
        if installed and skill.is_symlink():
            detail = f"symlink -> {skill.resolve()}"
            installed = skill.resolve() == (ROOT / "skills" / "threading").resolve()
        elif installed:
            pointer = skill / "references" / "core-path.txt"
            installed = pointer.is_file() and Path(pointer.read_text(encoding="utf-8").strip()).resolve() == ROOT
            detail = "copied installation; Core updates require --mode copy --update"
        else:
            detail = "missing or invalid; run install_skill.py, or use --platform repo for a repository-only host"
        results.append(check(label, installed, detail))

    if args.project:
        project = args.project.expanduser().resolve()
        results.append(check("project", project.is_dir(), str(project)))
        current = project / "CURRENT.md"
        state_path = project / "threading.json"
        results.append(check("Current State", current.is_file(), str(current)))
        results.append(check("project state", state_path.is_file(), str(state_path)))
        missing = [relative for relative in REQUIRED_WORKSPACE_PATHS if not (project / relative).is_file()]
        results.append(
            check(
                "workspace structure",
                not missing,
                "complete" if not missing else "missing: " + ", ".join(missing),
            )
        )
        if state_path.is_file():
            try:
                state = json.loads(state_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as error:
                results.append(check("project JSON", False, str(error)))
            else:
                results.append(
                    check("schema", state.get("schema_version") == 2, str(state.get("schema_version")))
                )
                pack = state.get("gsa_pack", {})
                if pack.get("enabled"):
                    pack_version = (ROOT / "packs" / "gsa" / "VERSION").read_text(encoding="utf-8").strip()
                    results.append(
                        check(
                            "GSA Pack",
                            pack.get("mode") == "linked-read-only" and pack.get("version") == pack_version,
                            f"project={pack.get('version')} core={pack_version}",
                        )
                    )

    passed = sum(results)
    print(f"Summary: {passed}/{len(results)} checks passed")
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
