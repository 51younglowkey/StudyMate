# StudyMate — NOW

Updated: 2026-10-13

Working-tree development (2026-10-13): guided first use, course-material intake,
host entries and independent conversation handoffs are under **Unreleased** in
`docs/CHANGELOG.md`. The public release below remains v0.3.0; this development
work is not yet a new GitHub release. Use `启动 StudyMate / Start StudyMate` for
the guided entry; framework maintenance stays on its own route.

Brand decision (2026-10-13): **StudyMate**, English name only. Natural entry:
`启动 StudyMate / Start StudyMate`. Legacy `Threading` commands remain aliases.
See `docs/BRANDING.md` for retained technical identifiers.

## Workspace

StudyMate is an Agent-native, evidence-led Research and Design project workflow. Its reusable core was extracted from a private academic workspace and is intended for projects with different contexts but similar needs around research organisation, evidence traceability, methods, design iteration and writing. An independent GSA Pack is available as an optional Design Innovation academic context.

Current working Core: **v0.3.0**.

Current status: **v0.3 Managed Workspace implementation with an automatically registered
StudyMate Skill, Current State, linked GSA Pack, existing-chat reconciliation,
non-destructive compatibility upgrades and safe migration tools**.

Latest public release (published as Threading): **v0.3.0** — [GitHub release](https://github.com/51younglowkey/StudyMate/releases/tag/v0.3.0)

Release decision (2026-08-11): the owner chose a public GitHub repository. Users
will view, clone or download Threading without collaborator access; changes should
come through forks and pull requests. Complete local project knowledge lives in
Git-ignored Managed Workspaces inside the clone or at an explicitly chosen
external path. The PDF/image index remains an
optional tool, not a core onboarding dependency.

```text
StudyMate
├── system rules and repository boundaries
├── automatically registered natural-language StudyMate Skill
├── linked read-only GSA Pack with methods, reflection-document analysis and Stage 3 assessment guidance
├── evidence, reading, interview and prototype templates
├── complete Git-ignored Managed Workspaces under projects/local/
├── Current State, Figma evolution and chat reconciliation routes
├── compatibility upgrade reports and legacy-trace connection
├── Agent-native text Dashboard and existing-project adoption
└── bounded indexing and file utilities
```

## Start here

- `AGENTS.md` — Codex route
- `CLAUDE.md` — Claude Code route
- `DASHBOARD.md` — text Dashboard and natural-language routes
- `docs/AGENT_ONBOARDING.md` — existing-project adoption and new-project route
- `core/system_context/workflow_rules.md` — evidence and decision rules
- `core/system_context/EXTRACTION_STATUS.md` — what was removed and the v0.2 status
- `core/skill_library/skill_index.md` — method and framework routing
- `core/skill_library/skills/apply-taught-methods/` — generic method application route
- `packs/gsa/PACK.md` — optional Design Innovation academic pack, including ILO/rubric guidance
- `core/templates/` — neutral starting templates
- `docs/QUICKSTART.md` — first-use route
- `profiles/_template/` — legacy v0.1 profile scaffold (migration only)
- `projects/_template/` — full Managed Workspace scaffold
- `skills/threading/` — shared Skill source registered for Codex and Claude Code
- `90_scripts_tools/project_workspace/` — adoption, Dashboard, pack, chat and migration tools
- `90_scripts_tools/threading/` — install, update and doctor tools

No timetable, deadline calendar, participant archive or private project evidence belongs in this core. Local derived project knowledge belongs only in ignored Managed Workspaces. Optional packs are not enabled unless the user selects one.
