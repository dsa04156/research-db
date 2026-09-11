---
type: research-source
item_id: 2753
title: "Graph-Based Safe Reinforcement Learning for Multi-Agent Systems with Time-Varying Topology"
source: "arxiv"
published: "2026-09-08T14:30:06Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.08802"
url: "https://arxiv.org/abs/2609.08802v1"
generated_by: codex-research-db
aliases:
  - "Graph-Based Safe Reinforcement Learning for Multi-Agent Systems with Time-Varying Topology"
topics:
  - "ai-agents"
---

# Graph-Based Safe Reinforcement Learning for Multi-Agent Systems with Time-Varying Topology

[원문 열기](https://arxiv.org/abs/2609.08802v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`V2A87AWD`)
- 발행일: 2026-09-08T14:30:06Z
- 저자: Xiao Sizhe, Dong Lijing, Bai Rui, Tan Xin
- 식별자: `arxiv:2609.08802`

## 요약·초록

This paper presents a graph-based safe multi-agent reinforcement learning (MARL) framework for cooperative navigation with time-varying topology. To address the critical challenge of ensuring safety in environments with sensing constraints, a safety-decoupled mechanism is introduced through a Control Barrier-Like Function (CBLF) action screening layer. This mechanism bridges the gap between discrete LiDAR perception and continuous safety constraints, ensuring that physical safety constraints are strictly satisfied regardless of the learning progress. Building upon this safety foundation, a unified structural architecture is proposed, integrating a attention-based actor and a Graph Attention Network (GAT) centralized critic. The actor utilizes a value vector reconstruction mechanism that explicitly encodes relative geometric relations through a collaborative tracking error matrix, enabling scale-insensitive policy learning under time-varying communication topologies. Meanwhile, the GAT-based critic models evolving interaction structures for accurate global value estimation. The proposed framework is validated on real differential-drive robot platforms, and experimental results demonstrate superior stability and safety in dynamic scenarios with limited fields-of-view.

## 내 메모


