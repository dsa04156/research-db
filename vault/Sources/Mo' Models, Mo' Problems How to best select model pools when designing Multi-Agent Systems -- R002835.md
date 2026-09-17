---
type: research-source
item_id: 2835
title: "Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems"
source: "arxiv"
published: "2026-09-15T15:17:29Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.17306"
url: "https://arxiv.org/abs/2609.17306v1"
generated_by: codex-research-db
aliases:
  - "Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems"
topics:
  - "ai-agents"
---

# Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2609.17306v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-15T15:17:29Z
- 저자: Sara Vera Marjanović, Jiacheng Xu, Aleksandr Laptev, Grigor Nalbandyan, Erik Arakelyan, Evelina Bakhaturina
- 식별자: `arxiv:2609.17306`

## 요약·초록

Multi-agent Systems (MAS) combine multiple model outputs to solve complex reasoning tasks. However, despite rapid growth of available open-source models, there is limited research on how to select optimal model candidates out of this massive pool. We systematically evaluate 8 model selection strategies (including model size, accuracy and answer diversity) across before-generation (routing) and after-generation (majority-voting, LLM-as-a-judge) MAS architectures on challenging scientific benchmarks. Our findings show a significant gap between theoretical oracle potential and actual performance: Expanding candidate pool sizes often degrades performance below that of the top performing base-model. We find that candidate selection within a single model family is the strategy that yields the best relative performance over a standalone model. These results demonstrate that adding arbitrary models to a heterogeneous MAS can introduce system instability, highlighting model selection as a critical design choice for multi-agent systems.

## 내 메모
