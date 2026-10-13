# User journey / 用户从哪里开始、可以选什么

This describes the current local development flow. Prefer a permitted native
question tool so users can click choices; follow [Native choices](NATIVE_CHOICES.md)
for host capability and answer handling. Otherwise use numbered text options.
These are Agent questions, not a separate application. The user can answer in
their own words when supported. Skip menus when the intent is already clear;
offer only a few relevant actions at once and recommend one with a reason.

## 1. 选择入口 / Entry choices

After `启动 StudyMate / Start StudyMate`, explain the purpose in plain language:
help organise the question, carry out research, connect findings to design and
keep project progress traceable. Then offer these entries when needed:

| 入口 | 用户可以说 | 会发生什么 |
|---|---|---|
| 先体验示例 | 先用示例看看 | 使用随仓库提供的合成 brief 与想法；不用提供私人材料，不自动建项目 |
| 开始自己的新项目 | 我想从一个想法开始 | 理解目标与要求，梳理工作问题和调研缺口 |
| 接入已有项目 | 我已有资料或调研，帮我接上 | 检查获授权的相关范围，判断阶段与前序依据，不强制从零重做 |
| 继续已有项目 | 继续 <项目名>，接着做 <任务> | 绑定项目、读取 CURRENT 与相关交接，继续当前工作 |

"I have material" is not a separate project stage. Ideas, course files,
research material and a specific problem can coexist in every real-project entry.
Framework-maintenance requests stay on their separate route.

## 2. 当前示例模拟 / What the demo actually does

Use `examples/first-task/course-brief.md` as EX-01 and `project-idea.md` as EX-02.
They are synthetic. The scenario is a welcome-card idea for a shared learning
space, with no collected research. The current demo covers framing and research
preparation; it is not a full simulated empirical project.

| 步骤 | Agent 展示或完成什么 | 用户可以选择什么 |
|---|---|---|
| 进入 | 明确合成来源、练习目标与当前无调研的状态 | 跟着做／先看一遍结果／切换到自己的项目 |
| 理解任务 | 读取合成 brief 与想法，区分课程要求、方案假设与未知 | 先看要求与想法的对应（默认）／先澄清工作问题 |
| 判断现状 | 说明当前为 framing / research preparation；卡片仍是假设 | 确认这段理解／纠正理解／查看依据 |
| 第一项成果 | 要求对应表、工作问题草案和研究缺口，按用户所选任务交付 | 修改工作问题／进入最小调研计划／解释某个判断 |
| 调研准备 | 明确需要了解什么、适合的来源/方法、应记录什么与局限 | 调整范围／准备阅读或访谈观察提纲／查看后续流程 |
| 结束或转入真实项目 | 汇总实际完成的演示工作与仍待调研的内容 | 继续准备／把这套方式用于自己的项目／结束体验 |

Do not ask the user to choose prototype development at this starting stage.
Do not create interviews, observations, findings or test results to let the demo
appear to advance. The early sketch is a proposal, not a confirmed solution.

"Show later stages" is a process walkthrough of `PROJECT_FLOW.md`: show the
required inputs, possible work and expected outputs, and explicitly state which
inputs are currently missing. It is not evidence that those stages happened.
If the user wants to work with real material, switch modes explicitly and follow
source-scope rules. Do not silently mix synthetic and real project records.

For real persistence, propose title/slug/destination together and obtain the
required confirmation. A demo alone does not write CURRENT.md or create a private
workspace. A demo recap stays in the conversation unless the user requests saving.

## 3. 进入自己的项目 / Real project intake

Use the user's description to establish the intended result and actual progress.
Only ask for missing information. Material options are combinable:

- course brief, requirements, rubric/ILOs, teaching PPT/PDF or readings;
- the user's idea, draft, constraints or existing handoff;
- authorised literature, interviews, observations or research notes;
- Figma, concepts, prototypes and test records for existing work;
- an explicitly scoped local file/folder or accessible Canvas/LMS page;
- no material yet: begin with framing and identify what to investigate.

Use `MATERIALS_INTAKE.md` for access, roles and provenance. A course page is not
whole-account permission; an upload/reference is not automatically validated
research. A filename or preferred output does not establish the stage.

After bounded orientation, propose the current stage using `PROJECT_FLOW.md`,
show its basis and any missing upstream connection. The owner confirms CURRENT
promotion. Demonstration choice never enables an optional academic Pack.

## 4. 随阶段变化的动作 / Stage-appropriate work

These are examples, not an exhaustive menu to show on every turn:

| Supported stage | Possible choices | Result or limit |
|---|---|---|
| 问题梳理 | 理解 brief／澄清工作问题／找调研缺口 | 工作问题与已知/未知，不能把想法当发现 |
| 调研准备与开展 | 审阅授权文献／制定访谈或观察计划／整理已有研究记录 | 来源笔记、计划或真实记录；Agent 不凭空替用户完成实地调研 |
| 分析与综合 | 区分观察与解释／比较模式与矛盾／补证据缺口 | 带来源的候选洞察与局限 |
| 机会与设计标准 | 提出机会／建立 criteria／核对要求和证据 | 可追溯的机会/标准草案，必要决定由用户确认 |
| 概念探索 | 生成概念／比较方向／确定待验证假设 | 有依据的概念比较与学习问题 |
| 原型与测试 | 定义原型范围／规划测试／分析已有反馈 | 原型或测试工作；缺少测试记录不宣称有效 |
| 迭代与表达 | 记录决定／调整方案／检查项目叙述 | 迭代记录、证据链与仍需验证的 claim |

At any stage, the user can ask to see sources, correct the interpretation, change
the task or inspect earlier decisions. Changing the requested task does not
automatically confirm a new project direction or fill missing evidence.

## 5. 每次工作结束 / End of a session

Show supported stage, actual completed work/output, remaining uncertainty and
one recommended next move. Offer `继续 / 换个任务 / 查看依据 / 结束本次`.
Real projects save an independent handoff using `SESSION_HANDOFF.md`. A new chat
can say `继续 <项目名>，接着做 <任务>`; it reads files rather than assuming shared
conversation memory. Multiple projects require a clear selection.

The route is implemented as Agent guidance and local tools. Actual adherence
across hosts and newcomer success still require observed end-to-end testing.
