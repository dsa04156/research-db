---
type: research-source
item_id: 699
title: "Streamlining Resilient Kubernetes Autoscaling with Multi-Agent Systems via an Automated Online Design Framework"
source: "arxiv"
published: "2025-05-26T20:39:31Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.21559"
url: "https://arxiv.org/abs/2505.21559v1"
generated_by: codex-research-db
aliases:
  - "Streamlining Resilient Kubernetes Autoscaling with Multi-Agent Systems via an Automated Online Design Framework"
topics:
  - "kubernetes"
  - "ai-agents"
---

# Streamlining Resilient Kubernetes Autoscaling with Multi-Agent Systems via an Automated Online Design Framework

[원문 열기](https://arxiv.org/abs/2505.21559v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KSURUIJR`)
- 발행일: 2025-05-26T20:39:31Z
- 저자: Julien Soulé, Jean-Paul Jamont, Michel Occello, Louis-Marie Traonouez, Paul Théron
- 식별자: `arxiv:2505.21559`

## 요약·초록

In cloud-native systems, Kubernetes clusters with interdependent services often face challenges to their operational resilience due to poor workload management issues such as resource blocking, bottlenecks, or continuous pod crashes. These vulnerabilities are further amplified in adversarial scenarios, such as Distributed Denial-of-Service attacks (DDoS). Conventional Horizontal Pod Autoscaling (HPA) approaches struggle to address such dynamic conditions, while reinforcement learning-based methods, though more adaptable, typically optimize single goals like latency or resource usage, neglecting broader failure scenarios. We propose decomposing the overarching goal of maintaining operational resilience into failure-specific sub-goals delegated to collaborative agents, collectively forming an HPA Multi-Agent System (MAS). We introduce an automated, four-phase online framework for HPA MAS design: 1) modeling a digital twin built from cluster traces; 2) training agents in simulation using roles and missions tailored to failure contexts; 3) analyzing agent behaviors for explainability; and 4) transferring learned policies to the real cluster. Experimental results demonstrate that the generated HPA MASs outperform three state-of-the-art HPA systems in sustaining operational resilience under various adversarial conditions in a proposed complex cluster.

## 내 메모


