---
name: threading
description: Guide Research and Design projects with StudyMate (formerly Threading), from first use to continuing work. Use for 启动 StudyMate / Start StudyMate and legacy Threading calls, project adoption, Dashboard, course-material intake, evidence gaps, Figma or chat reconciliation, session handoff, optional GSA Pack, and StudyMate diagnosis or updates. Keep framework maintenance separate from personal-project onboarding.
---

# StudyMate

Display brand: StudyMate. The technical Skill ID remains `threading`. Equivalent
Threading calls are legacy aliases for all routes below; preserve their existing
scope and selection. Read core `docs/BRANDING.md` for identifier compatibility.

Use StudyMate as the operating layer for a user-owned local project. Keep the
public core, local project knowledge and raw sources separate.

## Resolve the core

1. If this skill is symlinked from a StudyMate clone, resolve the skill path and
   use the repository containing `VERSION`, `DASHBOARD.md` and `packs/gsa/`.
2. For a copied installation, read `references/core-path.txt` when it exists.
3. If no core can be located, ask for the StudyMate clone path; do not scan a
   home directory or broad disk location.

## Route the request

For missing first-use or task preferences, read core `docs/NATIVE_CHOICES.md`.
Prefer an exposed and permitted native question tool; otherwise use numbered
text. Follow tool/mode constraints and wait for a submitted answer before
dependent work. Native choices do not replace understanding the actual idea.

- `先用示例看看`, `try the example`, demo/simulation of first use: read core
  `docs/USER_JOURNEY.md` and `examples/first-task/README.md`. Use the supplied
  synthetic exercise for framing/research preparation; do not invent completed
  empirical stages or automatically create a personal workspace.
- `启动 StudyMate`, `Start StudyMate`, `我不会用`, uncertain first use: read the
  core `docs/AGENT_ONBOARDING.md` guided start. Begin with the desired task, offer
  concrete materials and deliver one useful result. Ideas and materials coexist.
  Use core `docs/PROJECT_FLOW.md` to establish actual stage before selecting that
  result; idea/course-only projects default to framing and research.
  Core `docs/USER_JOURNEY.md` defines entry and stage-appropriate choices.
- Course brief, rubric, teaching PPT/PDF or Canvas/LMS links: read the core
  `docs/MATERIALS_INTAKE.md`. Requirements, methods and research evidence have
  different roles. Use available tools only within explicit source scope.
- `Dashboard`, `status`, `overview`, `next step`, `查看依据`: read the selected project's
  `CURRENT.md`, `packs.md` and bounded records; use the core Dashboard contract.
- `新建项目`, `start a new project`, `set up a project`: follow the new-project
  route in `references/routes.md`, create or select a Managed Workspace and begin
  with the working question, intended outcome and uncertainty.
- `接管项目`, `adopt project`, `orient this project`: follow
  `references/routes.md#existing-project-adoption`.
- `继续推进项目`, `continue this project`, `keep working`: read the selected
  Managed Workspace and core `docs/SESSION_HANDOFF.md`; bind this conversation,
  read relevant handoffs and follow the current-state / next-move route.
  Use core `docs/PROJECT_FLOW.md` to check the basis for the proposed stage.
- `整理已经导入的聊天记录`, `reconcile chat archive`: follow
  `references/routes.md#chat-reconciliation`.
- `map Figma`, `current Figma`, `which design is current`: follow
  `references/routes.md#figma-evolution`.
- `load pack gsa`, `use GSA Pack`: enable the linked pack for the selected
  workspace, then show its capabilities and version.
- `update StudyMate`, `升级 StudyMate，并接续我已有的项目`: run the safe core
  update check first. After approval, apply the Core update and show the
  resulting compatibility plan. Apply workspaces only after the user has seen
  that plan; report Managed Workspace repairs and legacy migrations.
- `what can you do`, `help`: render the concise capability view in
  `references/routes.md#capability-view`.
- `evidence gaps`, `find the evidence gaps`, `找出证据缺口`: inspect bounded
  project records and report unsupported claims, missing source pointers and
  pending confirmations without inventing support.

## Non-negotiable behaviour

- Require a selected Managed Workspace before writing project knowledge.
- Bind each conversation independently; do not maintain one global active-project
  pointer across chats. Keep concurrent outputs separate and reconcile shared writes.
- Ask before inspecting a local path, Figma source or chat archive.
- Honour already-authorised source scope without asking again. Never infer that
  a course link authorises an entire LMS, all attachments or other people's data.
- Preserve raw sources; store derived local knowledge with source pointer,
  extraction date, scope and status.
- Treat imported or model-generated material as `candidate` until the user
  confirms it.
- Let the Agent propose a current Figma file/page/frame; require user
  confirmation before changing `CURRENT.md`.
- Never delete or silently rewrite superseded decisions. Record the new state
  and retain the earlier state in history.
- Keep `projects/local/` private and Git-ignored.
- Treat the linked GSA Pack as read-only. Write project analysis into the local
  workspace, never into `packs/gsa/`.

Read `references/workspace-schema.md` when creating, migrating or repairing a
Managed Workspace. Read only the route needed for the current request.
