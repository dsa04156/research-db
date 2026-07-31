---
type: research-source
item_id: 308
title: "QEdgeProxy: QoS-Aware Load Balancing for IoT Services in the Computing Continuum"
source: "arxiv"
published: "2024-05-17T13:56:49Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/edge62653.2024.00018"
url: "https://arxiv.org/abs/2405.10788v1"
generated_by: codex-research-db
aliases:
  - "QEdgeProxy: QoS-Aware Load Balancing for IoT Services in the Computing Continuum"
topics:
  - "kubernetes"
---

# QEdgeProxy: QoS-Aware Load Balancing for IoT Services in the Computing Continuum

[원문 열기](https://arxiv.org/abs/2405.10788v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FSXBIPFZ`)
- 발행일: 2024-05-17T13:56:49Z
- 저자: Ivan Čilić, Valentin Jukanović, Ivana Podnar Žarko, Pantelis Frangoudis, Schahram Dustdar
- 식별자: `doi:10.1109/edge62653.2024.00018`

## 요약·초록

While various service orchestration aspects within Computing Continuum (CC) systems have been extensively addressed, including service placement, replication, and scheduling, an open challenge lies in ensuring uninterrupted data delivery from IoT devices to running service instances in this dynamic environment, while adhering to specific Quality of Service (QoS) requirements and balancing the load on service instances. To address this challenge, we introduce QEdgeProxy, an adaptive and QoS-aware load balancing framework specifically designed for routing client requests to appropriate IoT service instances in the CC. QEdgeProxy integrates naturally within Kubernetes, adapts to changes in dynamic environments, and manages to seamlessly deliver data to IoT service instances while consistently meeting QoS requirements and effectively distributing load across them. This is verified by extensive experiments over a realistic K3s cluster with instance failures and network variability, where QEdgeProxy outperforms both Kubernetes built-in mechanisms and a state-of-the-art solution, while introducing minimal computational overhead.

## 내 메모


