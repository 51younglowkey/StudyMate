# StudyMate Agent-native Onboarding

这是一份完整的项目说明书。README 负责让人快速开始；本文件负责说明
StudyMate 如何从项目早期、项目中段或已有项目进入，并如何持续推进到项目成果。

---

## 中文说明

### 第一次使用：先推进一件事

入口选项与示例模拟按 [`USER_JOURNEY.md`](USER_JOURNEY.md)：先体验示例、新建自己的
项目、接入已有项目或继续已有项目。用户已说明意图时跳过菜单；当前阶段内只提供
少量相关动作。示例只覆盖 framing 与调研准备，后续流程展示不能假装调研已经发生。
需要用户选择时，按 [`NATIVE_CHOICES.md`](NATIVE_CHOICES.md) 优先使用宿主提供且
当前允许的原生选择框；没有该能力才用文字选项。入口与阶段可以点选，用户的具体
想法则用一个开放问题了解。没有提交答案时，不把默认选项当成用户决定。

用户说 `启动 StudyMate`、`我不会用`，或直接描述卡点时，Agent 先检查可用工具，
然后问：**你希望这次推进什么？** 用户可以同时有想法、已有材料和具体需求。
不要要求在“只有想法”和“有材料”之间二选一；已有明确任务时直接接着做。
选择具体任务前，按 [`PROJECT_FLOW.md`](PROJECT_FLOW.md) 判断已经做过哪些调研与
分析、现有依据支持哪个阶段。只有想法或课程资料时，默认先明确问题和调研缺口，
再规划与开展调研；不直接把“推进原型”作为并列入口。已有项目按有依据的阶段接续。
用户想先体验时，使用 `examples/first-task/` 的合成练习，不自动建立个人空间。

举相关例子帮助用户回答：课程 brief、作业要求、评分标准/ILOs、教学 PPT/PDF、
阅读材料、自己的研究笔记、Figma、原型、测试记录、草稿或 AI 聊天导出。
也可以提供 Canvas 等课程页面链接，并明确允许检查哪一页或哪些附件。
按宿主能力上传、粘贴或指定文件；没有材料也可以从想法开始，或先看合成示例。

课程与网页材料按 [`MATERIALS_INTAKE.md`](MATERIALS_INTAKE.md) 处理：课程要求影响
交付与评价，教学内容帮助选择方法，用户需求与研究证据支持项目方向。它们不能
相互替代，也不会因为用户是学生而自动启用 GSA Pack。

只问当前任务缺少的信息。需要持久记录时，Agent 提议名称、slug 和默认本地位置，
让用户一次确认后建立空间。先选一份有用且获授权的材料；不要索要整门课或全部历史。
首轮应交付一项实际工作，例如要求与现有成果的对应表、问题草案、方向比较、
证据缺口或测试建议。清楚标出来源、推断与仍待确认的部分。
这些成果按阶段选择：新项目优先问题梳理、相关来源审阅和调研计划；方向比较和测试
建议需要前序依据，不能把提供资料等同于已完成调研。

空间建立和 Current State 草案只是过程。结束时说明本次完成了什么、下一步需要什么，
并按 [`SESSION_HANDOFF.md`](SESSION_HANDOFF.md) 保存独立交接记录。
框架维护请求继续走 Framework Fix，不自动转成个人研究项目 intake。

### 1. StudyMate 的工作方式

StudyMate 是一个面向 Research and Design 的 Agent-native、evidence-led 项目工作流。
它把项目从问题和目标推进到可解释、可交付、可继续迭代的成果：

```mermaid
flowchart LR
    A[新建项目] --> W[Managed Workspace]
    B[接入已有项目] --> W
    C[继续推进项目] --> W
    W --> Q[Question]
    Q --> S[Sources]
    S --> E[Evidence]
    E --> I[Insight & criteria]
    I --> D[Decision]
    D --> P[Prototype]
    P --> T[Testing & iteration]
    T --> O[Outcome]
```

StudyMate 的完整工作流可以从任意阶段进入。Agent 会先判断项目已经有什么、还缺什么，
再提出下一步；它不会因为材料已经存在，就把旧内容自动当成当前事实。

### 2. 选择项目入口

#### 从零开始

适用于只有一个兴趣、问题、brief 或初步方向的项目。Agent 会帮助你建立：

- project title 和 slug；
- working question；
- intended outcome；
- 当前不确定性；
- 初步 source map 和 evidence plan；
- 一个可以继续工作的 Managed Workspace。

可以直接说：

```text
帮我新建一个项目空间
我想从零开始做一个 service design project
帮我建立一个 evidence-led product design workflow
```

#### 从项目早期开始持续推进

