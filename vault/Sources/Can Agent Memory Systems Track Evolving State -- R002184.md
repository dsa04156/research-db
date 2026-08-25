---
type: research-source
item_id: 2184
title: "Can Agent Memory Systems Track Evolving State?"
source: "arxiv"
published: "2026-08-20T05:41:23Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.19652"
url: "https://arxiv.org/abs/2608.19652v1"
generated_by: codex-research-db
aliases:
  - "Can Agent Memory Systems Track Evolving State?"
topics:
  - "ai-agents"
---

# Can Agent Memory Systems Track Evolving State?

[원문 열기](https://arxiv.org/abs/2608.19652v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DFIUBRVP`)
- 발행일: 2026-08-20T05:41:23Z
- 저자: Xinyi Fan, Miri Liu, Ruozhen Yang, Siru Ouyang, Jiawei Han
- 식별자: `arxiv:2608.19652`

## 요약·초록

As LLM-based agents are deployed for longer and higher-stakes tasks, their memory systems continue to have crucial gaps. While existing memory benchmarks focus largely on recall-shaped tasks, we argue an effective memory system must track the evolving state of the world; as facts, constraints, and decisions are revised over a long interaction, answers must reflect the current state and not a superseded one. We define this capability as state tracking and instantiate it in StateMemBench, a benchmark of 234 multi-session scenarios spanning two conversation-length regimes. Its closed-pool grading scores whether an answer reflects the current state, the superseded state, or fails otherwise, separating state-tracking failures from other errors by construction. Our analysis shows that this task is challenging for existing memory systems, retrieval-augmented baselines, and long-context baselines. We then present StateMem, a state-first memory method that explicitly tracks supersession and relational dependencies, and show it improves current-state accuracy over the strongest same-backbone baseline by 1.8x (0.205 -> 0.363) on DeepSeek-V4-Flash and over the strongest memory system by 1.6x (0.149 -> 0.233) on Qwen-3.5-9B, while remaining competitive with the long-context baselines. Finally, we show the same state approach can be applied as a lightweight single-call wrapper over existing memory systems, lifting current-state accuracy by +32 to +67 points on StateMemBench across six memory and retrieval backends. A length- and cost-matched control attributes +15 to +32 of those points to state structure rather than added context.

## 내 메모


