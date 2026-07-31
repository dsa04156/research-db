---
type: research-source
item_id: 454
title: "Towards Efficient Deployment of Hybrid SNNs on Neuromorphic and Edge AI Hardware"
source: "arxiv"
published: "2024-07-11T17:40:39Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.08704"
url: "https://arxiv.org/abs/2407.08704v1"
generated_by: codex-research-db
aliases:
  - "Towards Efficient Deployment of Hybrid SNNs on Neuromorphic and Edge AI Hardware"
topics:
  - "edge-computing"
---

# Towards Efficient Deployment of Hybrid SNNs on Neuromorphic and Edge AI Hardware

[원문 열기](https://arxiv.org/abs/2407.08704v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MH8RF2A7`)
- 발행일: 2024-07-11T17:40:39Z
- 저자: James Seekings, Peyton Chandarana, Mahsa Ardakani, MohammadReza Mohammadi, Ramtin Zand
- 식별자: `arxiv:2407.08704`

## 요약·초록

This paper explores the synergistic potential of neuromorphic and edge computing to create a versatile machine learning (ML) system tailored for processing data captured by dynamic vision sensors. We construct and train hybrid models, blending spiking neural networks (SNNs) and artificial neural networks (ANNs) using PyTorch and Lava frameworks. Our hybrid architecture integrates an SNN for temporal feature extraction and an ANN for classification. We delve into the challenges of deploying such hybrid structures on hardware. Specifically, we deploy individual components on Intel's Neuromorphic Processor Loihi (for SNN) and Jetson Nano (for ANN). We also propose an accumulator circuit to transfer data from the spiking to the non-spiking domain. Furthermore, we conduct comprehensive performance analyses of hybrid SNN-ANN models on a heterogeneous system of neuromorphic and edge AI hardware, evaluating accuracy, latency, power, and energy consumption. Our findings demonstrate that the hybrid spiking networks surpass the baseline ANN model across all metrics and outperform the baseline SNN model in accuracy and latency.

## 내 메모