适用于已经有 brief、研究问题或设计目标，但还没有完整方向的项目。Agent 会按顺序
帮助你建立 source、evidence、insight、criteria、decision、prototype 和 testing，
每一步都保留不确定性和下一步验证方式。

可以说：

```text
帮我把这个 brief 变成一个可工作的 research question
帮我建立这个项目的 evidence plan
帮我把当前 insight 转成 design criteria
```

#### 接入已经形成的项目

适用于 Figma、本地文件夹、PDF、图片或 ChatGPT 导出已经存在的项目。Agent 会先登记
source pointers，再请求对明确来源的有限检查权限；原始材料继续留在原位置。

可以说：

```text
帮我接管这个现有项目
帮我把这个项目整理成 StudyMate Workspace
帮我判断这个项目现在真正工作的方向
```

#### 继续一个已经运行中的项目

适用于已经有 Managed Workspace、Current State 和历史记录的项目。Agent 先读取项目
自己的 `AGENTS.md`、`CURRENT.md`、`packs.md` 和有边界的记录，再帮助你更新当前状态、
证据、决策、原型或下一步行动。

可以说：

```text
继续推进这个项目
Dashboard
帮我找出这个项目现在最重要的下一步
```

### 3. 第一次对话应该确认什么

Agent 按当前任务逐步确认，不把下面的信息变成固定的八轮问卷；已有答案不重复问：

1. 这次想解决的问题或得到的成果；
2. 相关的已有材料与允许检查的范围；没有材料也可以先工作；
3. 必要的项目阶段、类型、限制与不确定性；
4. 需要保存时，确认 Agent 提议的项目名称、slug 和本地位置；
5. 只有用户选择时才启用 linked GSA Pack。

除非你明确选择外部路径，项目知识保存在：

```text
projects/local/<slug>/
```

这是被 Git 忽略的本地 Managed Workspace。公共 StudyMate core、其他项目和原始来源
保持分离。

### 4. 来源登记与检查权限

StudyMate 先记录 source pointer，再请求 inspection permission。登记一个路径、Figma
文件或聊天导出，不等于 Agent 已经读取它。

来源登记应包含：

- source ID；
- 文件、Figma page/frame 或 archive pointer；
- 来源类型；
- 所属项目和时间范围；
- 允许检查的范围；
- 处理日期；
- 当前状态：`unknown`、`candidate`、`confirmed`、`historical` 或 `superseded`。

原始来源可以继续留在 Figma、Desktop 或聊天平台；StudyMate 保存的是经过授权、带有
来源指针的 derived knowledge。

### 5. Orientation：先理解，再提升为当前状态

第一次 orientation 要把材料分成几层：

| 状态 | 含义 |
| --- | --- |
| `observed` | Agent 在授权范围内直接看到的内容 |
| `inferred` | 根据多个材料推断出的关系或解释 |
| `candidate` | 可以考虑，但还没有得到 owner 确认的方向 |
| `confirmed` | owner 已确认，可以进入当前工作状态 |
| `unknown` | 目前没有足够材料支持的内容 |
| `superseded` | 曾经有效，但后来被新方向替代的内容 |

Agent 会提出一个 Current State 草案，包括：

- current question；
- current direction；
- current insight / opportunity；
- current working set；
- current prototype 或 draft；
- evidence gaps 和 contradictions；
- 一个具体的 next move。

只有你确认之后，Agent 才能更新项目的 `CURRENT.md`。旧方向进入 decision log 或
iteration log，不会被删除。

### 6. 从证据走向项目成果

StudyMate 使用下面这条可追溯链路：

```text
source
  → note / observation
  → interpretation
  → insight
  → opportunity
  → criteria
  → decision
  → prototype
  → testing
  → iteration
  → outcome
```

Agent 可以帮助你把材料放到正确层级，但 method、summary 或 model-generated prose 不会
自动成为 empirical evidence。每个 claim 都应该保留来源、确认状态和 limitation。

### 7. Figma、聊天和 PDF 的专用入口

```text
帮我整理 Figma 的演变
帮我提出最近版本的 current candidate
整理已经导入的聊天记录
从聊天记录中提取 candidate insights 和 decisions
帮我分析这些 PDF，并建立本地 index
帮我找出这个项目的 evidence gaps
```

Figma current candidate 需要 owner 确认后，才能写入 `CURRENT.md`。聊天整理会保留
原始 archive，并把候选 insight、decision、rejected direction 和 open question 分开。
PDF / image index 是本地 retrieval aid；找到页面之后仍要检查原始材料。

### 8. 原型、测试、写作与输出

```text
帮我把这个 insight 转成 design opportunity
帮我把 opportunity 转成 design criteria
帮我为这个 prototype 写 testing plan
帮我记录这次 testing 的 response、interpretation 和 design decision
帮我把 evidence chain 变成 document outline
帮我检查这段文字的 claim、evidence 和 limitation
帮我整理一个可以交接的 project summary
```

