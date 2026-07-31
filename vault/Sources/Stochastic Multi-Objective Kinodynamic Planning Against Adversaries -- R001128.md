---
type: research-source
item_id: 1128
title: "Stochastic Multi-Objective Kinodynamic Planning Against Adversaries"
source: "arxiv"
published: "2026-07-21T16:56:34Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19284"
url: "https://arxiv.org/abs/2607.19284v1"
generated_by: codex-research-db
aliases:
  - "Stochastic Multi-Objective Kinodynamic Planning Against Adversaries"
topics:
  - "ai-agents"
---

# Stochastic Multi-Objective Kinodynamic Planning Against Adversaries

[원문 열기](https://arxiv.org/abs/2607.19284v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`VISG5A38`)
- 발행일: 2026-07-21T16:56:34Z
- 저자: Thomas Marshall Vielmetti, Daniel Cherenson, Dimitra Panagou
- 식별자: `arxiv:2607.19284`

## 요약·초록

This paper addresses multi-objective kinodynamic planning in environments with stochastic hybrid adversaries that probabilistically transition to adversarial modes based on the ego state. The goal is to construct the Pareto-front of paths that trade off execution cost and the probability of safety constraint violation (risk). Existing chance-constrained planners evaluate risk over open-loop trajectories, yielding overly conservative solutions that fail to account for ego-agent reactivity. To address this limitation, we shift the planning space to sequences of closed-loop policies, and integrate sample-based risk evaluation directly into tree construction via Monte-Carlo particle rollouts. We first introduce Stochastic Multi-Objective RRT (SMO-RRT), for which we prove probabilistic completeness, followed by Stochastic Multi-Objective Stable Sparse RRT (SMO-SST), which leverages selective pruning to improve numerical performance at the cost of completeness. For both algorithms, we derive a finite-sample bound on the probability of chance constraint violation for systems with non-Gaussian, state-dependent uncertainty, enabling probabilistically safe planning in a broad class of environments applicable to multi-agent systems, social navigation, and autonomous driving.

## 내 메모


