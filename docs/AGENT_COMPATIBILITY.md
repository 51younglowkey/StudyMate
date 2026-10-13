# Agent compatibility / Agent 接入

StudyMate shares one core, with small host entry files. Reading an instruction
file is different from verifying the complete workflow on that product.

| Host | Entry | Validation status |
|---|---|---|
| Codex | AGENTS.md + user Skill | Local installation/tool tests; newcomer end-to-end validation still needed |
| Claude Code | CLAUDE.md + user Skill | Skill registration/tool tests; host end-to-end validation still needed |
| Cursor | AGENTS.md | Instruction-compatible entry; StudyMate host workflow not tested |
| Gemini CLI | GEMINI.md, referring to shared AGENTS.md | Entry supplied; StudyMate host workflow not tested |
| Other directory-capable Agents | Explicitly read AGENTS.md and the needed route | Capability-dependent; not a universal compatibility claim |
| Chat-only products | User-provided material and manual handoff | No automatic local persistence without file/connector capabilities |

Host references: [Codex instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[Codex Skills](https://learn.chatgpt.com/docs/build-skills),
[Claude Code context](https://code.claude.com/docs/en/memory),
[Cursor rules](https://cursor.com/docs/rules),
[Gemini CLI context](https://geminicli.com/docs/cli/gemini-md/).
These references describe host mechanisms, not StudyMate test results.

## Agent preflight

- Check for a permitted native user-input tool. Follow
  [Native choices](NATIVE_CHOICES.md) for clickable questions; product name alone
  does not guarantee tool availability, option limits or permitted modes.
- Check that this selected directory contains NOW.md and AGENTS.md. Confirm
  that project instructions were loaded; if not, explicitly read the entry.
- Check available file reading/writing, command execution and durable storage.
  Use available capabilities; explain exactly what cannot persist or run.
- Detect Python 3.10+ with a working command (`python3`, `python`, or `py -3`).
  Do not repeat a non-working WindowsApps alias. If Python is unavailable,
  explain that tool-based setup needs Python and continue bounded conversational
  work without claiming that registration or a Managed Workspace was created.
- On Codex/Claude Code, follow the required registration/check route. On other
  hosts, do not install into unrelated products; repository instructions can be
  used directly. `doctor.py --platform repo` checks the core without requiring
  Codex/Claude registrations; `--platform codex` or `claude` checks one host.
  In a ZIP/non-Git directory, doctor reports the privacy ignore declaration
  separately from actual Git verification; it does not claim Git protection was tested.
- Symlinks are preferred. The installer defaults to `--mode auto`, falling back
  to copying if linking fails. A copy records its core path and needs explicit
  `--mode copy --update` after Core updates. A different clone's installation is
  never automatically replaced.
- Browser or connector access is optional. For course sites, follow
  [Materials intake](MATERIALS_INTAKE.md); inaccessible pages require a relevant
  export or pasted content rather than a promise of automatic crawling.

## Recovery prompt / 启动恢复

In a directory-capable Agent opened on the cloned folder, say:

```text
请读取这个文件夹的 AGENTS.md，并按 docs/AGENT_ONBOARDING.md 启动 StudyMate。
先检查你能使用的工具，再引导我完成一项研究或设计任务。
```

Normal entry: `启动 StudyMate / Start StudyMate`. A repository cannot initiate a
conversation without a user or host trigger. Agents should show readiness and
the next input after this trigger rather than implying a background service.
