# Multiple conversations / 多对话接续

Each conversation works on one selected project. Project files carry memory;
chat windows do not automatically share context. This protocol supports sequential
continuation and separate candidate outputs from concurrent conversations.

## 开始或继续 / Start or resume

1. Use the user's named project or the project folder they opened. If no project
   is named, list only known local project names: with one project, display its
   identity and continue; with multiple, ask which one. Do not scan external
   directories or maintain one global active-project pointer for all chats.
2. Read the nested instructions and `CURRENT.md`, then the handoff relevant to
   the task. If several handoffs compete, show their goals/status and ask which
   thread of work to continue. Modification time is not a current-state decision.
3. State what is confirmed and what remains candidate. Ask only for information
   missing from the current task; do not repeat initial project intake.
4. Start an independent session record. Store the returned session ID in this
   conversation and use it when finishing. It binds the workspace, goal and
   starting `CURRENT.md` hash.

```bash
python3 90_scripts_tools/project_workspace/session_handoff.py start --project projects/local/my-project --goal "Compare the two current directions"
```

Use the working Python command on this machine (`python` or `py -3` if needed).
For an explicitly selected external workspace, add `--allow-external-project`.
The command creates `sessions/<id>/start.json`; it does not read raw materials.

## 工作结束或切换任务 / Save a handoff

Save completed work and output locations, already-inspected sources and scope,
pending confirmations/limitations and one proposed next move. Do not include raw
records or credentials. CLI values are derived notes written by the Agent.

```bash
python3 90_scripts_tools/project_workspace/session_handoff.py finish --project projects/local/my-project --session-id <returned-id> --completed "Saved the candidate comparison in outputs/directions.md" --source "S-001 / brief / assignment section only" --pending "Owner has not selected a direction" --next-move "Review the comparison and choose the next test"
```

The source flag records scope already inspected under authorisation; it neither
grants permission nor opens a source. Complete a handoff only after the named
work actually occurred. The saved `handoff.md` is candidate session progress,
not new research evidence or an automatic decision.

The tool refuses to overwrite an earlier handoff. Start a new session for later
work. If CURRENT changed since the session began, the handoff is marked
`needs-reconciliation`. This may be an expected owner-approved change from this
conversation; read it and reconcile rather than treating the warning as failure.
Show a brief continuation card and an example prompt:

```text
本次完成：<actual work + output>
仍需确认：<pending decision or evidence>
建议接续：<one concrete task>
新对话可说：继续 <project title>，接着处理 <task>。
```

## 并行边界 / Concurrent work

Use separate session IDs and outputs. Shared CURRENT/evidence/decision records
have one writer at a time; compare current contents immediately before any
owner-approved write and reconcile competing changes. Owner confirmation is
still required for CURRENT promotion.

The tool checks CURRENT hashes and protects its own handoff from replacement.
It does not lock edits by other tools, make shared log writes transactional or
detect changes to every source. Fully simultaneous shared writes are not supported.
No write to CURRENT.md or shared logs is performed by this tool.

Existing schema-2 projects can create `sessions/` lazily. Compatibility checks
may propose missing instructional files, but applying them remains separately
confirmed and never rewrites historical decisions.
