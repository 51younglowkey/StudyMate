# StudyMate Quickstart / 快速开始

## 1. 下载并打开 / Get the folder

在终端（Windows PowerShell / macOS Terminal）运行：

```bash
git clone https://github.com/51younglowkey/StudyMate.git
cd StudyMate
```

没有 Git 时，在 GitHub 点 **Code → Download ZIP** 并解压。
Open the downloaded StudyMate folder as a local project/workspace in your
directory-capable Agent, then start a new conversation there. A workspace is the
folder the Agent works in. Codex/Claude Code have instruction and Skill entries;
other hosts use [Agent compatibility](AGENT_COMPATIBILITY.md).

## 2. 一句话启动 / One entry

```text
启动 StudyMate
```

Or say `Start StudyMate`. The Agent checks available file/Python capabilities,
follows the required setup on supported hosts, then shows `STUDYMATE / WELCOME`
and guides your first task. You do not need to remember method or command names.

若入口没加载，可发送：

```text
请读取这个文件夹的 AGENTS.md，并按 docs/AGENT_ONBOARDING.md 启动 StudyMate。
```

Python tools need Python 3.10+. The Agent should detect a working `python3`,
`python` or `py -3`; explain missing capabilities rather than claiming setup
succeeded. Skill registration defaults to linking with a copy fallback.
An unrelated existing installation is preserved; copied Skills require explicit
refresh after Core updates.

## 3. 需求和材料一起说 / Bring your task and materials

可以只有想法，也可以同时有想法、已有材料和具体卡点。比如：

```text
我有一个服务设计想法，也有课程 PPT 和作业要求。
帮我看要求与我的目标如何对应，先找到一个可以推进的任务。
```

You can upload, paste or name one useful source, depending on host capabilities:

- course brief, assignment requirements, rubric/ILOs;
- teaching PPT/PDF, readings and reference material;
- your own notes, drafts, Figma, prototypes or test records;
- chat exports or an existing project handoff;
- named Canvas/LMS course pages, with explicit inspection scope.

课程要求用于判断交付与评价，教学内容用于理解背景与方法，研究记录用于支持项目
判断。按 [Materials intake](MATERIALS_INTAKE.md) 分开处理；无须上传全部课程。
Inaccessible websites/files need a relevant export, attachment or pasted text.
No automatic whole-course crawling or GSA Pack activation is implied.

没有材料也可以开始；可以说 `先用示例看看`，使用
[`examples/first-task/`](../examples/first-task/README.md) 中明确标为合成的练习。

## 4. 得到第一项成果 / First useful result

The Agent asks only for missing information, proposes and confirms a project
title, slug and destination when persistence is needed, then completes one task:
a requirements map, working question, evidence gap, comparison or test proposal.
It distinguishes inspected sources, interpretation and pending decisions.
First establish actual progress with [Project flow](PROJECT_FLOW.md). Ideas and
course-only materials default to framing, source review and research planning.
Comparison/prototype/testing work needs its upstream basis; an existing project
can enter at its supported stage without repeating valid research.

Project knowledge is private under Git-ignored `projects/local/<slug>/` unless
you explicitly choose another location. Raw materials can stay at their source.
Only the owner confirms promotion into `CURRENT.md`; earlier decisions remain.

## 5. 开新对话继续 / Continue in another conversation

```text
继续 <项目名>，接着处理 <任务>
```

The Agent binds this conversation to the named project, reads Current State and
the relevant independent [handoff](SESSION_HANDOFF.md), and continues without
repeating intake. Multiple projects require an explicit selection. Concurrent
outputs stay separate and shared records need coordinated reconciliation.

`Dashboard` shows the current task, uncertainty and next action. `查看依据` or
the Python renderer's `--details` adds record counts and metadata.
`加载 GSA Pack` remains an explicit optional choice.

## 6. 后续更新 / Update later

Say `升级 StudyMate，并接续我已有的项目 / Update StudyMate`.
The Agent checks Core state, then separately shows and confirms workspace
compatibility changes before applying them. See [Updating](UPDATING.md).
ZIP downloads do not have the Git history the update tool needs: acquire a new
Core separately, preserve private projects and use a reviewed compatibility plan.

Full operating guide: [Agent onboarding](AGENT_ONBOARDING.md).
