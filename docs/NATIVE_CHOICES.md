# Native choices / 原生点选式引导

Use native question UI when the host exposes a permitted tool for collecting
missing information or a user preference. This is an Agent interaction policy,
not a Python popup, new application or guaranteed capability of every host.

## Capability selection

1. Inspect the tools actually exposed in the current conversation and their
   usage constraints. Do not infer availability from the product's name alone.
2. If `request_user_input_async` is exposed and permitted, use its supported
   question/option schema. For example, this desktop session exposes a tool
   whose questions have `title` and optional `options`.
3. If only `request_user_input` is exposed, obey its current mode restrictions
   and schema. A tool limited to Plan mode must not be called in another mode.
   Do not silently change modes just to display a form.
4. Without a permitted native tool, use a short numbered text question and
   accept a natural-language reply. Explain once that the current environment
   lacks native choices. Do not claim a popup was displayed.

OpenAI's [Codex App Server](https://learn.chatgpt.com/docs/app-server) documents
user-input requests and client responses. Protocol support does not mean every
chat exposes the same model-callable tool. In a custom API application, the
[async input function](https://developers.openai.com/api/docs/guides/async-tool-calling)
and its display/response behaviour belong to that application. Adding a tool name
to README or AGENTS.md cannot create a missing host capability.

## Question design

- Use choices to establish an entry, actual progress or a next-task preference;
  these are orientation questions, not a knowledge exam or a test of the user.
- Ask only for information still missing. Skip the first menu when the user
  already says they want the example or states a clear project task.
- Prefer one short question at a time, with two or three relevant alternatives
  where the tool supports them. Do not copy the entire capability catalogue.
- Four conceptual entry routes need not fit in one form: offer
  "try the example / start my project / bring in or continue existing work", then
  distinguish adoption/continuation only if the user's intent is still unclear.
- Native single-choice questions do not become multi-select checklists. Ideas
  and material types can coexist; do not force "idea OR material". Accept a
  free-text inventory or a supported follow-up question for material combinations.
- Use a permitted free-text question or a brief ordinary message for the user's
  actual idea: who/context, what they hope to understand/change, and what remains
  uncertain. Choices alone do not establish their research question or intent.
- No file-upload prompt belongs in a text-only user-input tool. Explain file
  attachment/export options in the conversation, using the host's supported
  attachment surface. Do not request screenshots via a text-only form.

## Answer lifecycle

An accepted/presented tool request is not a submitted answer. A preselected or
recommended option is not confirmation. For asynchronous tools, continue only
independent work while the answer is pending; use the submitted reply before
following the dependent route. Never treat elapsed time as a choice or consent.

Record an explicit selection as a user preference, not research evidence or
automatic Current State confirmation. Reuse supplied answers rather than asking
the same question again. If a question is dismissed, follow the tool's no-answer
rules; do not invent a selected option. Scope/approval requirements remain intact.

## First-use example

1. Entry, if missing: "你希望从哪里开始？" with example/new/existing choices.
2. For the synthetic exercise: explain its no-research state, then ask whether
   to inspect requirements versus the idea, clarify a research question, or
   prepare an initial investigation. Reuse a clearly chosen task.
3. Complete that task from EX-01/EX-02, label missing empirical support, and
   show the resulting gap plus one stage-appropriate next move.
4. For a real project, ask for its actual idea/goal and relevant actual progress,
   then apply PROJECT_FLOW.md and MATERIALS_INTAKE.md. Do not route to prototype
   development merely because a menu can offer it.

The conversational flow remains in USER_JOURNEY.md. Native UI changes how the
question is answered, not the research process, source boundaries or save rules.
