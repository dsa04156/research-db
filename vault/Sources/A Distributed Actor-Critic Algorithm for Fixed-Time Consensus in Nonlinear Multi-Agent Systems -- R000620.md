---
type: research-source
item_id: 620
title: "A Distributed Actor-Critic Algorithm for Fixed-Time Consensus in Nonlinear Multi-Agent Systems"
source: "arxiv"
published: "2025-07-22T12:30:06Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.16520"
url: "https://arxiv.org/abs/2507.16520v1"
generated_by: codex-research-db
aliases:
  - "A Distributed Actor-Critic Algorithm for Fixed-Time Consensus in Nonlinear Multi-Agent Systems"
topics:
  - "ai-agents"
---

# A Distributed Actor-Critic Algorithm for Fixed-Time Consensus in Nonlinear Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2507.16520v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8NK2NWFP`)
- 발행일: 2025-07-22T12:30:06Z
- 저자: Aria Delshad, Maryam Babazadeh
- 식별자: `arxiv:2507.16520`

## 요약·초록

This paper proposes a reinforcement learning (RL)-based backstepping control strategy to achieve fixed time consensus in nonlinear multi-agent systems with strict feedback dynamics. Agents exchange only output information with their neighbors over a directed communication graph, without requiring full state measurements or symmetric communication. Achieving fixed time consensus, where convergence occurs within a pre-specified time bound that is independent of initial conditions is faced with significant challenges due to the presence of unknown nonlinearities, inter-agent couplings, and external disturbances. This work addresses these challenges by integrating actor critic reinforcement learning with a novel fixed time adaptation mechanism. Each agent employs an actor critic architecture supported by two estimator networks designed to handle system uncertainties and unknown perturbations. The adaptation laws are developed to ensure that all agents track the leader within a fixed time regardless of their initial conditions. The consensus and tracking errors are guaranteed to converge to a small neighborhood of the origin, with the convergence radius adjustable through control parameters. Simulation results demonstrate the effectiveness of the proposed approach and highlight its advantages over state-of-the-art methods in terms of convergence speed and robustness.

## 내 메모


