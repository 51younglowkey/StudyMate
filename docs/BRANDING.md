# StudyMate naming and compatibility

Confirmed on 2026-10-13: the display brand is **StudyMate**, with no Chinese
brand name. Chinese documentation is explanatory text, not an alternate brand.
This independent Research and Design workflow was previously called Threading.

## Current calls

- `启动 StudyMate / Start StudyMate`
- `StudyMate Dashboard`
- `StudyMate doctor`
- `Update StudyMate / 升级 StudyMate，并接续我已有的项目`

Equivalent Threading calls remain supported aliases. Interpret them through the
same routes and preserve the user's existing authorisation and project selection.

## Retained technical identifiers

The canonical GitHub repository is `https://github.com/51younglowkey/StudyMate`.
New clones default to a `StudyMate` folder; existing local folders need no rename.
Script paths retain `threading`. The registered Skill's ID remains `threading` and can
be explicitly called with `$threading`; its UI display name is StudyMate.
No `$studymate` Skill ID is claimed in this version.

`threading.json`, `threading_version`, `[THREADING VERSION]` and the
`Threading core version` metadata field retain their schema meaning. Existing
installation paths, backups, reports and legacy migrations continue to work.
Renaming the display brand does not require moving projects or rewriting records.

Public v0.3.0 release notes, copyright-holder names, dated extraction/publication
records and generated historical indexes retain the name used when recorded.
New active UI/documentation uses StudyMate; prior releases are still reconstructable.

The owner authorised the GitHub update on 2026-10-13. Existing clones can update
their remote explicitly with:

```bash
git remote set-url origin https://github.com/51younglowkey/StudyMate.git
```

Existing GitHub links are checked after the rename. This update changes the
default-branch contents; v0.3.0 remains the latest tagged release.
