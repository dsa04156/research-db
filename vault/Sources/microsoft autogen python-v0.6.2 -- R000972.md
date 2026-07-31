---
type: research-source
item_id: 972
title: "microsoft/autogen python-v0.6.2"
source: "github-release"
published: "2025-07-01T00:09:01Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:f485b04134b966cec97f7b6232b10a723c1f326f8111cfcbe9b1fa5e38c2c4f8"
url: "https://github.com/microsoft/autogen/releases/tag/python-v0.6.2"
generated_by: codex-research-db
aliases:
  - "microsoft/autogen python-v0.6.2"
topics:
  - "ai-agents"
---

# microsoft/autogen python-v0.6.2

[원문 열기](https://github.com/microsoft/autogen/releases/tag/python-v0.6.2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `github-release`
- 검토 상태: `pending`
- Zotero: created (`ETTF58P6`)
- 발행일: 2025-07-01T00:09:01Z
- 저자: ekzhu
- 식별자: `url:f485b04134b966cec97f7b6232b10a723c1f326f8111cfcbe9b1fa5e38c2c4f8`

## 요약·초록

## What's New ### Streaming Tools This release introduces streaming tools and updates `AgentTool` and `TeamTool` to support `run_json_stream`. The new interface exposes the inner events of tools when calling `run_stream` of agents and teams. `AssistantAgent` is also updated to use `run_json_stream` when the tool supports streaming. So, when using `AgentTool` or `TeamTool` with `AssistantAgent`, you can receive the inner agent's or team's events through the main agent. To create new streaming tools, subclass `autogen_core.tools.BaseStreamTool` and implement `run_stream`. To create new streaming workbench, subclass `autogen_core.tools.StreamWorkbench` and implement `call_tool_stream`. * Introduce streaming tool and support streaming for `AgentTool` and `TeamTool`. by @ekzhu in https://github.com/microsoft/autogen/pull/6712 ### `tool_choice` parameter for `ChatCompletionClient` and subclasses Introduces a new parameter `tool_choice` to the `ChatCompletionClient`s `create` and `create_stream` methods. **This is also the first PR by @copliot-swe-agent!** * Add `tool_choice` parameter to `ChatCompletionClient` `create` and `create_stream` methods by @copilot-swe-agent in https://github.com/microsoft/autogen/pull/6697 ### `AssistantAgent`'s inner tool calling loop Now you can enable `AssistantAgent` with an inner tool calling loop by setting the `max_tool_iterations` parameter through its constructor. The new implementation calls the model and executes tools until (1) the model stops generating tool calls, or (2) `max_tool_iterations` has been reached. This change simplies the usage of `AssistantAgent`. * Feat/tool call loop by @tejas-dharani in https://github.com/microsoft/autogen/pull/6651 ### OpenTelemetry GenAI Traces This releases added new traces `create_agent`, `invoke_agent`, `execute_tool` from the [GenAI Semantic Convention](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/). * OTel GenAI Traces for Agent and Tool by @ekzhu in https://github.com/microsoft/autogen/pull/6653 You can also disable agent runtime traces by setting the environment variable `AUTOGEN_DISABLE_RUNTIME_TRACING=true`. * add env var to disable runtime tracing by @EItanya in https://github.com/microsoft/autogen/pull/6681 ### `output_task_messages` flag for `run` and `run_stream` You can use the new flag to customize whether the input `task` messages get emitted as part of `run_stream` of agents and teams. * Fix output task messages 6150 by @tejas-dharani in https://github.com/microsoft/autogen/pull/6678 ### Mem0 Extension Added Mem0 memory extension so you can use it as memory for AutoGen agents. * Add mem0 Memory Implementation by @alpha-xone in https://github.com/microsoft/autogen/pull/6510 ### Improvement to `GraphFlow` * Add activation group for workflow with multiple cycles by @ZenWayne in https://github.com/microsoft/autogen/pull/6711 ### `uv` update We have removed the `uv` version limit so you can use the latest version to develop AutoGen. * Unpin uv version to use the latest version by @ekzhu in https://github.com/microsoft/autogen/pull/6713 ## Other Python Related Changes * SK KernelFunction from ToolSchemas by @peterychang in https://github.com/microsoft/autogen/pull/6637 * docs: fix shell command with escaped brackets in pip install by @roharon in https://github.com/microsoft/autogen/pull/6464 * Use yaml safe_load instead of load by @ekzhu in https://github.com/microsoft/autogen/pull/6672 * Feature/chromadb embedding functions #6267 by @tejas-dharani in https://github.com/microsoft/autogen/pull/6648 * docs: Memory and RAG: add missing backtick for class reference by @roysha1 in https://github.com/microsoft/autogen/pull/6656 * fix: fix devcontainer issue with AGS by @victordibia in https://github.com/microsoft/autogen/pull/6675 * fix: fix self-loop in workflow by @ZenWayne in https://github.com/microsoft/autogen/pull/6677 * update: openai response api by @bassmang in https://github.com/microsoft/autogen/pull/6622 * fix serialization issue in streamablehttp mcp tools by @victordibia in https://github.com/microsoft/autogen/pull/6721 * Fix completion tokens none issue 6352 by @tejas-dharani in https://github.com/microsoft/autogen/pull/6665 * Fix/broad exception handling #6280 by @tejas-dharani in https://github.com/microsoft/autogen/pull/6647 * fix: enable function_calling for o1-2024-12-17 by @jeongsu-an in https://github.com/microsoft/autogen/pull/6725 * Add support for Gemini 2.5 flash stable by @DavidSchmidt00 in https://github.com/microsoft/autogen/pull/6692 * Feature/agentchat message id field 6317 by @tejas-dharani in https://github.com/microsoft/autogen/pull/6645 * Fix mutable default in ListMemoryConfig by @mohiuddin-khan-shiam in https://github.com/microsoft/autogen/pull/6729 * update version to 0.6.2 by @ekzhu in https://github.com/microsoft/autogen/pull/6734 * Update agentchat documentation with latest changes by @ekzhu in https://github.com/microsoft/autogen/pull/6735 ## New Contributors * @roharon made their first contribution in https://github.com/microsoft/autogen/pull/6464 * @tejas-dharani made their first contribution in https://github.com/microsoft/autogen/pull/6648 * @roysha1 made their first contribution in https://github.com/microsoft/autogen/pull/6656 * @ZenWayne made their first contribution in https://github.com/microsoft/autogen/pull/6677 * @alpha-xone made their first contribution in https://github.com/microsoft/autogen/pull/6510 * @jeongsu-an made their first contribution in https://github.com/microsoft/autogen/pull/6725 * @DavidSchmidt00 made their first contribution in https://github.com/microsoft/autogen/pull/6692 * @mohiuddin-khan-shiam made their first contribution in https://github.com/microsoft/autogen/pull/6729 * @copilot-swe-agent made their first contribution in https://github.com/microsoft/autogen/pull/6697 **Full Changelog**: https://github.com/microsoft/autogen/compare/python-v0.6.1...python-v0.6.2

## 내 메모


