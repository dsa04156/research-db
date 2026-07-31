---
type: research-source
item_id: 258
title: "Decentralized Transformers with Centralized Aggregation are Sample-Efficient Multi-Agent World Models"
source: "arxiv"
published: "2024-06-22T12:40:03Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.15836"
url: "https://arxiv.org/abs/2406.15836v2"
generated_by: codex-research-db
aliases:
  - "Decentralized Transformers with Centralized Aggregation are Sample-Efficient Multi-Agent World Models"
topics:
  - "ai-agents"
---

# Decentralized Transformers with Centralized Aggregation are Sample-Efficient Multi-Agent World Models

[원문 열기](https://arxiv.org/abs/2406.15836v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`T8ZTQNUH`)
- 발행일: 2024-06-22T12:40:03Z
- 저자: Yang Zhang, Chenjia Bai, Bin Zhao, Junchi Yan, Xiu Li, Xuelong Li
- 식별자: `arxiv:2406.15836`

## 요약·초록

Learning a world model for model-free Reinforcement Learning (RL) agents can significantly improve the sample efficiency by learning policies in imagination. However, building a world model for Multi-Agent RL (MARL) can be particularly challenging due to the scalability issue in a centralized architecture arising from a large number of agents, and also the non-stationarity issue in a decentralized architecture stemming from the inter-dependency among agents. To address both challenges, we propose a novel world model for MARL that learns decentralized local dynamics for scalability, combined with a centralized representation aggregation from all agents. We cast the dynamics learning as an auto-regressive sequence modeling problem over discrete tokens by leveraging the expressive Transformer architecture, in order to model complex local dynamics across different agents and provide accurate and consistent long-term imaginations. As the first pioneering Transformer-based world model for multi-agent systems, we introduce a Perceiver Transformer as an effective solution to enable centralized representation aggregation within this context. Results on Starcraft Multi-Agent Challenge (SMAC) show that it outperforms strong model-free approaches and existing model-based methods in both sample efficiency and overall performance.

## 내 메모


