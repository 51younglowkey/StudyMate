# Materials intake / 材料入口

Use this route when the user brings course or project material. It is part of
the generic StudyMate core; no academic Pack is required. Respond in the user's
language, choose one useful starting source and avoid demanding a complete archive.

## 告诉用户可以提供什么 / Offer concrete examples

用户可以同时有想法、已有资料和具体需求。先问这次想推进什么，再举相关材料的例子：

| 可以提供 / Material | 用途 / Role |
|---|---|
| 课程 brief、作业要求、rubric、ILOs | 明确任务、交付要求与评价标准 / requirements and criteria |
| 教学 PPT/PDF、讲义、方法说明 | 理解背景、概念与可用方法 / context and methodological guidance |
| 阅读材料、论文、参考作品 | 支持文献与先例分析 / literature and precedents |
| 自己的想法、需求、brief、当前草稿 | 明确目标、限制与待解决问题 / user intent and working proposals |
| 访谈、观察、研究笔记 | 经核验与授权的研究证据 / research observations and evidence |
| Figma、原型、测试记录、presentation | 判断当前设计、测试与表达缺口 / design, testing and communication |
| AI 聊天导出、project handoff | 接续历史；模型文字先作为 candidate / history, not automatic evidence |
| Canvas 等 LMS 的课程页面链接 | 在授权与访问能力范围内定位相关要求或教学内容 / bounded course-page inspection |

按宿主能力，用户可以上传文件、粘贴相关段落、指定本地文件，或提供课程页面链接。
不要要求他先把所有课程内容搬入仓库。只选能解决当前问题的一两份材料。
图片、扫描件或 PPT 如果当前工具不能可靠读取，说明缺失范围，并提供 PDF 导出、
相关页截图或粘贴文本的替代方式；未读到的页不能算已检查。

## 来源与授权 / Source scope

1. Bind a selected Managed Workspace before saving derived project knowledge.
2. Record a source pointer in `sources/source_registry.md`; a pointer alone is
   not inspection permission. Explicitly supplied text or an instruction to
   analyse an attached/named file can authorise that specific scope; honour it
   without asking the same question again.
3. For a URL, confirm which course/page/module and whether named linked files
   are included unless the user has already explicitly specified that scope.
   Use a connected tool or browser only when available; a URL does not grant
   access to an entire account, all modules, submissions, people or messages.
4. For a login wall, let the user complete normal authentication in the chosen
   product. Do not request passwords or bypass access controls. If access is
   unavailable, ask for the relevant export, attachment or pasted text.
5. Inspect the smallest useful scope. Do not follow unrelated links or bulk
   download a course. Stop and explain incomplete access or extraction.
6. Keep raw teaching files at their controlled source. A bounded local copy
   requires the user's explicit request and a private destination. Never put
   course originals or personal project knowledge into the public core.

No built-in Canvas crawler is implied. This route orchestrates the host Agent's
available browser/connector/file capabilities. The pointer-registration tools
do not fetch URLs or import file contents.

## 课程内容如何影响项目 / Apply course context

Before choosing what to do with the material, follow [Project flow](PROJECT_FLOW.md).
Course/reference material plus an idea normally supports framing and research
planning; it does not establish completed research, synthesis or a concept basis.

Separate three layers when translating material into a useful task:

- **Requirements:** what the authorised course source asks for, with exact
  source location and wording when quoted. A requirement is evidence about the
  assignment, not evidence that a participant need or design impact is real.
- **Teaching context:** concepts and methods the course introduces, their use
  and limits. A taught method is analytical machinery, not an empirical finding.
- **Project intent and evidence:** what the user wants to achieve, their
  current proposal, observations, tests and unsupported assumptions.

Build a small requirements-to-work map, rather than replacing the user's aim:

| Requirement + locator | User's intended outcome | Current support / work | Gap or proposed action | Status |
|---|---|---|---|---|
| [SOURCE TO VERIFY] | [DECISION PENDING] | [EVIDENCE NEEDED] | [DECISION PENDING] | candidate |

If a course criterion conflicts with the user's goal, or two requirements
disagree, show both sources and ask for a decision. Do not silently choose.
Verify the applicable course/cohort and source version; do not invent a date or
use a generic Pack in place of the user's current requirement. GSA Pack stays
disabled unless explicitly selected.

## 保存什么 / Derived record

For each bounded extraction, record source ID, URL/file and page/slide/section,
inspected scope, retrieval/extraction date, role, limitations and status. Optional
notes can live under `sources/course-context/<source-id>.md`, created only when
needed. A slide/page locator must be verified; otherwise use `[SOURCE TO VERIFY]`.
Record explicitly granted source scope in the private registry or source note,
without credentials. Derived notes preserve the distinction between quotation,
paraphrase and interpretation.

End with one useful result for the user's task: for example, a requirements
map and the most relevant gap, a working question, a direction comparison or a
test plan, selected for the supported stage. New projects default to source
review, a research question/gap and research planning; later outputs require
upstream support. Propose Current State separately and obtain owner confirmation before
promotion. Calendar/deadline administration remains outside this edition.
