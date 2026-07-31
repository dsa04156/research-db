---
type: research-source
item_id: 686
title: "Resilience Evaluation of Kubernetes in Cloud-Edge Environments via Failure Injection"
source: "arxiv"
published: "2025-07-21T23:37:14Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.16109"
url: "https://arxiv.org/abs/2507.16109v1"
generated_by: codex-research-db
aliases:
  - "Resilience Evaluation of Kubernetes in Cloud-Edge Environments via Failure Injection"
topics:
  - "edge-computing"
  - "kubernetes"
---

# Resilience Evaluation of Kubernetes in Cloud-Edge Environments via Failure Injection

[원문 열기](https://arxiv.org/abs/2507.16109v1)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`INJ2RRQ4`)
- 발행일: 2025-07-21T23:37:14Z
- 저자: Zihao Chen, Mohammad Goudarzi, Adel Nadjaran Toosi
- 식별자: `arxiv:2507.16109`

## 요약·초록

Kubernetes has emerged as an essential platform for deploying containerised applications across cloud and edge infrastructures. As Kubernetes gains increasing adoption for mission-critical microservices, evaluating system resilience under realistic fault conditions becomes crucial. However, systematic resilience assessments of Kubernetes in hybrid cloud-edge environments are currently limited in research. To address this gap, a novel resilience evaluation framework integrates mainstream fault injection tools with automated workload generation for comprehensive cloud-edge Kubernetes testing. Multiple fault injection platforms, including Chaos Mesh, Gremlin, and ChaosBlade are combined with realistic traffic simulation tools, enabling automated orchestration of complex failure scenarios. Through this framework, comprehensive experiments are conducted that systematically target node-level, pod-level, and network failures across cloud and cloud-edge environments. The first comprehensive resilience dataset for hybrid cloud-edge Kubernetes deployments is created, comprising over 30 GB of performance data from 11,965 fault injection scenarios including response times, failure rates, and error patterns. Analysis reveals that cloud-edge deployments demonstrate 80% superior response stability under network delay and partition conditions, while cloud deployments exhibit 47% better resilience under bandwidth limitations, providing quantitative guidance for architectural decision-making in cloud-edge deployments.

## 내 메모


