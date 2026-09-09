---
type: research-source
item_id: 2627
title: "GreenPipe: Power Modeling for Containerized DNN Inference on Kubernetes Edge Nodes"
source: "arxiv"
published: "2026-09-04T09:57:51Z"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "arxiv:2609.04952"
url: "https://arxiv.org/abs/2609.04952v1"
generated_by: codex-research-db
aliases:
  - "GreenPipe: Power Modeling for Containerized DNN Inference on Kubernetes Edge Nodes"
topics:
  - "kubernetes"
---

# GreenPipe: Power Modeling for Containerized DNN Inference on Kubernetes Edge Nodes

[원문 열기](https://arxiv.org/abs/2609.04952v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`W8NXX82N`)
- 발행일: 2026-09-04T09:57:51Z
- 저자: Mengxue Wang, Peini Liu, Amir Taherkordi, Jordi Guitart
- 식별자: `arxiv:2609.04952`

## 요약·초록

Distributed DNN inference is increasingly deployed in containerized edge-cloud environments, where workloads run on-device or are exposed to remote clients over the network. Accurate online power estimation on resource-constrained ARM nodes without hardware power counters such as RAPL remains a challenge, and CPU-only models fail to capture multi-resource behavior. We present GreenPipe, an automated profiling-training-validation pipeline that builds multi-resource regression models from external power meter measurements and attributes power to containers proportionally. GreenPipe is evaluated on a Raspberry Pi 4 edge node in a K3s edge-cloud testbed, covering DNN inference with three vision models, multiple precisions, thread counts, and both local and serving scenarios. System-level MAPE is 6.3-9.4%, improving over CPU-stress and utilization-only baselines by 26.9% MAPE on average. We jointly report inference latency and energy per inference, exposing performance-energy trade-offs across workload configurations.

## 내 메모


