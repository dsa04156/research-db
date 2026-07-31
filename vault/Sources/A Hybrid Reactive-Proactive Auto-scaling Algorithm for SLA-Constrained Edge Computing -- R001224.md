---
type: research-source
item_id: 1224
title: "A Hybrid Reactive-Proactive Auto-scaling Algorithm for SLA-Constrained Edge Computing"
source: "arxiv"
published: "2025-12-16T11:01:48Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2512.14290"
url: "https://arxiv.org/abs/2512.14290v1"
generated_by: codex-research-db
aliases:
  - "A Hybrid Reactive-Proactive Auto-scaling Algorithm for SLA-Constrained Edge Computing"
topics:
  - "edge-computing"
  - "kubernetes"
---

# A Hybrid Reactive-Proactive Auto-scaling Algorithm for SLA-Constrained Edge Computing

[원문 열기](https://arxiv.org/abs/2512.14290v1)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JAN2WFCF`)
- 발행일: 2025-12-16T11:01:48Z
- 저자: Suhrid Gupta, Muhammed Tawfiqul Islam, Rajkumar Buyya
- 식별자: `arxiv:2512.14290`

## 요약·초록

Edge computing decentralizes computing resources, allowing for novel applications in domains such as the Internet of Things (IoT) in healthcare and agriculture by reducing latency and improving performance. This decentralization is achieved through the implementation of microservice architectures, which require low latencies to meet stringent service level agreements (SLA) such as performance, reliability, and availability metrics. While cloud computing offers the large data storage and computation resources necessary to handle peak demands, a hybrid cloud and edge environment is required to ensure SLA compliance. This is achieved by sophisticated orchestration strategies such as Kubernetes, which help facilitate resource management. The orchestration strategies alone do not guarantee SLA adherence due to the inherent delay of scaling resources. Existing auto-scaling algorithms have been proposed to address these challenges, but they suffer from performance issues and configuration complexity. In this paper, a novel auto-scaling algorithm is proposed for SLA-constrained edge computing applications. This approach combines a Machine Learning (ML) based proactive auto-scaling algorithm, capable of predicting incoming resource requests to forecast demand, with a reactive autoscaler which considers current resource utilization and SLA constraints for immediate adjustments. The algorithm is integrated into Kubernetes as an extension, and its performance is evaluated through extensive experiments in an edge environment with real applications. The results demonstrate that existing solutions have an SLA violation rate of up to 23%, whereas the proposed hybrid solution outperforms the baselines with an SLA violation rate of only 6%, ensuring stable SLA compliance across various applications.

## 내 메모


