---
type: research-source
item_id: 971
title: "microsoft/autogen python-v0.6.4"
source: "github-release"
published: "2025-07-09T17:52:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:15abae17aed9f8cf01c4bb6ccb1234bfdba7df969d6a17b568ad7a414340694f"
url: "https://github.com/microsoft/autogen/releases/tag/python-v0.6.4"
generated_by: codex-research-db
aliases:
  - "microsoft/autogen python-v0.6.4"
topics:
  - "ai-agents"
---

# microsoft/autogen python-v0.6.4

[원문 열기](https://github.com/microsoft/autogen/releases/tag/python-v0.6.4)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `github-release`
- 검토 상태: `pending`
- Zotero: created (`TGIW5JEV`)
- 발행일: 2025-07-09T17:52:40Z
- 저자: ekzhu
- 식별자: `url:15abae17aed9f8cf01c4bb6ccb1234bfdba7df969d6a17b568ad7a414340694f`

## 요약·초록

# What's New More helps from @copilot-swe-agent for this release. ### Improvements to `GraphFlow` Now it behaves the same way as `RoundRobinGroupChat`, `SelectorGroupChat` and others after termination condition hits -- it retains its execution state and can be resumed with a new task or empty task. Only when the graph finishes execution i.e., no more next available agent to choose from, the execution state will be reset. Also, the inner StopAgent has been removed and there will be no last message coming from the StopAgent. Instead, the `stop_reason` field in the `TaskResult` will carry the stop message. - Fix GraphFlow to support multiple task execution without explicit reset by @copilot-swe-agent in https://github.com/microsoft/autogen/pull/6747 - Fix GraphFlowManager termination to prevent \_StopAgent from polluting conversation context by @copilot-swe-agent in https://github.com/microsoft/autogen/pull/6752 ### Improvements to `Workbench` implementations `McpWorkbench` and `StaticWorkbench` now supports overriding tool names and descriptions. This allows client-side optimization of the server-side tools, for better adaptability. - Add tool name and description override functionality to Workbench implementations by @copilot-swe-agent in https://github.com/microsoft/autogen/pull/6690 ## All Changes * Update documentation version by @ekzhu in https://github.com/microsoft/autogen/pull/6737 * Fix function calling support for Llama3.3 by @Z1m4-blu3 in https://github.com/microsoft/autogen/pull/6750 * Fix GraphFlow to support multiple task execution without explicit reset by @copilot-swe-agent in https://github.com/microsoft/autogen/pull/6747 * Fix GraphFlowManager termination to prevent _StopAgent from polluting conversation context by @copilot-swe-agent in https://github.com/microsoft/autogen/pull/6752 * Add tool name and description override functionality to Workbench implementations by @copilot-swe-agent in https://github.com/microsoft/autogen/pull/6690 * Added DuckDuckGo Search Tool and Agent in AutoGen Extensions by @varadsrivastava in https://github.com/microsoft/autogen/pull/6682 * Add script to automatically generate API documentation by @ekzhu in https://github.com/microsoft/autogen/pull/6755 * Move `docs` from `python/packages/autogen-core` to `python/docs` by @ekzhu in https://github.com/microsoft/autogen/pull/6757 * Add reflection for claude model in AssistantAgent by @ekzhu in https://github.com/microsoft/autogen/pull/6763 * Add autogen-ext-yepcode project to community projects by @marcos-muino-garcia in https://github.com/microsoft/autogen/pull/6764 * Update GitHub Models url to the new url by @sgoedecke in https://github.com/microsoft/autogen/pull/6759 * SingleThreadedAgentRuntime to use subclass check for factory_wrapper instead of equality by @ZenWayne in https://github.com/microsoft/autogen/pull/6731 * feat: add qwen2.5vl support by @rfsousa in https://github.com/microsoft/autogen/pull/6650 * Remove otel semcov package from core dependencies by @ekzhu in https://github.com/microsoft/autogen/pull/6775 * Update tracing doc by @ekzhu in https://github.com/microsoft/autogen/pull/6776 * Update version to 0.6.3 by @ekzhu in https://github.com/microsoft/autogen/pull/6781 * Update website to 0.6.3 by @ekzhu in https://github.com/microsoft/autogen/pull/6782 * Remove duckduckgo search tools and agents by @ekzhu in https://github.com/microsoft/autogen/pull/6783 * Update to version 0.6.4 by @ekzhu in https://github.com/microsoft/autogen/pull/6784 ## New Contributors * @Z1m4-blu3 made their first contribution in https://github.com/microsoft/autogen/pull/6750 * @varadsrivastava made their first contribution in https://github.com/microsoft/autogen/pull/6682 * @marcos-muino-garcia made their first contribution in https://github.com/microsoft/autogen/pull/6764 * @sgoedecke made their first contribution in https://github.com/microsoft/autogen/pull/6759 * @rfsousa made their first contribution in https://github.com/microsoft/autogen/pull/6650 **Full Changelog**: https://github.com/microsoft/autogen/compare/python-v0.6.2...python-v0.6.4

## 내 메모


