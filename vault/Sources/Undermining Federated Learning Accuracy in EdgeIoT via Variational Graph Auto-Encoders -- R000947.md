---
type: research-source
item_id: 947
title: "Undermining Federated Learning Accuracy in EdgeIoT via Variational Graph Auto-Encoders"
source: "arxiv"
published: "2025-04-14T10:09:38Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2504.10067"
url: "https://arxiv.org/abs/2504.10067v1"
generated_by: codex-research-db
aliases:
  - "Undermining Federated Learning Accuracy in EdgeIoT via Variational Graph Auto-Encoders"
topics:
  - "edge-computing"
---

# Undermining Federated Learning Accuracy in EdgeIoT via Variational Graph Auto-Encoders

[원문 열기](https://arxiv.org/abs/2504.10067v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ISH4M6BF`)
- 발행일: 2025-04-14T10:09:38Z
- 저자: Kai Li, Shuyan Hu, Bochun Wu, Sai Zou, Wei Ni, Falko Dressler
- 식별자: `arxiv:2504.10067`

## 요약·초록

EdgeIoT represents an approach that brings together mobile edge computing with Internet of Things (IoT) devices, allowing for data processing close to the data source. Sending source data to a server is bandwidth-intensive and may compromise privacy. Instead, federated learning allows each device to upload a shared machine-learning model update with locally processed data. However, this technique, which depends on aggregating model updates from various IoT devices, is vulnerable to attacks from malicious entities that may inject harmful data into the learning process. This paper introduces a new attack method targeting federated learning in EdgeIoT, known as data-independent model manipulation attack. This attack does not rely on training data from the IoT devices but instead uses an adversarial variational graph auto-encoder (AV-GAE) to create malicious model updates by analyzing benign model updates intercepted during communication. AV-GAE identifies and exploits structural relationships between benign models and their training data features. By manipulating these structural correlations, the attack maximizes the training loss of the federated learning system, compromising its overall effectiveness.

## 내 메모


