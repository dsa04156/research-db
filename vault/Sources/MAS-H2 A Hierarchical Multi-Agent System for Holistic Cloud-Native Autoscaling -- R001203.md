---
type: research-source
item_id: 1203
title: "MAS-H2: A Hierarchical Multi-Agent System for Holistic Cloud-Native Autoscaling"
source: "arxiv"
published: "2026-03-08T12:39:14Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.07607"
url: "https://arxiv.org/abs/2603.07607v1"
generated_by: codex-research-db
aliases:
  - "MAS-H2: A Hierarchical Multi-Agent System for Holistic Cloud-Native Autoscaling"
topics:
  - "kubernetes"
  - "ai-agents"
---

# MAS-H2: A Hierarchical Multi-Agent System for Holistic Cloud-Native Autoscaling

[원문 열기](https://arxiv.org/abs/2603.07607v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`R34UWGSB`)
- 발행일: 2026-03-08T12:39:14Z
- 저자: Hamed Hamzeh, Parisa Vahdatian
- 식별자: `arxiv:2603.07607`

## 요약·초록

Autoscaling in cloud-native platforms like Kubernetes is reactive and metric-driven, leading to a strategic void problem. This comes from the decoupling of higher-level business policies from lower-level resource provisioning. The strategic void, coupled with a fragmented coordination of pod and node scaling, can lead to significant resource waste and performance degradation under dynamic workloads. In this paper, we present MAS-H2, a new hierarchical multi-agent system that addresses the challenges of autonomic cloud resource management with a complete end-to-end solution. MAS-H2 systematically decomposes the control problem into three layers: a Strategic Agent that formalises business policies (e.g., cost vs. performance) into a global utility function; Planning Agents that produce a joint, proactive scaling plan for pods and nodes with time-series forecasting; and Execution Agents that execute the scaling plan. We built and tested a MAS-H2 prototype as a Kubernetes Operator on Google Kubernetes Engine (GKE) to benchmark it against the native Horizontal Pod Autoscaler (HPA) and Cluster Autoscaler (CA) baselines under two realistic, spiky, and stress-inducing workload scenarios. The results show that the MAS-H2 system maintained application CPU usage under 40% for predictable Heartbeat workloads. This resulted in over 50% less sustained CPU stress than the native HPA baseline, which typically operated above 80%. The MAS-H2 system demonstrated proactive planning in a volatile Chaotic Flash Sale scenario by filtering transient noise and deploying more replicas compared to HPA. It reduced peak CPU load by 55% without under-provisioning. Beyond performance, MAS-H2 seamlessly performed a zero-downtime strategic migration between two cost- and performance-optimised infrastructures.

## 내 메모


