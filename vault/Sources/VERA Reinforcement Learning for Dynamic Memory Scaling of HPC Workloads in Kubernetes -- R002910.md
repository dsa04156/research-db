---
type: research-source
item_id: 2910
title: "VERA: Reinforcement Learning for Dynamic Memory Scaling of HPC Workloads in Kubernetes"
source: "arxiv"
published: "2026-09-17T09:10:15Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.19936"
url: "https://arxiv.org/abs/2609.19936v1"
generated_by: codex-research-db
aliases:
  - "VERA: Reinforcement Learning for Dynamic Memory Scaling of HPC Workloads in Kubernetes"
topics:
  - "kubernetes"
---

# VERA: Reinforcement Learning for Dynamic Memory Scaling of HPC Workloads in Kubernetes

[원문 열기](https://arxiv.org/abs/2609.19936v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`43S6JVAD`)
- 발행일: 2026-09-17T09:10:15Z
- 저자: Ade Pramono, Jie Ren, Ivy Peng
- 식별자: `arxiv:2609.19936`

## 요약·초록

Memory over-provisioning results in resource underutilization when HPC workloads run on Kubernetes. The default Vertical Pod Autoscaler (VPA) cannot anticipate phase-driven memory spikes for first-run HPC jobs. In this work, we present a reinforcement learning (RL) recommender VERA that formulates vertical memory scaling as a Markov Decision Process and trains an agent on 3353 real Prometheus traces. Evaluated on a live Google Kubernetes Engine cluster using LAMMPS, graph analytics, in-memory analytics, and MLPerf 3D-UNet, the RL agent reclaims 31.6% of the available memory headroom and incurs at most one OOM event while VPA reclaims -7.9% over the same runs, raising memory provisioning, and its recommendation would have been insufficient to avoid OOM in 30 runs. The results demonstrate that an observation-driven RL recommender could outperform retrospective heuristics for dynamic memory scaling.

## 내 메모