Testing record 要把 participant response、researcher interpretation 和后续 design
decision 分开。没有 testing record 的 prototype 仍然是 representation，而不是
effectiveness evidence。

### 9. GSA Pack

GSA Pack 是一个可选的、linked read-only 的 Design Innovation academic pack。启用时
直接说：

```text
加载 GSA Pack
```

它提供 Semester methods、Provotyping、Reflection Document / guidance-video analysis、
Stage 3 criteria、rubric 和 ILO guidance。项目分析写入项目自己的 Managed Workspace；
Pack 本体保持只读。对于 consequential assessment wording，要核对当前授权的官方 source。

### 10. Dashboard、更新和迁移

```text
Dashboard
Update StudyMate
StudyMate doctor
迁移我的旧 StudyMate profile
```

公共 core 更新前先运行 check mode。Git 更新只改变 StudyMate core，不修改
`projects/local/` 中的项目知识。旧 v0.1 profile 迁移时会建立新的 Managed Workspace，
并保留旧 profile 不变。

### 11. 完成标准

一次 onboarding 完成时，Agent 应该能够展示：

- 一项实际完成的有用工作及其来源／限制，而不只是已建立的目录；
- 本次交接记录与在新对话继续的示例；
- 项目 title、阶段和目标；
- Managed Workspace 路径；
- 已登记的 sources；
- Current State 或待确认的 Current State 草案；
- evidence / decision / iteration 的数量和状态；
- GSA Pack 是否启用；
- 一个有来源支持的 next move；
- 仍然需要人工确认的事项。

模板存在不等于项目已经完成。来源、证据、决定和成果必须保留 provenance、状态和
必要的隐私边界。

---

## English

### First use: complete one useful task

Use [User journey](USER_JOURNEY.md) for the four entries and stage-dependent
choices. Skip menus when the intent is clear. The current example covers
framing/research preparation; later-stage explanations are not empirical simulation.
Follow [Native choices](NATIVE_CHOICES.md) for clickable input when the host
provides a permitted tool, with text fallback. Actual ideas require open input;
default/preselected options do not count as submitted answers.

For `Start StudyMate`, `启动 StudyMate`, uncertain first use or a stated problem,
check available capabilities, then ask what the user wants to accomplish in this
session. Ideas, existing materials and a concrete problem can coexist. Skip a
menu when the user has already explained the task.
Before choosing work, follow [Project flow](PROJECT_FLOW.md) to establish actual
research/analysis progress. Ideas or course-only material begin with framing,
source review and research gaps/planning. Later tasks require their upstream
basis; existing projects join at the supported stage rather than restarting.
For a demonstration, use the labelled synthetic exercise in `examples/first-task/`
without automatically creating a personal workspace.

Offer relevant examples: course brief, assignment requirements, rubric/ILOs,
teaching PPT/PDF, readings, research notes, Figma, prototypes, test records,
drafts and chat exports. Course-page links such as Canvas can be inspected only
with available tools, access and explicitly authorised page/attachment scope.
Follow [Materials intake](MATERIALS_INTAKE.md); no materials or academic Pack are
required to begin from an idea or a labelled synthetic example.

Ask only for missing information. When persistence is needed, propose and confirm
the title, slug and destination together. Complete one bounded task, show its
sources/limits and save a [session handoff](SESSION_HANDOFF.md). A directory and
Current State draft alone do not complete onboarding. Framework maintenance
stays on its own route.

This is the complete operating guide. The README is the quick start; this document explains
how StudyMate can start a project, accompany its full lifecycle, join an already-developed
project, or continue an existing Managed Workspace.

### 1. How StudyMate works

StudyMate is an Agent-native, evidence-led project workflow for Research and Design. It moves
a project from a question and a goal toward an explainable, deliverable and iterable outcome:

```mermaid
flowchart LR
    A[Start a project] --> W[Managed Workspace]
    B[Join an existing project] --> W
    C[Continue a project] --> W
    W --> Q[Question]
    Q --> S[Sources]
    S --> E[Evidence]
    E --> I[Insight & criteria]
    I --> D[Decision]
    D --> P[Prototype]
    P --> T[Testing & iteration]
    T --> O[Outcome]
```

StudyMate can enter at any stage. The Agent first identifies what is present and what is
missing, then proposes the next move; existing material is not automatically treated as
confirmed current state.

### 2. Choose an entry point

#### Start from scratch

For a project with an interest, question, brief or early direction, StudyMate helps establish
the title, slug, working question, intended outcome, uncertainty, source map and evidence plan.

Try:

```text
start a new project
help me set up a service design project
help me establish an evidence-led product design workflow
```

