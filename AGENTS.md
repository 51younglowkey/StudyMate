# StudyMate Instructions

StudyMate is an Agent-native, evidence-led Research and Design project workflow. Its reusable core is available to every project; an independent GSA Pack provides an optional situated academic context for Design Innovation-related workflows. Each person's project context, evidence and decisions remain their own.

Reply in Chinese by default when the user writes in Chinese. Preserve useful English academic, research and design terms where translation would reduce precision.

## Start and routing

Use StudyMate as the display brand, with no Chinese brand name. Equivalent
Threading commands are supported aliases. Read `docs/BRANDING.md` when handling
name or installation questions; preserve technical identifiers and historical records.

1. Read `NOW.md` for the compact route.
2. Read `core/system_context/workflow_rules.md` before substantive framework changes.
3. Read the closest `AGENTS.md` for any nested project added later.
4. Read only the current files needed for the task; do not scan every source, export or generated file by default.
5. Use `core/skill_library/skill_index.md` to route method and framework requests.
6. Treat `CLAUDE.md` as the parallel Claude Code routing layer.

### Required Skill registration

- At the start of the first interaction in this clone, before Dashboard or onboarding work, run `python3 90_scripts_tools/threading/install_skill.py` from the repository root.
- Then run `python3 90_scripts_tools/project_workspace/upgrade_workspaces.py` in check mode. If it reports compatibility changes or legacy traces, show the plan and ask before applying them. If nothing is found, continue without adding onboarding friction.
- Registration is part of StudyMate setup, not an optional onboarding step. The installer links this clone to the supported user-level Codex and Claude Code Skill locations so StudyMate remains callable from other workspaces.
- The installer is idempotent. If either destination contains a different installation, do not overwrite it automatically; report the exact conflict and continue using the repository-level StudyMate instructions.
- Detect a working Python 3.10+ command first: use `python3`, or `python` / `py -3` when appropriate. Do not repeat a broken WindowsApps alias. The installer uses a symlink when available and falls back to a copy; copied Skills need an explicit refresh after Core updates.
- On other Agent hosts, use repository instructions without installing into unrelated products. Follow `docs/AGENT_COMPATIBILITY.md` and report missing filesystem or execution capabilities.
- If the Agent environment requires approval to write to the user-level Skill directories, ask for that single bounded approval and then resume onboarding.

### Optional packs

- Load the generic StudyMate core by default; do not load an optional pack unless the user selects it.
- When the user selects the GSA Pack, or says “load pack gsa”, read `packs/gsa/PACK.md` before using its methods, reflection-document tool or assessment guide.
- The GSA Pack uses linked, read-only activation. Enabling it records the pack and version in the local project; it does not copy or modify `packs/gsa/`.
- Describe the GSA Pack as an independent academic pack for Design Innovation-related workflows. Never imply that it is official, endorsed or institutionally owned by GSA.

### Agent dashboard and first run

