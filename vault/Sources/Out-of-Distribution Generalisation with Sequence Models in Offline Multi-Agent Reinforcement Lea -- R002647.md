---
type: research-source
item_id: 2647
title: "Out-of-Distribution Generalisation with Sequence Models in Offline Multi-Agent Reinforcement Learning"
source: "kurate"
published: "2026-09-03T11:04:23Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.03667"
url: "http://arxiv.org/abs/2609.03667v1"
generated_by: codex-research-db
aliases:
  - "Out-of-Distribution Generalisation with Sequence Models in Offline Multi-Agent Reinforcement Learning"
topics:
  - "ai-agents"
---

# Out-of-Distribution Generalisation with Sequence Models in Offline Multi-Agent Reinforcement Learning

[원문 열기](http://arxiv.org/abs/2609.03667v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- 발행일: 2026-09-03T11:04:23Z
- 저자: Oussama Hidaoui, Omer Ebead, Ulrich Armel Mbou Sob, Siddarth Singh, Juan Claude Formanek, Felix Chalumeau, Omayma Mahjoub, Sasha Abramowitz
- 식별자: `arxiv:2609.03667`

## 요약·초록

Generalising to unseen tasks remains a fundamental challenge in offline multi-agent reinforcement learning (MARL). In this work, we present a principled analysis of zero-shot task generalisation in the offline setting and conduct an extensive empirical investigation into the scaling behaviour governing task diversity, dataset size, and network capacity. To facilitate this study, we extend offline sequence modelling architectures to handle multi-task observation and action spaces alongside variable agent counts across tasks. Our primary finding is that scaling task diversity---rather than sheer dataset size is the dominant factor in achieving robust zero-shot transfer. Through large-scale experiments across four challenging environments (Connector, RWARE, SMAX, and LBF), we demonstrate that our multi-task approach achieves a mean improvement of 3.2x on held-out test tasks compared to single-task models and consistently outperforms strong behaviour cloning baselines. These results suggest that the development of generalisable MARL agents should prioritise the diversity of the training distribution with varying numbers of agents, providing a roadmap for scaling offline MARL effectively.

## 내 메모