#### Start early and continue through the lifecycle

For a brief or design goal that is still forming, StudyMate builds sources, evidence, insights,
criteria, decisions, prototypes and testing in sequence, keeping uncertainty and the next
verification step visible.

Try:

```text
turn this brief into a working research question
help me make an evidence plan
turn this insight into design criteria
```

#### Join an already-developed project

For a project with Figma, local folders, PDFs, images or ChatGPT exports, StudyMate registers
source pointers first and requests bounded permission before inspection. Raw sources remain in
their original locations.

Try:

```text
adopt this existing project
organise this project into a StudyMate Workspace
help me identify the direction that is currently working
```

#### Continue a running project

For an existing Managed Workspace, StudyMate reads its nested `AGENTS.md`, `CURRENT.md`,
`packs.md` and bounded records before helping update the current state, evidence, decisions,
prototype or next move.

Try:

```text
continue this project
Dashboard
help me find the most important next move
```

### 3. What the first conversation confirms

Confirm what the task needs, rather than running a fixed questionnaire. Do not
repeat information already supplied:

1. the intended result or problem for this session;
2. relevant materials and explicitly authorised inspection scope, if needed;
3. necessary project stage, type, constraints and uncertainty;
4. the proposed title, slug and destination when persistent records are needed;
5. linked GSA Pack only when the user selects it.

Unless an external destination is explicitly chosen, project knowledge is stored at:

```text
projects/local/<slug>/
```

This is a Git-ignored Managed Workspace. The reusable StudyMate core, other projects and raw
sources remain separate.

### 4. Source registration and inspection permission

StudyMate records a source pointer before requesting inspection permission. Registering a path,
Figma file or chat export does not mean the Agent has read it.

Each source record includes an ID, pointer, type, scope, date and status such as `unknown`,
`candidate`, `confirmed`, `historical` or `superseded`. Raw sources may remain in Figma, a
desktop folder or a chat platform; StudyMate stores authorised derived knowledge with provenance.

### 5. Orientation and Current State

Orientation separates `observed`, `inferred`, `candidate`, `confirmed`, `unknown` and
`superseded`. The Agent proposes a Current State containing the current question, direction,
insight/opportunity, working set, prototype or draft, evidence gaps, contradictions and one
next move.

Only the owner confirms promotion into `CURRENT.md`. Older directions remain in decision and
iteration history rather than being deleted.

### 6. From evidence to outcome

```text
source → note / observation → interpretation → insight → opportunity
       → criteria → decision → prototype → testing → iteration → outcome
```

Methods, summaries and model-generated prose do not become empirical evidence automatically.
Claims retain sources, confirmation status and limitations.

### 7. Figma, chat and PDF routes

```text
map the Figma evolution
propose the most recent current candidate
reconcile the imported chat archive
extract candidate insights and decisions from the chat
index these PDFs and create local project knowledge
find the evidence gaps
```

The owner confirms a Figma current candidate before `CURRENT.md` changes. Chat reconciliation
preserves the raw archive and separates candidate insights, decisions, rejected directions and
open questions. A PDF/image index is a local retrieval aid; inspect the original source before
using a located page as evidence.

### 8. Prototypes, testing, writing and outputs

```text
turn this insight into a design opportunity
turn the opportunity into design criteria
write a testing plan for this prototype
record responses, interpretation and the design decision separately
turn the evidence chain into a document outline
check the claims, evidence and limitations in this section
prepare a handover summary for this project
```

Testing records separate participant response, researcher interpretation and later design
decision. A prototype without a testing record is a representation, not effectiveness evidence.

### 9. GSA Pack

The GSA Pack is an optional linked, read-only Design Innovation academic pack. Say:

```text
load GSA Pack
```

It provides Semester methods, Provotyping, Reflection Document / guidance-video analysis,
Stage 3 criteria, rubric and ILO guidance. Project analysis is written to the project's
Managed Workspace and the pack remains read-only. Verify consequential assessment wording
against the current authorised official source.

### 10. Dashboard, updates and migration

```text
Dashboard
Update StudyMate
StudyMate doctor
migrate my old StudyMate profile
```

Run the update check before applying a core update. Git updates change the reusable core and
leave ignored `projects/local/` knowledge untouched. Legacy v0.1 migration creates a new
Managed Workspace and preserves the old profile.

### 11. Completion criteria

At the end of onboarding, complete one useful task and provide a session handoff
with an example continuation prompt, then show the project title, phase and goal, the Managed
Workspace path, registered sources, Current State or pending confirmation, evidence/decision/
iteration counts, GSA Pack status, one source-supported next move and all remaining human
decisions.

Templates are scaffolds, not evidence. Sources, evidence, decisions and outputs retain
provenance, status and appropriate privacy boundaries.
