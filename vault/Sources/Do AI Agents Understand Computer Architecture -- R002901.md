---
type: research-source
item_id: 2901
title: "Do AI Agents Understand Computer Architecture?"
source: "arxiv"
published: "2026-09-16T20:10:28Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.19387"
url: "https://arxiv.org/abs/2609.19387v1"
generated_by: codex-research-db
aliases:
  - "Do AI Agents Understand Computer Architecture?"
topics:
  - "ai-agents"
---

# Do AI Agents Understand Computer Architecture?

[원문 열기](https://arxiv.org/abs/2609.19387v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`T23QI7EK`)
- 발행일: 2026-09-16T20:10:28Z
- 저자: Ambika Sharan, Grigory Chirkov, Soheil Abbasloo
- 식별자: `arxiv:2609.19387`

## 요약·초록

Agents are increasingly asked to design hardware, and increasingly reported to succeed. Such reports establish that a design improved; they cannot establish why. An agent that improves an accelerator may be reasoning about the machine, or may be searching competently over knobs whose meaning it never recovers -- and only the first transfers to the next architecture. Existing evaluations cannot tell the two apart, because they vary the agent while holding the framing of the problem fixed. We do the opposite. AutoTuring hands the same agent the same 15-dimensional accelerator space twice: once as named architectural knobs with simulator counters, once as anonymous variables on [0,1], with the evaluator, the legal space and the reachable optima held identical, so that the only thing that varies is whether the problem means anything. The gap between the two is the measurement. On a nine-kernel FP16 GEMM basket, meaning pays: the architect beats a modeled H200 by 5.4% and its blind counterpart by 12.3% on average, with 70.1% fewer simulator calls. It does not pay uniquely: a critic loop recovers most of that gap for the blind agent and buys the architect nothing, so architectural knowledge and structured critique behave as substitutes rather than as complements. We report these as preliminary findings -- five to six runs per condition on a single modeled accelerator -- and take the comparison itself, not the accelerator, to be the contribution.

## 내 메모


