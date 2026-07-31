---
type: research-source
item_id: 1221
title: "QoS-Aware Load Balancing in the Computing Continuum via Multi-Player Bandits"
source: "arxiv"
published: "2025-12-21T23:18:07Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2512.18915"
url: "https://arxiv.org/abs/2512.18915v2"
generated_by: codex-research-db
aliases:
  - "QoS-Aware Load Balancing in the Computing Continuum via Multi-Player Bandits"
topics:
  - "kubernetes"
---

# QoS-Aware Load Balancing in the Computing Continuum via Multi-Player Bandits

[원문 열기](https://arxiv.org/abs/2512.18915v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`Z4XWSK4H`)
- 발행일: 2025-12-21T23:18:07Z
- 저자: Ivan Čilić, Ivana Podnar Žarko, Pantelis Frangoudis, Schahram Dustdar
- 식별자: `arxiv:2512.18915`

## 요약·초록

As computation shifts from the cloud to the edge to reduce processing latency and network traffic, the resulting Computing Continuum (CC) creates a dynamic environment where meeting strict Quality of Service (QoS) requirements and avoiding service instance overload becomes challenging. Existing methods often prioritize global metrics and overlook per-client QoS, which is crucial for latency-sensitive and reliability-critical applications. We propose QEdgeProxy, a decentralized QoS-aware load balancer that acts as a proxy between IoT devices and service instances in the CC. We formulate the load balancing problem as a Multi-Player Multi-Armed Bandit (MP-MAB) with heterogeneous rewards: Each load balancer autonomously selects service instances to maximize the probability of meeting its clients' QoS requirements by using Kernel Density Estimation (KDE) to estimate QoS success probabilities. Our load-balancing algorithm also incorporates an adaptive exploration mechanism to recover rapidly from performance shifts and non-stationary conditions. We present a Kubernetes-native QEdgeProxy implementation and evaluate it on an emulated CC testbed deployed on a K3s cluster with realistic network conditions and a latency-sensitive edge-AI workload. Results show that QEdgeProxy significantly outperforms proximity-based and reinforcement-learning baselines in per-client QoS satisfaction, while adapting effectively to load surges and changes in instance availability.

## 내 메모


