---
type: research-source
item_id: 1124
title: "CHMAS: A Coupled Hierarchical Framework for Multi-Agent Reinforcement Learning"
source: "arxiv"
published: "2026-07-21T20:22:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19555"
url: "https://arxiv.org/abs/2607.19555v1"
generated_by: codex-research-db
aliases:
  - "CHMAS: A Coupled Hierarchical Framework for Multi-Agent Reinforcement Learning"
topics:
  - "ai-agents"
---

# CHMAS: A Coupled Hierarchical Framework for Multi-Agent Reinforcement Learning

[원문 열기](https://arxiv.org/abs/2607.19555v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`BPXNNI9J`)
- 발행일: 2026-07-21T20:22:40Z
- 저자: Dongming Wang, Jie Xu, Yanyu Zhang, Wei Ren
- 식별자: `arxiv:2607.19555`

## 요약·초록

Multi-agent reinforcement learning (MARL) systems face fundamental challenges in balancing global coordination with local execution across different temporal scales. This paper introduces the Coupled Hierarchical Multi-Agent System (CHMAS), a novel framework that decomposes multi-agent decision-making into centralized strategic planning and distributed tactical execution with bidirectional information flow. The strategic layer integrates all agents' states with an exclusive global environmental state to generate guidance actions every $T$ timesteps, while tactical agents execute distributed policies augmented by strategic guidance and local neighborhood observations. Unlike existing hierarchical approaches with unidirectional control, CHMAS establishes a feedback mechanism where accumulated tactical rewards influence strategic objectives through a coupling coefficient $λ$, ensuring strategic plans remain grounded in tactical feasibility. To address the non-stationarity inherent in hierarchical learning, we propose an asynchronous update protocol where strategic parameters update every $N_f$ tactical episodes, allowing tactical policies to converge to quasi-stationary points between strategic changes. We present both a general bi-level formulation capturing full system dynamics and a tractable additive approximation enabling rigorous analysis. Theoretical analysis proves that this asynchronous scheme achieves $\mathcal{O}(\log K/\sqrt{K})$ convergence for the strategic layer after $K$ strategic updates under standard assumptions. Experimental validation in a multi-agent foraging domain demonstrates successful learning of spatially partitioned exploration strategies, with both layers converging stably despite hierarchical coupling.

## 내 메모


