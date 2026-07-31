---
type: research-source
item_id: 1605
title: "$Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems"
source: "arxiv"
published: "2026-07-30T10:05:50Z"
first_seen: "2026-07-31"
review_status: "pending"
canonical_key: "arxiv:2607.27958"
url: "https://arxiv.org/abs/2607.27958v1"
generated_by: codex-research-db
aliases:
  - "$Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems"
topics:
  - "ai-agents"
---

# $Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2607.27958v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-31|2026-07-31]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`45J3F67I`)
- 발행일: 2026-07-30T10:05:50Z
- 저자: Peilin Feng, Suorong Yang, Soujanya Poria
- 식별자: `arxiv:2607.27958`

## 요약·초록

Memory is central to long-horizon LLM agents, yet existing memory systems primarily preserve interaction content rather than modeling which agents can be trusted and under what conditions. This limitation is particularly important in multi-agent systems, where a central model may be unable to directly verify plausible or correlated peer responses. We introduce $Σ$-Mem, an online reliability memory that records historical competence evidence for individual peers and peer relationship evidence across the peer set. Both forms of evidence are maintained as real symmetric states and updated from post-decision correctness feedback. By Weyl's inequality, the spectral change caused by each event-level update is bounded, enabling stable online adaptation without retraining the underlying models. $Σ$-Mem provides a general write-and-read interface: the same memory can be used for residual steering of a central model, response-free peer routing, or reliability-weighted voting. Across five Qwen-family models, $Σ$-Mem adapts to counterfactual reliability shifts and generalizes to unseen peers and task domains. Direct memory readouts also outperform majority voting and the best fixed peer over the full OOD evaluation set. Moreover, performance improves consistently as more correctness feedback becomes available, indicating that $Σ$-Mem progressively accumulates actionable reliability information. These results establish reliability memory as a reusable foundation for adaptive coordination in LLM-based multi-agent systems.

## 내 메모


