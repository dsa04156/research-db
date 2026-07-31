---
type: research-source
item_id: 1182
title: "NimbusGuard: A Novel Framework for Proactive Kubernetes Autoscaling Using Deep Q-Networks"
source: "arxiv"
published: "2026-04-13T05:32:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/icoin68469.2026.11480646"
url: "https://arxiv.org/abs/2604.11017v1"
generated_by: codex-research-db
aliases:
  - "NimbusGuard: A Novel Framework for Proactive Kubernetes Autoscaling Using Deep Q-Networks"
topics:
  - "kubernetes"
---

# NimbusGuard: A Novel Framework for Proactive Kubernetes Autoscaling Using Deep Q-Networks

[원문 열기](https://arxiv.org/abs/2604.11017v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NH65V54C`)
- 발행일: 2026-04-13T05:32:12Z
- 저자: Chamath Wanigasooriya, Indrajith Ekanayake
- 식별자: `doi:10.1109/icoin68469.2026.11480646`

## 요약·초록

Cloud native architecture is about building and running scalable microservice applications to take full advantage of the cloud environments. Managed Kubernetes is the powerhouse orchestrating cloud native applications with elastic scaling. However, traditional Kubernetes autoscalers are reactive, meaning the scaling controllers adjust resources only after they detect demand within the cluster and do not incorporate any predictive measures. This can lead to either over-provisioning and increased costs or under-provisioning and performance degradation. We propose NimbusGuard, an open-source, Kubernetes-based autoscaling system that leverages a deep reinforcement learning agent to provide proactive autoscaling. The agents perception is augmented by a Long Short-Term Memory model that forecasts future workload patterns. The evaluations were conducted by comparing NimbusGuard against the built-in scaling controllers, such as Horizontal Pod Autoscaler, and the event-driven autoscaler KEDA. The experimental results demonstrate how NimbusGuard's proactive framework translates into superior performance and cost efficiency compared to existing reactive methods.

## 내 메모


