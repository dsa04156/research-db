---
type: research-source
item_id: 975
title: "microsoft/autogen python-v0.5.7"
source: "github-release"
published: "2025-05-14T05:02:29Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:89111206aed0752cd0009a7f1d002418fcb8c31e174e63395e2ea779ea18c69e"
url: "https://github.com/microsoft/autogen/releases/tag/python-v0.5.7"
generated_by: codex-research-db
aliases:
  - "microsoft/autogen python-v0.5.7"
topics:
  - "ai-agents"
---

# microsoft/autogen python-v0.5.7

[원문 열기](https://github.com/microsoft/autogen/releases/tag/python-v0.5.7)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `github-release`
- 검토 상태: `pending`
- Zotero: created (`3X249Z85`)
- 발행일: 2025-05-14T05:02:29Z
- 저자: ekzhu
- 식별자: `url:89111206aed0752cd0009a7f1d002418fcb8c31e174e63395e2ea779ea18c69e`

## 요약·초록

## What's New ### `AzureAISearchTool` Improvements The Azure AI Search Tool API now features unified methods: - `create_full_text_search()` (supporting `"simple"`, `"full"`, and `"semantic"` query types) - `create_vector_search()` and - `create_hybrid_search()` We also added support for client-side embeddings, while defaults to service embeddings when client embeddings aren't provided. **If you have been using `create_keyword_search()`, update your code to use `create_full_text_search()` with `"simple"` query type.** * Simplify Azure Ai Search Tool by @jay-thakur in https://github.com/microsoft/autogen/pull/6511 ### `SelectorGroupChat` Improvements To support long context for the model-based selector in `SelectorGroupChat`, you can pass in a model context object through the new `model_context` parameter to customize the messages sent to the model client when selecting the next speaker. * Add `model_context` to `SelectorGroupChat` for enhanced speaker selection by @Ethan0456 in https://github.com/microsoft/autogen/pull/6330 ### OTEL Tracing Improvements We added new metadata and message content fields to the OTEL traces emitted by the `SingleThreadedAgentRuntime`. * improve Otel tracing by @peterychang in https://github.com/microsoft/autogen/pull/6499 ### Agent Runtime Improvements * Add ability to register Agent instances by @peterychang in https://github.com/microsoft/autogen/pull/6131 ## Other Python Related Changes * Update website 0.5.6 by @ekzhu in https://github.com/microsoft/autogen/pull/6454 * Sample for integrating Core API with chainlit by @DavidYu00 in https://github.com/microsoft/autogen/pull/6422 * Fix Gitty prompt message by @emmanuel-ferdman in https://github.com/microsoft/autogen/pull/6473 * Fix: Move the createTeam function by @xionnon in https://github.com/microsoft/autogen/pull/6487 * Update docs.yml by @victordibia in https://github.com/microsoft/autogen/pull/6493 * Add gpt 4o search by @victordibia in https://github.com/microsoft/autogen/pull/6492 * Fix header icons focus and hover style for better accessibility by @AndreaTang123 in https://github.com/microsoft/autogen/pull/6409 * improve Otel tracing by @peterychang in https://github.com/microsoft/autogen/pull/6499 * Fix AnthropicBedrockChatCompletionClient import error by @victordibia in https://github.com/microsoft/autogen/pull/6489 * fix/mcp_session_auto_close_when_Mcpworkbench_deleted by @SongChiYoung in https://github.com/microsoft/autogen/pull/6497 * fixes the issues where exceptions from MCP server tools aren't serial… by @peterj in https://github.com/microsoft/autogen/pull/6482 * Update version 0.5.7 by @ekzhu in https://github.com/microsoft/autogen/pull/6518 * FIX/mistral could not recive name field by @SongChiYoung in https://github.com/microsoft/autogen/pull/6503 ## New Contributors * @emmanuel-ferdman made their first contribution in https://github.com/microsoft/autogen/pull/6473 **Full Changelog**: https://github.com/microsoft/autogen/compare/python-v0.5.6...python-v0.5.7

## 내 메모


