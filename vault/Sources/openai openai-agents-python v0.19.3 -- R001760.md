---
type: research-source
item_id: 1760
title: "openai/openai-agents-python v0.19.3"
source: "github-release"
published: "2026-08-04T07:17:48Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "url:cc94fc94ac6773becd3831ab566c890cdd9d3307ab3ec2514b8c4819851aafdf"
url: "https://github.com/openai/openai-agents-python/releases/tag/v0.19.3"
generated_by: codex-research-db
aliases:
  - "openai/openai-agents-python v0.19.3"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# openai/openai-agents-python v0.19.3

[원문 열기](https://github.com/openai/openai-agents-python/releases/tag/v0.19.3)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `github-release`
- 검토 상태: `pending`
- Zotero: created (`WNWBR7I7`)
- 발행일: 2026-08-04T07:17:48Z
- 저자: seratch
- 식별자: `url:cc94fc94ac6773becd3831ab566c890cdd9d3307ab3ec2514b8c4819851aafdf`

## 요약·초록

## What's Changed * fix: resolve agent tool name collisions consistently by @seratch in https://github.com/openai/openai-agents-python/pull/4137 * fix: reconcile resumed tool name collisions by @seratch in https://github.com/openai/openai-agents-python/pull/4145 * fix: persist the max-turns handler output to the session by @LeSingh1 in https://github.com/openai/openai-agents-python/pull/4160 * fix: report output guardrail results when a tripwire aborts the run by @Kaif10 in https://github.com/openai/openai-agents-python/pull/4090 * fix: replace closed default loop in run_sync by @hsusul in https://github.com/openai/openai-agents-python/pull/4102 * fix: honor falsey custom output extractors for agents as tools by @n33levo in https://github.com/openai/openai-agents-python/pull/4088 * fix: report tool guardrail results for streamed runs by @hsusul in https://github.com/openai/openai-agents-python/pull/4097 * fix: preserve approved tool output on streamed resume by @seratch in https://github.com/openai/openai-agents-python/pull/4126 * fix: normalize typeless strict object schemas by @seratch in https://github.com/openai/openai-agents-python/pull/4139 * fix: synchronize after-turn cancellation with event consumption by @seratch in https://github.com/openai/openai-agents-python/pull/4130 * fix: keep input item order when collapsing duplicates by @hsusul in https://github.com/openai/openai-agents-python/pull/4140 * fix: stop emitting handoff calls as streamed tool_called events by @hsusul in https://github.com/openai/openai-agents-python/pull/4146 * fix: preserve tool call and output order when deduplicating inputs by @seratch in https://github.com/openai/openai-agents-python/pull/4147 * fix: honor falsey handoff input filters by @omidsaffari in https://github.com/openai/openai-agents-python/pull/4153 * fix: define explicit zero-value contracts by @seratch in https://github.com/openai/openai-agents-python/pull/4101 * fix: keep committed tool session records when a streamed output guardrail trips by @LHMQ878 in https://github.com/openai/openai-agents-python/pull/4148 * fix(mcp): auto-paginate tool and prompt listings by @seratch in https://github.com/openai/openai-agents-python/pull/4094 * fix(chatcmpl): clear pending thinking blocks when flushing an assistant message by @Kaif10 in https://github.com/openai/openai-agents-python/pull/4089 * fix(sandbox): remove apply_patch move source as the bound user by @hsusul in https://github.com/openai/openai-agents-python/pull/4100 * fix(sandbox): harden default snapshot path resolution by @seratch in https://github.com/openai/openai-agents-python/pull/4141 * fix(sessions): enforce closed state in AsyncSQLiteSession by @chinmayv095 in https://github.com/openai/openai-agents-python/pull/4109 * fix(sessions): avoid creating remote conversation on uninitialized clear_session by @hsusul in https://github.com/openai/openai-agents-python/pull/4111 * fix(sessions): roll back a failed SQLiteSession insert by @LeSingh1 in https://github.com/openai/openai-agents-python/pull/4163 * fix(realtime): apply output guardrails to text deltas by @seratch in https://github.com/openai/openai-agents-python/pull/4124 * fix(realtime): clamp interrupt truncation to received audio by @hsusul in https://github.com/openai/openai-agents-python/pull/4122 * fix(realtime): scope delayed audio guardrail interruption by @seratch in https://github.com/openai/openai-agents-python/pull/4135 * fix(voice): clean up tasks when streams close early by @seratch in https://github.com/openai/openai-agents-python/pull/4131 * fix(voice): finish STT event handling after listener errors by @seratch in https://github.com/openai/openai-agents-python/pull/4170 * fix(tracing): name streamed task spans after the run's own workflow by @LeSingh1 in https://github.com/openai/openai-agents-python/pull/4167 * fix(extensions): keep trimmer's definition names and instance data in trimmed schemas by @LHMQ878 in https://github.com/openai/openai-agents-python/pull/4110 * fix(extensions): release AnyLLM provider streams and preserve completed runs by @hsusul in https://github.com/openai/openai-agents-python/pull/4133 * fix(extensions): send AnyLLM Responses reasoning as a mapping by @hsusul in https://github.com/openai/openai-agents-python/pull/4138 * fix(extensions): record model-call failures on the provider's own span by @PranavMishra28 in https://github.com/openai/openai-agents-python/pull/4143 * fix(extensions): let an in-flight provider stream close finish after cancellation by @LHMQ878 in https://github.com/openai/openai-agents-python/pull/4156 * fix(extensions): preserve thinking blocks for replay by @seratch in https://github.com/openai/openai-agents-python/pull/4157 ### Documentation & Other Changes * docs: fix spelling in GPT-5 example by @wesleyzhangwq in https://github.com/openai/openai-agents-python/pull/4168 * chore(deps): bump actions/checkout from 7.0.0 to 7.0.1 by @dependabot[bot] in https://github.com/openai/openai-agents-python/pull/4080 * chore(deps): bump pypa/gh-action-pypi-publish from 1.14.0 to 1.14.2 by @dependabot[bot] in https://github.com/openai/openai-agents-python/pull/4081 * chore(deps): bump actions/setup-python from 6.3.0 to 7.0.0 by @dependabot[bot] in https://github.com/openai/openai-agents-python/pull/4083 * chore(deps): bump actions/stale from 10.3.0 to 11.0.0 by @dependabot[bot] in https://github.com/openai/openai-agents-python/pull/4084 * chore(ci): preserve cache pruning with setup-uv v9 by @seratch in https://github.com/openai/openai-agents-python/pull/4103 * test: stabilize tracing atexit timeout coverage by @seratch in https://github.com/openai/openai-agents-python/pull/4104 * Release 0.19.3 by @github-actions[bot] in https://github.com/openai/openai-agents-python/pull/4169 ## New Contributors * @n33levo made their first contribution in https://github.com/openai/openai-agents-python/pull/4088 * @omidsaffari made their first contribution in https://github.com/openai/openai-agents-python/pull/4153 * @PranavMishra28 made their first contribution in https://github.com/openai/openai-agents-python/pull/4143 * @wesleyzhangwq made their first contribution in https://github.com/openai/openai-agents-python/pull/4168 **Full Changelog**: https://github.com/openai/openai-agents-python/compare/v0.19.2...v0.19.3

## 내 메모