- On a first interaction, or whenever the user asks for `Dashboard`, `status`, `overview` or `next step`, read `DASHBOARD.md` and render its compact text view.
- If no Managed Workspace is selected, follow `docs/AGENT_ONBOARDING.md`. For an existing project, prefer the adoption route over a blank-project intake.
- `启动 StudyMate`, `Start StudyMate`, `我不会用`, or an uncertain first-use request: follow the guided start in `docs/AGENT_ONBOARDING.md`. Start from the user's intended task; ideas and existing materials can coexist. Do not turn framework-maintenance requests into personal-project onboarding.
- Offer concrete material examples: course brief, assignment requirements, rubric/ILOs, teaching PPT/PDF, reading, research notes, Figma, prototypes, tests or chat exports. Read `docs/MATERIALS_INTAKE.md` for course files or Canvas/LMS links. Course requirements, taught methods and research evidence have different roles; being a student does not enable GSA Pack.
- Deliver one useful bounded result before ending onboarding, and leave a clear way to continue. A created directory alone is not a first result.
- Before selecting that result or a next move, follow `docs/PROJECT_FLOW.md`: establish actual progress and evidence gaps. New ideas/course materials start with framing and research, not a prototype menu. Existing projects enter at the supported stage and repair missing upstream links.
- Follow `docs/USER_JOURNEY.md` for conversational entry choices and `先用示例看看 / try the example`. The current demo covers framing/research preparation; later-stage walkthroughs do not invent completed research. Demo mode does not automatically create a personal workspace.
- For missing entry/phase/task preferences, read `docs/NATIVE_CHOICES.md` and prefer an exposed, permitted native user-input tool. Check actual tool availability and mode restrictions; without one, use numbered text. Await a submitted answer before dependent work; preselection is not consent. Use a brief open question to understand the actual idea rather than inferring it from menu choices alone.
- Bind each working conversation to one selected project. Follow `docs/SESSION_HANDOFF.md`; use independent session records and reconcile shared changes. Never silently choose between multiple projects or assume chats share memory.
- Complete user-owned project knowledge belongs in `projects/local/<slug>/` (ignored by Git). `profiles/local/` is a legacy compatibility layer only.
- Read the closest nested `AGENTS.md`, then `CURRENT.md`, before substantive project work.
- Record pointers to Figma, local files, course pages and other repositories in `sources/source_registry.md`; a pointer is not permission to inspect the source.
- Ask for explicit permission before reading a named local or connected source. Never import raw project material automatically.
- Honour source scope already explicitly authorised in the conversation; do not ask again for the same scope. New links/attachments or broader inspection need their own authorised scope.
- Use `90_scripts_tools/project_workspace/adopt_project.py` only after the user confirms the project title, slug and local destination.
- For `整理已经导入的聊天记录` or `reconcile chat archive`, register the user-selected Markdown archive with `reconcile_chat_archive.py`, then review candidates in bounded batches.
- For Figma evolution, let the Agent propose a current candidate and require the user to confirm it before changing `CURRENT.md`.
- Use `manage_pack.py` for linked GSA activation and show the pack capabilities immediately.
- For `Update StudyMate` or `升级 StudyMate，并接续我已有的项目`, run `update_threading.py` in check mode before any `--apply` action. After the Core update, show the resulting Compatibility Plan and require a second confirmation before `--apply-workspaces`. Preserve existing project records, add only missing schema files and produce an Upgrade Report.
- The PDF/image OCR index is an optional local tool. Read its README and require an explicitly authorised source directory before using it; its OCR output is a locator, not automatic project evidence.

## Non-negotiable rules

- Never invent sources, quotations, participant data, citations, page numbers, feedback, test results, dates, findings or design decisions.
- Keep raw evidence separate from cleaned notes, interpretation, synthesis and final outputs.
- Preserve the distinction between evidence, quotation, observation, interpretation, insight, criterion, decision, claim and limitation.
- Preserve traceability for design research: `evidence -> insight -> opportunity -> criteria -> concept -> prototype -> testing -> iteration -> claimed impact`.
- Preserve traceability for academic writing: `source -> note -> interpretation -> claim -> evidence -> counterpoint/limitation -> section -> final argument`.
- Mark missing support explicitly with `[EVIDENCE NEEDED]`, `[SOURCE TO VERIFY]`, `[DECISION PENDING]` or `[DATE TO CONFIRM]`.
- Treat names, contact details, consent records and identifiable raw material as sensitive.
- Do not publish personal, participant-specific, institution-restricted or project-specific material in a reusable edition.
- Read an important file before editing it. Do not overwrite evidence or historical decisions without an explicit reason.
- A method or framework is analytical machinery, not empirical proof. Do not turn a diagram or hypothesis into a validated claim without matching evidence.

## Workspace boundaries

- The reusable core contains rules, methods, templates and tools.
- A Git-ignored Managed Workspace may contain bounded derived knowledge, context, evidence, decisions and outputs. Raw sources may remain in Figma, local folders or chat archives and must retain pointers and provenance.
- Calendar, timetable, deadline and personal-administration records are not part of this edition.
- A future public profile must use neutral examples or user-supplied project data and must document its provenance.

## Repository and generated files

- Keep one repository for this edition unless a later profile genuinely requires independent access control.
- Do not add raw participant material, personal correspondence, private academic administration, local caches, dependencies or generated exports to the public repository.
- Change source files rather than generated output when a source exists.
- Review the complete working tree and Git history before any external publication.

## Lifecycle

Reusable rules and methods may evolve. Historical evidence and user-owned project records should remain dated and should not be silently modernised. If a future profile is archived, preserve its record and mark the lifecycle explicitly.
