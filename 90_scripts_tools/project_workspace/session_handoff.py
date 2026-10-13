#!/usr/bin/env python3
"""Bind a conversation to one project and save an independent candidate handoff.

Never modifies CURRENT.md or shared logs. A changed Current State is reported,
not overwritten; different conversations use different session directories.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path

from common import resolve_project


def current_hash(project: Path) -> str:
    return hashlib.sha256((project / "CURRENT.md").read_bytes()).hexdigest()


def session_folder(project: Path, session_id: str) -> Path:
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9-]{0,79}", session_id):
        raise ValueError("Invalid session ID. Use letters, numbers and hyphens.")
    folder = project / "sessions" / session_id
    if not folder.resolve().is_relative_to(project.resolve()):
        raise ValueError("Session path must remain inside the selected project.")
    return folder


def start(project: Path, goal: str, session_id: str | None = None) -> Path:
    if not goal.strip():
        raise ValueError("A session needs a non-empty working goal.")
    state = {
        "workspace": str(project.resolve()),
        "goal": goal.strip(),
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "base_current_sha256": current_hash(project),
    }
    identifier = uuid.uuid4().hex if session_id is None else session_id
    folder = session_folder(project, identifier)
    folder.mkdir(parents=True, exist_ok=False)
    state["session_id"] = identifier
    (folder / "start.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return folder


def finish(project: Path, session_id: str, completed: list[str], next_move: str,
           sources: list[str], pending: list[str]) -> tuple[Path, bool]:
    if not completed or not all(item.strip() for item in completed) or not next_move.strip():
        raise ValueError("Provide completed work and a non-empty proposed next move.")
    folder = session_folder(project, session_id)
    record = folder / "start.json"
    if not record.resolve().is_relative_to(folder.resolve()):
        raise ValueError("Session binding record must remain inside its session directory.")
    state = json.loads(record.read_text(encoding="utf-8"))
    if state.get("workspace") != str(project.resolve()) or state.get("session_id") != session_id:
        raise ValueError("Session binding does not match the selected workspace.")
    changed = state["base_current_sha256"] != current_hash(project)
    status = "needs-reconciliation" if changed else "candidate"
    def bullets(values: list[str]) -> str:
        return "\n".join(f"- {value.strip()}" for value in values) if values else "- None recorded."
    content = (
        f"# Session Handoff\n\nSession: {session_id}\nStatus: {status}\n"
        f"Workspace: {state['workspace']}\nCompleted at UTC: {datetime.now(timezone.utc).isoformat()}\n"
        f"Base Current State SHA-256: {state['base_current_sha256']}\n\n"
        f"## Working goal\n\n{state['goal']}\n\n"
        f"## Completed work\n\n{bullets(completed)}\n\n"
        f"## Inspected sources and scope\n\n{bullets(sources)}\n\n"
        f"## Pending confirmations and limitations\n\n{bullets(pending)}\n\n"
        f"## Proposed next move\n\n{next_move.strip()}\n\n"
        "This handoff records session progress. It does not promote claims or decisions into Current State.\n"
    )
    path = folder / "handoff.md"
    # Exclusive creation preserves an earlier handoff even on repeated completion.
    with path.open("x", encoding="utf-8") as handle:
        handle.write(content)
    return path, changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("start", "finish"))
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--allow-external-project", action="store_true")
    parser.add_argument("--session-id")
    parser.add_argument("--goal", default="")
    parser.add_argument("--completed", action="append", default=[])
    parser.add_argument("--source", action="append", default=[], help="already-inspected source ID, locator and scope; does not inspect a source")
    parser.add_argument("--pending", action="append", default=[])
    parser.add_argument("--next-move", default="")
    args = parser.parse_args()
    try:
        project = resolve_project(args.project, args.allow_external_project)
        if args.action == "start":
            folder = start(project, args.goal, args.session_id)
            print(f"Session ID: {folder.name}\nBound workspace: {project}\nRecord: {folder / 'start.json'}")
        else:
            if not args.session_id:
                raise ValueError("finish requires --session-id from the current conversation.")
            path, changed = finish(project, args.session_id, args.completed, args.next_move, args.source, args.pending)
            print(f"Saved candidate handoff: {path}")
            if changed:
                print("Current State changed during this session. Reconcile before continuing; no shared records changed.")
    except (ValueError, OSError, KeyError) as error:
        raise SystemExit(str(error)) from error
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
