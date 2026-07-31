---
type: research-source
item_id: 996
title: "Context by Distinct Information: An Auditable Dirichlet-Process Working Memory for Long, Redundant Context Streams"
source: "arxiv"
published: "2026-07-11T18:58:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.10441"
url: "https://arxiv.org/abs/2607.10441v1"
generated_by: codex-research-db
aliases:
  - "Context by Distinct Information: An Auditable Dirichlet-Process Working Memory for Long, Redundant Context Streams"
topics:
  - "self-evolving-harness"
---

# Context by Distinct Information: An Auditable Dirichlet-Process Working Memory for Long, Redundant Context Streams

[원문 열기](https://arxiv.org/abs/2607.10441v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`E7X57IUX`)
- 발행일: 2026-07-11T18:58:22Z
- 저자: Siddharth Pal, Viktoria Rojkova
- 식별자: `arxiv:2607.10441`

## 요약·초록

Context engineering decides what information a model carries forward, and current designs meter it in tokens: compressing the past into a bounded recurrent state, keeping a key-value entry for every token, or imposing a fixed budget through a window or eviction rule. All three make the token the unit of memory even when the stream is redundant and the task depends on the distinct information it carries. Building on a companion mechanism paper that opens a cache slot only when an incoming key is novel, so memory scales with the number of distinct items rather than tokens, we develop that allocate-on-novelty cache as a working-memory component and organize context by how a task depends on the past: recall-carried information belongs in a content-addressed novelty cache, summary-carried information in a recurrent state, and locality-carried information in a recency window. The claim is empirical and bounded. On a matched character-level control, novelty-gated attention reaches full-attention performance while attending to about half the tokens, and coupling the cache with a state-space summary matches full-attention coupling at that reduced cost; the advantage grows as context lengthens, while a sliding window is preferable on short, locality-dominated spans. On next-code prediction over synthetic Medicare claims the coupled component leads full attention and every fixed-budget eviction policy at a thousand-event horizon, whereas cost forecasting over the same stream is summary-carried and the cache is neutral. The retained memory is an inspectable table of templates, codes, drugs, or places rather than an opaque state. The experiments are small-scale and use only public data; they establish the primitive that context can scale with distinct information rather than tokens, in a working memory that is content-addressable and auditable.

## 내 메모


