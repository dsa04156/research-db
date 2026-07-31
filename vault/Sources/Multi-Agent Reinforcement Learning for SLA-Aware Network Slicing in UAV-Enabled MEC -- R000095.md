---
type: research-source
item_id: 95
title: "Multi-Agent Reinforcement Learning for SLA-Aware Network Slicing in UAV-Enabled MEC"
source: "arxiv"
published: "2026-07-10T11:19:06Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.09295"
url: "https://arxiv.org/abs/2607.09295v2"
generated_by: codex-research-db
aliases:
  - "Multi-Agent Reinforcement Learning for SLA-Aware Network Slicing in UAV-Enabled MEC"
topics:
  - "ai-agents"
  - "edge-computing"
---

# Multi-Agent Reinforcement Learning for SLA-Aware Network Slicing in UAV-Enabled MEC

[원문 열기](https://arxiv.org/abs/2607.09295v2)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HEPXC2DR`)
- 발행일: 2026-07-10T11:19:06Z
- 저자: Mohammad Farhoudi, Zeinab Sasan, Masoud Shokrnezhad, Tarik Taleb
- 식별자: `arxiv:2607.09295`

## 요약·초록

Unmanned Aerial Vehicle (UAV)-enabled Mobile Edge Computing (MEC) offers flexible capacity provisioning for heterogeneous network slices, including Hyper-Reliable and Low-Latency Communication (HRLLC), Enhanced Mobile Broadband (eMBB), and Massive Machine-Type Communications (mMTC). However, guaranteeing slice-level Service-Level Agreements (SLAs) under dynamic user mobility, stochastic task arrivals, and constrained onboard energy and computing resources remains a fundamental challenge. This paper proposes a predictive multi-agent Reinforcement Learning (RL) framework that proactively maintains SLA stability in UAV-enabled MEC through coordinated trajectory control and computation resource allocation. A lightweight prediction module forecasts near-future user mobility, enabling UAVs to anticipate congestion and reposition before SLA violations occur. We design an SLA-aware reward function that explicitly penalizes both violation probability and duration across slices, alongside total energy consumption. UAV agents are trained using Multi-Agent Proximal Policy Optimization (MAPPO) with centralized training and decentralized execution, enabling scalable online decision-making. Event-driven simulations with realistic mobility traces demonstrate that the proposed framework significantly improves SLA stability compared with baselines while maintaining competitive energy efficiency and delay performance, approaching oracle-level performance with sufficiently accurate predictive information.

## 내 메모


