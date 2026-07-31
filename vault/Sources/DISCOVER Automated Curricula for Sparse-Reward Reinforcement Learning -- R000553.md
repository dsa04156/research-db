---
type: research-source
item_id: 553
title: "DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning"
source: "arxiv"
published: "2025-05-26T11:35:07Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.19850"
url: "https://arxiv.org/abs/2505.19850v2"
generated_by: codex-research-db
aliases:
  - "DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning"
topics:
  - "self-evolving-harness"
---

# DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning

[원문 열기](https://arxiv.org/abs/2505.19850v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`F67ET4JP`)
- 발행일: 2025-05-26T11:35:07Z
- 저자: Leander Diaz-Bone, Marco Bagatella, Jonas Hübotter, Andreas Krause
- 식별자: `arxiv:2505.19850`

## 요약·초록

Sparse-reward reinforcement learning (RL) can model a wide range of highly complex tasks. Solving sparse-reward tasks is RL's core premise, requiring efficient exploration coupled with long-horizon credit assignment, and overcoming these challenges is key for building self-improving agents with superhuman ability. Prior work commonly explores with the objective of solving many sparse-reward tasks, making exploration of individual high-dimensional, long-horizon tasks intractable. We argue that solving such challenging tasks requires solving simpler tasks that are relevant to the target task, i.e., whose achieval will teach the agent skills required for solving the target task. We demonstrate that this sense of direction, necessary for effective exploration, can be extracted from existing RL algorithms, without leveraging any prior information. To this end, we propose a method for directed sparse-reward goal-conditioned very long-horizon RL (DISCOVER), which selects exploratory goals in the direction of the target task. We connect DISCOVER to principled exploration in bandits, formally bounding the time until the target task becomes achievable in terms of the agent's initial distance to the target, but independent of the volume of the space of all tasks. We then perform a thorough evaluation in high-dimensional environments. We find that the directed goal selection of DISCOVER solves exploration problems that are beyond the reach of prior state-of-the-art exploration methods in RL.

## 내 메모


