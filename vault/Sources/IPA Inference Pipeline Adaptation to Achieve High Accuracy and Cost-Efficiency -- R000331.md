---
type: research-source
item_id: 331
title: "IPA: Inference Pipeline Adaptation to Achieve High Accuracy and Cost-Efficiency"
source: "arxiv"
published: "2023-08-24T15:48:21Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.5070/sr34163500"
url: "https://arxiv.org/abs/2308.12871v3"
generated_by: codex-research-db
aliases:
  - "IPA: Inference Pipeline Adaptation to Achieve High Accuracy and Cost-Efficiency"
topics:
  - "kubernetes"
---

# IPA: Inference Pipeline Adaptation to Achieve High Accuracy and Cost-Efficiency

[원문 열기](https://arxiv.org/abs/2308.12871v3)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`PDMD2V3W`)
- 발행일: 2023-08-24T15:48:21Z
- 저자: Saeid Ghafouri, Kamran Razavi, Mehran Salmani, Alireza Sanaee, Tania Lorido-Botran, Lin Wang, Joseph Doyle, Pooyan Jamshidi
- 식별자: `doi:10.5070/sr34163500`

## 요약·초록

Efficiently optimizing multi-model inference pipelines for fast, accurate, and cost-effective inference is a crucial challenge in machine learning production systems, given their tight end-to-end latency requirements. To simplify the exploration of the vast and intricate trade-off space of latency, accuracy, and cost in inference pipelines, providers frequently opt to consider one of them. However, the challenge lies in reconciling latency, accuracy, and cost trade-offs. To address this challenge and propose a solution to efficiently manage model variants in inference pipelines, we present IPA, an online deep learning Inference Pipeline Adaptation system that efficiently leverages model variants for each deep learning task. Model variants are different versions of pre-trained models for the same deep learning task with variations in resource requirements, latency, and accuracy. IPA dynamically configures batch size, replication, and model variants to optimize accuracy, minimize costs, and meet user-defined latency Service Level Agreements (SLAs) using Integer Programming. It supports multi-objective settings for achieving different trade-offs between accuracy and cost objectives while remaining adaptable to varying workloads and dynamic traffic patterns. Navigating a wider variety of configurations allows \namex{} to achieve better trade-offs between cost and accuracy objectives compared to existing methods. Extensive experiments in a Kubernetes implementation with five real-world inference pipelines demonstrate that IPA improves end-to-end accuracy by up to 21% with a minimal cost increase. The code and data for replications are available at https://github.com/reconfigurable-ml-pipeline/ipa.

## 내 메모


