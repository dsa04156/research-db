---
type: research-source
item_id: 1658
title: "openai/openai-agents-python v0.19.2"
source: "github-release"
published: "2026-08-01T01:08:37Z"
first_seen: "2026-08-03"
review_status: "pending"
canonical_key: "url:8f2bc511fc3a0fa6638e1b2adaf318ec9fd2cda94e8bbccf7de2cdc20cde72a7"
url: "https://github.com/openai/openai-agents-python/releases/tag/v0.19.2"
generated_by: codex-research-db
aliases:
  - "openai/openai-agents-python v0.19.2"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# openai/openai-agents-python v0.19.2

[원문 열기](https://github.com/openai/openai-agents-python/releases/tag/v0.19.2)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-03|2026-08-03]]
- 수집 채널: `github-release`
- 검토 상태: `pending`
- Zotero: created (`GVI59C4B`)
- 발행일: 2026-08-01T01:08:37Z
- 저자: seratch
- 식별자: `url:8f2bc511fc3a0fa6638e1b2adaf318ec9fd2cda94e8bbccf7de2cdc20cde72a7`

## 요약·초록

## What's Changed * feat: expose original callable through wrapped by @seratch in https://github.com/openai/openai-agents-python/pull/4038 * fix: report input guardrail results when a tripwire aborts the run by @hsusul in https://github.com/openai/openai-agents-python/pull/4071 * fix: consolidate same-exception re-raises into bare raise across all modules by @AAliKKhan in https://github.com/openai/openai-agents-python/pull/4023 * fix(sandbox): preserve tagged EnvValue subclasses by @seratch in https://github.com/openai/openai-agents-python/pull/4039 * fix(modal): reject ephemeral paths during tar hydration by @LHMQ878 in https://github.com/openai/openai-agents-python/pull/4045 * fix(mcp): redact MCP prompt and resource transport errors by @seratch in https://github.com/openai/openai-agents-python/pull/4067 * fix(mcp): redact URL credentials from SDK errors by @seratch in https://github.com/openai/openai-agents-python/pull/4015 * fix(mcp): redact URL credentials from tracing and tool metadata by @seratch in https://github.com/openai/openai-agents-python/pull/4020 * fix(mcp): redact direct MCP cleanup transport errors by @seratch in https://github.com/openai/openai-agents-python/pull/4078 * fix(mcp): clean failed servers before reconnecting by @jstar0 in https://github.com/openai/openai-agents-python/pull/3939 * fix(mcp): nested MCP cleanup error redaction by @seratch in https://github.com/openai/openai-agents-python/pull/4049 * fix(realtime): preserve raw server event payloads by @GautamSharma99 in https://github.com/openai/openai-agents-python/pull/4062 * fix(memory): count valid SQLAlchemy and MongoDB session items for positive limits by @chinmayv095 in https://github.com/openai/openai-agents-python/pull/4032 * fix(memory): count valid AdvancedSQLiteSession items for positive limits by @chinmayv095 in https://github.com/openai/openai-agents-python/pull/4031 * fix(memory): count valid Redis and Dapr session items for positive limits by @chinmayv095 in https://github.com/openai/openai-agents-python/pull/4033 * fix(memory): enforce closed state in Redis and Dapr sessions by @SawhneySatvik in https://github.com/openai/openai-agents-python/pull/4035 * fix(extensions): keep tool parameters named like schema keywords by @Kaif10 in https://github.com/openai/openai-agents-python/pull/4036 * fix(extensions): close the LiteLLM provider stream on exit by @SawhneySatvik in https://github.com/openai/openai-agents-python/pull/4066 * fix(extensions): preserve completed LiteLLM streams on cleanup failure by @seratch in https://github.com/openai/openai-agents-python/pull/4077 * fix(voice): propagate iterator cancellation by @hsusul in https://github.com/openai/openai-agents-python/pull/4040 * fix(voice): break out of audio dispatch loop when a stream task signals session_ended by @AAliKKhan in https://github.com/openai/openai-agents-python/pull/4044 * fix(voice): block audio dispatcher while idle by @GautamSharma99 in https://github.com/openai/openai-agents-python/pull/4061 * fix(tracing): use monotonic export deadlines by @GautamSharma99 in https://github.com/openai/openai-agents-python/pull/4063 ### Documentation & Other Changes * docs: correct the documented Chat Completions store default by @dfedoryshchev in https://github.com/openai/openai-agents-python/pull/4074 * Release 0.19.2 by @github-actions[bot] in https://github.com/openai/openai-agents-python/pull/4046 ## New Contributors * @chinmayv095 made their first contribution in https://github.com/openai/openai-agents-python/pull/4032 * @jstar0 made their first contribution in https://github.com/openai/openai-agents-python/pull/3939 * @Kaif10 made their first contribution in https://github.com/openai/openai-agents-python/pull/4036 * @SawhneySatvik made their first contribution in https://github.com/openai/openai-agents-python/pull/4035 * @GautamSharma99 made their first contribution in https://github.com/openai/openai-agents-python/pull/4061 * @LHMQ878 made their first contribution in https://github.com/openai/openai-agents-python/pull/4045 * @dfedoryshchev made their first contribution in https://github.com/openai/openai-agents-python/pull/4074 **Full Changelog**: https://github.com/openai/openai-agents-python/compare/v0.19.1...v0.19.2

## 내 메모


