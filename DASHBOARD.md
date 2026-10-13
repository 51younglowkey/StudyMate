# StudyMate Dashboard

StudyMate is an Agent-native, evidence-led project workflow for Research and
Design. It can start a project, accompany its full lifecycle or join an
already-developed project. The local Managed Workspace holds the project's
working knowledge and history.

## Welcome view

Use this when no Managed Workspace is selected or the user asks what StudyMate
can do. Render in the user's language; this Chinese view is a concrete example:

```text
STUDYMATE / WELCOME
────────────────────────────────────────────────────────────────
先说：启动 StudyMate。也可以直接描述你卡在哪里。
你希望这次推进什么？有想法、已有材料、有具体卡点都可以同时成立。
可以提供：课程 brief、作业要求、评分标准、PPT/PDF、阅读材料，
          访谈/观察笔记、Figma、原型、测试记录或聊天导出。
也可以提供 Canvas 等课程页面链接，并说明允许检查哪一页。
没有材料也能开始；先看合成示例也可以。
下一步：说明你的需求，Agent 会带你完成第一项有用的工作。
也可选择：1 先体验示例 / 2 新建项目 / 3 接入已有项目 / 4 继续已有项目
────────────────────────────────────────────────────────────────
```

Follow `docs/USER_JOURNEY.md` for these choices. They are entry routes, not
mutually exclusive material categories or permission to skip research stages.
Skip the menu when the user has already given a task.
Use `docs/NATIVE_CHOICES.md` to present needed choices through a permitted native
tool when available. The text renderer prints guidance only; it cannot create
Codex-native question UI. Do not equate a printed list with a displayed form.

## Natural-language routes

- `启动 StudyMate`, `Start StudyMate`, `我不会用`: follow the guided start in
  `docs/AGENT_ONBOARDING.md`; use task-first intake, not a fixed questionnaire.
- Course files or Canvas/LMS links: follow `docs/MATERIALS_INTAKE.md`; combine
  the user's intended task with bounded authorised materials.
- `Dashboard`, `status`, `overview`: render the selected project's current view.
- `帮我新建一个项目空间`, `start a new project`: create or select a Managed
  Workspace and begin with a question, intended outcome and uncertainty.
- `帮我接管这个现有项目`, `adopt project`: create or select a Managed Workspace,
  register source pointers, orient bounded sources and propose Current State.
- `继续推进这个项目`, `continue this project`: read the selected workspace,
  show its Current State and propose the next evidence-led move.
- `整理已经导入的聊天记录`, `reconcile chat archive`: register the selected
  Markdown archive, extract candidates and ask before promotion.
- `帮我整理 Figma 的演变`, `map Figma`: record file/page/frame evolution and
  propose a current candidate for user confirmation.
- `加载 GSA Pack`, `load pack gsa`: enable the linked pack and show its methods,
  Provotyping, Reflection Document and Stage 3 capabilities.
- `Update StudyMate`, `升级 StudyMate，并接续我已有的项目`: check tracked
  changes and remote state, then preview compatibility repairs and legacy-trace
  connections before applying them.
- `帮我找出 evidence gaps`, `find the evidence gaps`: report unsupported claims,
  missing source pointers and pending confirmations in bounded project records.
- `StudyMate doctor`: verify core, skill, privacy ignore, project schema and pack.

## Project view

Read the selected `projects/local/<slug>/CURRENT.md`, `packs.md` and bounded
records and relevant session handoff. Do not infer current state from file
modification time alone. Default to an actionable view; do not fill missing
support with invented findings. Describe a proposed task as proposed.
Use `docs/PROJECT_FLOW.md` to show the supported stage and missing upstream
connection. New ideas/course materials lead to framing and research work;
the Dashboard must not treat any chosen output as evidence of stage readiness.

```text
STUDYMATE / PROJECT DASHBOARD
────────────────────────────────────────────────────────────────
当前项目        <title> / <phase>
我理解你在做    <confirmed question/direction or pending>
本次已经完成    <actual work + output; none if no handoff/work exists>
目前卡在哪里    <supported gap or uncertainty; label missing support>
建议下一步      <one concrete proposed action + basis or confirmation needed>
需要你提供      <one relevant source/input; or no further material needed>
可直接回复      继续 / 换个任务 / 查看依据
────────────────────────────────────────────────────────────────
```

`查看依据 / --details` adds workspace location, confirmation date/status, source
and record counts, source scope and linked-Pack metadata. The Python renderer
reports stored fields; the Agent interprets them only with matching support.
When Next move is missing, offer task-first intake rather than displaying
template instructions as an action. Keep all confirmed/candidate labels visible.
The renderer's `--session-id <id>` shows the explicitly selected conversation's
completed work and proposed continuation; it never silently chooses a latest handoff.

## Current-state rule

Root `NOW.md` describes StudyMate itself. A local project's `CURRENT.md`
describes what that school/research/design project currently accepts as active.
The Agent may propose changes from newer Figma or chat material, but only the
user can confirm promotion to Current State. Preserve earlier states in decision
and iteration history.

## Source boundary

Raw Figma files, desktop folders and complete chat archives may stay in their
original locations. Bounded derived text may live in the local Managed Workspace
when it records source ID, pointer, inspected scope, date and status. A pointer
is not inspection permission. Course files and LMS pages follow
`docs/MATERIALS_INTAKE.md`; cross-conversation work follows `docs/SESSION_HANDOFF.md`.
