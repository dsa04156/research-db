---
type: research-source
item_id: 253
title: "Intrinsic Action Tendency Consistency for Cooperative Multi-Agent Reinforcement Learning"
source: "arxiv"
published: "2024-06-26T08:06:29Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.18152"
url: "https://arxiv.org/abs/2406.18152v2"
generated_by: codex-research-db
aliases:
  - "Intrinsic Action Tendency Consistency for Cooperative Multi-Agent Reinforcement Learning"
topics:
  - "ai-agents"
---

# Intrinsic Action Tendency Consistency for Cooperative Multi-Agent Reinforcement Learning

[원문 열기](https://arxiv.org/abs/2406.18152v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3IEVZFZR`)
- 발행일: 2024-06-26T08:06:29Z
- 저자: Junkai Zhang, Yifan Zhang, Xi Sheryl Zhang, Yifan Zang, Jian Cheng
- 식별자: `arxiv:2406.18152`

## 요약·초록

Efficient collaboration in the centralized training with decentralized execution (CTDE) paradigm remains a challenge in cooperative multi-agent systems. We identify divergent action tendencies among agents as a significant obstacle to CTDE's training efficiency, requiring a large number of training samples to achieve a unified consensus on agents' policies. This divergence stems from the lack of adequate team consensus-related guidance signals during credit assignments in CTDE. To address this, we propose Intrinsic Action Tendency Consistency, a novel approach for cooperative multi-agent reinforcement learning. It integrates intrinsic rewards, obtained through an action model, into a reward-additive CTDE (RA-CTDE) framework. We formulate an action model that enables surrounding agents to predict the central agent's action tendency. Leveraging these predictions, we compute a cooperative intrinsic reward that encourages agents to match their actions with their neighbors' predictions. We establish the equivalence between RA-CTDE and CTDE through theoretical analyses, demonstrating that CTDE's training process can be achieved using agents' individual targets. Building on this insight, we introduce a novel method to combine intrinsic rewards and CTDE. Extensive experiments on challenging tasks in SMAC and GRF benchmarks showcase the improved performance of our method.

## 내 메모


