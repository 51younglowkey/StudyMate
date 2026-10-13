# Contributing to StudyMate

Use a fork and pull request for changes. Ordinary use needs only read/clone
access, not collaborator permissions. Describe the user problem, the resulting
behaviour and relevant validation. Follow AGENTS.md and the evidence rules.

## Local checks

Use Python 3.10+ and Git. Substitute your working Python command if needed:

```bash
python3 -X utf8 -m unittest discover -s tests -v
python3 90_scripts_tools/threading/doctor.py --platform repo
git diff --check
```

On Windows, set `$env:PYTHONUTF8='1'` before running tests so spawned Python
processes and the test runner use the same output encoding. CI sets this for all hosts.

Tests use temporary synthetic projects. Do not use real participant or student
records as fixtures. Keep project data in Git-ignored private workspaces. Review
the complete diff and relevant history before publishing changes.

For onboarding changes, check first use, no-material start, course-material
scope, first useful result and a new conversation continuing the same project.
An automated script test is not a newcomer usability test; report which was run.
For a new host adapter, distinguish documented instruction support from an
actual end-to-end test, and keep shared workflow rules in the core.

## Reporting a problem

Use a GitHub issue with host/OS, Core version or commit, steps, expected/actual
behaviour and a minimal synthetic example. Remove names, credentials, course
originals, private paths and participant content before posting. Do not attach
a whole personal workspace or full chat archive. Missing support should be
labelled rather than invented.
