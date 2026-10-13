#!/usr/bin/env python3
"""Render StudyMate's project-aware text Dashboard."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from common import PROJECTS_ROOT, ROOT, field, resolve_project
from session_handoff import session_folder


LEGACY_ROOT = ROOT / "profiles" / "local"
PLACEHOLDER_PREFIXES = ("[DECISION PENDING]", "[EVIDENCE NEEDED]", "[SOURCE TO VERIFY]", "[DATE TO CONFIRM]")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a StudyMate Managed Workspace Dashboard.")
    parser.add_argument("--project", type=Path)
    parser.add_argument("--allow-external-project", action="store_true")
    parser.add_argument("--details", action="store_true", help="show record counts and pack metadata")
    parser.add_argument("--session-id", help="show only this conversation's saved handoff")
    return parser.parse_args()


def local_projects() -> list[Path]:
    if not PROJECTS_ROOT.is_dir():
        return []
    return sorted(path for path in PROJECTS_ROOT.iterdir() if path.is_dir())


def first_section_value(text: str, heading: str, fallback: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}[ \t]*\r?$\n(.*?)(?=^## |\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        return fallback
    for line in match.group(1).splitlines():
        value = line.strip()
        if not value or value.startswith("<!--"):
            continue
        # An explicit missing value must not fall through into explanatory prose.
        if value.startswith("|") or value.startswith(PLACEHOLDER_PREFIXES):
            return fallback
        return value
    return fallback


def table_data_rows(path: Path) -> int:
    if not path.exists():
        return 0
    count = 0
    in_data = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            in_data = False
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            in_data = True
            continue
        if in_data and any(cells) and not any("[SOURCE TO VERIFY]" in cell for cell in cells):
            count += 1
    return count


def render_welcome() -> None:
    print("STUDYMATE / WELCOME")
    print("────────────────────────────────────────────────────────────────")
    print("先说：启动 StudyMate / Start StudyMate。也可以直接描述你卡在哪里。")
    print("你希望这次推进什么？有想法、已有材料、有具体卡点都可以同时成立。")
    print("可以提供：课程 brief、作业要求、评分标准、PPT/PDF、阅读材料，")
    print("          访谈/观察笔记、Figma、原型、测试记录或聊天导出。")
    print("也可以提供 Canvas 等课程页面链接，并说明允许检查哪一页。")
    print("没有材料也能开始；先用一个明确标为合成的示例体验也可以。")
    print("可选择：1 先体验示例 / 2 新建项目 / 3 接入已有项目 / 4 继续已有项目")
    print("下一步 / Next move：说明你的需求，Agent 会带你完成第一项有用的工作。")
    print("────────────────────────────────────────────────────────────────")


def render_project(project: Path, details: bool = False, session_id: str | None = None) -> None:
    current = (project / "CURRENT.md").read_text(encoding="utf-8")
    packs = (project / "packs.md").read_text(encoding="utf-8") if (project / "packs.md").exists() else ""
    title = field(current, "Project", project.name)
    phase = field(current, "Current phase", "orientation")
    confirmed = field(current, "Last confirmed", "[DATE TO CONFIRM]")
    confirmation = field(current, "Confirmation status", "needs confirmation")
    question = first_section_value(current, "Current question", "[DECISION PENDING]")
    direction = first_section_value(current, "Current direction", "[DECISION PENDING]")
    next_move = first_section_value(current, "Next move", "[DECISION PENDING]")
    gsa = field(packs, "GSA Pack", "disabled")
    gsa_version = field(packs, "GSA Pack version", "none")
    sources = table_data_rows(project / "sources" / "source_registry.md")
    evidence = table_data_rows(project / "evidence" / "evidence_log.md")
    decisions = table_data_rows(project / "decisions" / "decision_log.md")
    chat_candidates = table_data_rows(project / "sources" / "chats" / "candidate_records.md")

    print("STUDYMATE / PROJECT DASHBOARD")
    print("────────────────────────────────────────────────────────────────")
    print(f"Project         {title}")
    try:
        display = f"{project.relative_to(ROOT)}/"
    except ValueError:
        display = f"<external project>/{project.name}/"
    print(f"Phase           {phase}")
    print(f"Current status  {confirmation}")
    print(f"Current question {question}")
    print(f"Current direction {direction}")
    uncertainty = first_section_value(current, "Open contradiction or uncertainty", "[EVIDENCE NEEDED]")
    print(f"Open question   {uncertainty}")
    print(f"NEXT MOVE       {next_move}")
    if next_move == "[DECISION PENDING]":
        print("先说明这次想解决什么；可提供一份课程要求或项目材料，也可以只描述想法。")
    if session_id:
        handoff = session_folder(project, session_id) / "handoff.md"
        if handoff.is_file():
            record = handoff.read_text(encoding="utf-8")
            print(f"Session status  {field(record, 'Status', 'unknown')}")
            print(f"Completed work  {first_section_value(record, 'Completed work', 'None recorded')}")
            print(f"Proposed resume {first_section_value(record, 'Proposed next move', '[DECISION PENDING]')}")
        else:
            print("Session handoff  No completed handoff saved for this conversation.")
    else:
        print("Session handoff  未选定会话记录；可用 --session-id 查看，候选进度不替代 Current State。")
    if not details:
        print("────────────────────────────────────────────────────────────────")
        print("可回复：继续 / 换个任务 / 查看依据。运行 --details 查看记录数量。")
        return
    print()
    print(f"Workspace       {display}")
    print(f"Last confirmed  {confirmed}")
    print("KNOWLEDGE")
    print(f"  Sources       {sources} registered")
    print(f"  Evidence      {evidence} records")
    print(f"  Decisions     {decisions} records")
    print(f"  Chat review   {chat_candidates} candidates")
    print()
    print(f"GSA PACK        {gsa} / version {gsa_version}")
    if gsa == "enabled":
        print("  Methods / Provotyping / Reflection Document / Stage 3 audit")
    print("────────────────────────────────────────────────────────────────")
    print("可回复：继续 / 换个任务 / 查看依据。")


def main() -> int:
    args = parse_args()
    if args.project:
        try:
            project = resolve_project(args.project, args.allow_external_project)
            render_project(project, args.details, args.session_id)
        except (ValueError, OSError) as error:
            raise SystemExit(str(error)) from error
        return 0

    projects = local_projects()
    if not projects:
        render_welcome()
        if LEGACY_ROOT.is_dir() and any(path.is_dir() for path in LEGACY_ROOT.iterdir()):
            print("Legacy profiles detected. Say: migrate my old StudyMate profile")
        return 0
    if len(projects) > 1:
        print("STUDYMATE / SELECT A PROJECT")
        for project in projects:
            print(f"- {project.name}")
        print("Ask the user which project to open; do not choose silently.")
        return 0
    render_project(projects[0], args.details, args.session_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
