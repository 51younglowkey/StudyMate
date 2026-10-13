# StudyMate — Claude Code Instructions

StudyMate is an Agent-native, evidence-led Research and Design project workflow.

Use this file as the parallel Claude Code routing layer for the reusable StudyMate workspace. `AGENTS.md` is the primary Codex route; keep the two files conceptually aligned. The optional GSA Pack is loaded only when selected by the user.

## Start here

StudyMate is the display brand; Threading calls remain supported aliases. Keep
technical identifiers and historical records as described in `docs/BRANDING.md`.

1. Read `NOW.md`.
2. Read `core/system_context/workflow_rules.md` before framework changes.
3. Read `core/skill_library/skill_index.md` when routing a method, template or skill request.
4. Read only the files needed for the current task.

Before Dashboard or onboarding work on the first interaction in this clone, run
`python3 90_scripts_tools/threading/install_skill.py` from the repository root.
Then run `python3 90_scripts_tools/project_workspace/upgrade_workspaces.py` in
check mode. Show and confirm any compatibility plan before applying it; if
nothing needs attention, continue normally.
This required, idempotent setup links the StudyMate Skill into the supported
user-level Codex and Claude Code Skill locations so it remains available from
other workspaces. Never overwrite a different existing installation
automatically; report the conflict and continue with the repository instructions.
If user-level writes require permission, request that one bounded approval.
Detect a working Python 3.10+ interpreter first; use `python` or `py -3` when
`python3` is unavailable. Automatic registration falls back to a copy when
symlinks are unavailable; copied Skills need an explicit refresh after updates.

For `Update StudyMate` or `升级 StudyMate，并接续我已有的项目`, check the core
update first. After applying the Core update, show the resulting Compatibility
Plan and require a second confirmation before applying workspace changes.
Preserve existing project records, add only missing schema files and show the
generated Upgrade Report.

For a first-run or `Dashboard` request, read `DASHBOARD.md` and follow
`docs/AGENT_ONBOARDING.md`. Keep complete local project knowledge in
`projects/local/<slug>/`; retain `profiles/local/` only for legacy migration.
Ask permission before inspecting Figma files, desktop folders or chat archives.
Read a selected project's nested `AGENTS.md` and `CURRENT.md` first.

For `启动 StudyMate`, `Start StudyMate`, `我不会用` or an uncertain first use,
follow the guided start in `docs/AGENT_ONBOARDING.md`. Ask what the user wants
to achieve; ideas and materials can coexist. Offer examples rather than asking
only whether they have "materials": course brief, assignment requirements,
rubric/ILOs, teaching slides/PDF, reading, research notes, Figma, prototypes,
tests and chat exports. Follow `docs/MATERIALS_INTAKE.md` for course files and
Canvas/LMS links. Deliver one useful bounded result, not just an empty workspace.
Before selecting a task, follow `docs/PROJECT_FLOW.md`: establish actual progress.
New ideas/course material begin with framing and research; existing projects
enter at the supported stage with upstream evidence gaps checked.
Read `docs/USER_JOURNEY.md` for entry choices and demonstration mode. The current
demo covers framing/research preparation; do not fabricate later-stage evidence
or automatically create a personal workspace merely to demonstrate an answer.
For entry/phase/task questions, follow `docs/NATIVE_CHOICES.md`: prefer an
exposed, permitted native input tool, otherwise use concise text choices.
Respect tool/mode restrictions and submitted-answer semantics. An actual idea
needs an open response; it cannot be inferred from a menu selection alone.
Framework-maintenance requests stay on the framework route.

Bind each conversation to one selected project and follow
`docs/SESSION_HANDOFF.md`. Preserve already-authorised inspection scope without
repeating the same question; ask when new sources or a broader scope are needed.
Course requirements and methods are context, not participant evidence. Student
status does not enable GSA Pack.

For GSA-specific taught-method routing, read `packs/gsa/PACK.md` only after the
user enables the linked, read-only pack. Show its available capabilities and
version after activation. The pack is an independent academic resource for
Design Innovation-related workflows, not an official GSA product.

## Behaviour

- Do not invent evidence, sources, quotations, dates, test results or decisions.
- Keep raw evidence, interpretation, claims and outputs distinct.
- Treat personal, participant-specific and institution-restricted information as sensitive.
- Keep the reusable core separate from any user-owned Managed Workspace.
- Treat taught methods as analytical frameworks, not proof of a project claim.
- Mark missing support with `[EVIDENCE NEEDED]`, `[SOURCE TO VERIFY]`, `[DECISION PENDING]` or `[DATE TO CONFIRM]`.
- Before adding future material or releases, repeat the privacy, provenance and Git-history review.
- Public users should use read/clone access; do not add collaborators merely for ordinary StudyMate use. Keep the optional PDF/image index local and source-authorised.
