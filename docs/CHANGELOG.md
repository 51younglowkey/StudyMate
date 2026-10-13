# StudyMate Changelog

## Unreleased

- Renamed the display brand and GitHub repository to StudyMate, with no Chinese
  brand name. Updated clone instructions while preserving legacy Threading
  calls, installation identifiers and schema fields.

- Added native-question preference with host/mode checks, text fallback and
  explicit submitted-answer handling; actual ideas still need open input.
- Documented four conversational entries, the actual demo sequence and
  stage-dependent choices; clarified that the sample stops at research preparation.
- Added stage-aware progression: new ideas/course material start with framing
  and research; later concept/prototype tasks require an explicit upstream basis.
- Added a task-first `Start StudyMate / 启动 StudyMate` entry and concrete
  material suggestions, including course briefs, rubrics, teaching files and
  bounded Canvas/LMS inspection using available host tools.
- Added independent session binding/handoffs, Current State change detection
  and an explicit single-writer boundary for shared project records.
- Fixed Dashboard empty decision counts and placeholder next-move fallthrough;
  moved record counts to `--details` and made the Welcome view task-oriented.
- Added course/web pointer registration, Gemini entry files and host capability
  guidance. Cross-host newcomer workflows still need end-to-end validation.
- Added automatic copied-Skill fallback and host-scoped doctor checks.
- Made ZIP/non-Git doctor checks disclose when ignore rules are declared but
  could not be verified by Git.
- Added synthetic first-task material and onboarding regression coverage.

## 0.3.0 — 2026-08-12

- Added non-destructive compatibility upgrades for existing Managed Workspaces.
- Added legacy-profile attachment, missing-schema repair and Upgrade Reports.
- Connected `Update Threading` to project compatibility checks and migration.
- Registered the Threading Skill for both Codex and Claude Code user scopes.

## 0.2.0 — 2026-08-11

- Added full local Managed Workspaces under `projects/local/<slug>/`.
- Added an installable `threading` skill for natural-language routing.
- Added `CURRENT.md` as the confirmed current-state layer for each project.
- Added existing-project adoption, legacy-profile migration and conservative Dashboard tools.
- Added Figma evolution and existing-chat reconciliation workflows.
- Changed the GSA Pack to linked, read-only activation by default.
- Added version, update, doctor and existing-user upgrade routes.

## 0.1.0 — 2026-08-11

- Published the privacy-reviewed reusable Threading core.
- Added the text Dashboard, legacy project-profile scaffold, optional GSA Pack and PDF/image index.
