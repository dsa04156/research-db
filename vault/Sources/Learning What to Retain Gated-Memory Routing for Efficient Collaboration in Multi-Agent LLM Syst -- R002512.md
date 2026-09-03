---
type: research-source
item_id: 2512
title: "Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems"
source: "arxiv"
published: "2026-08-31T18:42:57Z"
first_seen: "2026-09-02"
review_status: "pending"
canonical_key: "arxiv:2609.00237"
url: "https://arxiv.org/abs/2609.00237v1"
generated_by: codex-research-db
aliases:
  - "Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems"
topics:
  - "ai-agents"
---

# Learning What to Retain: Gated-Memory Routing for Efficient Collaboration in Multi-Agent LLM Systems

[원문 열기](https://arxiv.org/abs/2609.00237v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-02|2026-09-02]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6FA9QHQM`)
- 발행일: 2026-08-31T18:42:57Z
- 저자: Rakibul Hasan Rajib, Mengxing Zheng, Qian Lou
- 식별자: `arxiv:2609.00237`

## 요약·초록

Large language model (LLM)-based multi-agent systems tackle complex reasoning by orchestrating how multiple agents are configured and how they collaborate. A central challenge is to adapt orchestration to the evolving collaboration state. Routing from the query alone cannot adapt to intermediate progress or errors, which hurts accuracy. Routing from the complete execution history supplies this missing context, but forces later decisions to process every prior step, including redundant or low-utility ones. This creates an execution-history overload that inflates cost. Effective orchestration instead requires a compact state that captures useful progress without accumulating redundant context. We propose Gated-Memory Routing, which conditions each decision on the query and a learned execution memory. A learned Memory Write Gate commits only non-redundant reasoning steps, and a learned Retrieval Gate supplies each agent a compact, relevant subset, so every decision conditions on a clean, informative state. At each step, the system selects the next role and backbone from this memory, while an Adaptive Halting Controller stops execution once the memory contains sufficient evidence for answering. Across five reasoning and code-generation benchmarks, our framework is both effective and efficient: it attains the best average accuracy, exceeding the strongest baseline by 2.44 points, while reducing HumanEval inference cost by 31.9% relative to that baseline. Code is available at https://github.com/rajibrhasan/gated-memory-routing

## 내 메모


