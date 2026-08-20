---
type: research-source
item_id: 2094
title: "What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics"
source: "arxiv"
published: "2026-08-17T10:21:36Z"
first_seen: "2026-08-19"
review_status: "pending"
canonical_key: "arxiv:2608.16370"
url: "https://arxiv.org/abs/2608.16370v1"
generated_by: codex-research-db
aliases:
  - "What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics"
topics:
  - "ai-agents"
---

# What Does Context Compression Cost an Agent? Interaction Costs Unrevealed by Task-Completion Metrics

[원문 열기](https://arxiv.org/abs/2608.16370v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-19|2026-08-19]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NT2NGDJI`)
- 발행일: 2026-08-17T10:21:36Z
- 저자: Shuyu Liu
- 식별자: `arxiv:2608.16370`

## 요약·초록

Task completion is the standard metric for evaluating context compression, yet it is incomplete: compression can increase an agent's interaction cost by forcing it to reacquire dropped state while leaving completion statistically unchanged. We introduce a controlled runtime measurement protocol for reacquisition cost in a bounded-horizon tool-using agent. The agent acts in a deterministic planning environment under a fixed 24-turn horizon. We vary compression severity, compare a dropping operator with a fact-preserving operator, restore dropped state through controlled oracle interventions, and decompose tool calls into retrieval and execution. We evaluate three models across two task regimes. Retrieval calls increase in all six model-regime comparisons and account for almost all added interaction; five of six remain significant after Holm correction. At the prespecified 5x comparison point, completion changes are not significant in any cell. DeepSeek shows a significant completion drop only at 10x compression. GPT-5.5 is the clearest case: completion changes from 80% to 85% (p = 1.0) while retrieval increases from 21.0 to 63.9 calls (p = .002). Retention interventions further separate state quantity, state type, and content validity. Random selection is comparable to an offline hindsight oracle, while replacing retained D-state with semantically irrelevant content increases retrieval by 57% (p < .001) without a significant completion change. In a second environment, ALFWorld, sliding compression produces no retrieval surge, showing that the reacquisition signature is environment-dependent rather than intrinsic to shortening context. Overall, compression can impose hidden interaction costs when execution-relevant state becomes absent and must be reacquired, while completion alone may not expose those costs.

## 내 메모


