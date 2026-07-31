---
type: research-source
item_id: 1184
title: "NL-CPS: Reinforcement Learning-Based Kubernetes Control Plane Placement in Multi-Region Clusters"
source: "arxiv"
published: "2026-04-09T16:36:29Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.08434"
url: "https://arxiv.org/abs/2604.08434v1"
generated_by: codex-research-db
aliases:
  - "NL-CPS: Reinforcement Learning-Based Kubernetes Control Plane Placement in Multi-Region Clusters"
topics:
  - "kubernetes"
  - "edge-computing"
---

# NL-CPS: Reinforcement Learning-Based Kubernetes Control Plane Placement in Multi-Region Clusters

[원문 열기](https://arxiv.org/abs/2604.08434v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SF7EZ6SI`)
- 발행일: 2026-04-09T16:36:29Z
- 저자: Sajid Alam, Amjad Ullah, Ze Wang
- 식별자: `arxiv:2604.08434`

## 요약·초록

The placement of Kubernetes control-plane nodes is critical to ensuring cluster reliability, scalability, and performance, and therefore represents a significant deployment challenge in heterogeneous, multi-region environments. Existing initialisation procedures typically select control-plane hosts arbitrarily, without considering node resource capacity or network topology, often leading to suboptimal cluster performance and reduced resilience. Given Kubernetes's status as the de facto standard for container orchestration, there is a need to rigorously evaluate how control-plane node placement influences the overall performance of the cluster operating across multiple regions. This paper advances this goal by introducing an intelligent methodology for selecting control-plane node placement across dynamically selected Cloud-Edge resources spanning multiple regions, as part of an automated orchestration system. More specifically, we propose a reinforcement learning framework based on neural contextual bandits that observes operational performance and learns optimal control-plane placement policies from infrastructure characteristics. Experimental evaluation across several geographically distributed regions and multiple cluster configurations demonstrates substantial performance improvements over several baseline approaches.

## 내 메모


