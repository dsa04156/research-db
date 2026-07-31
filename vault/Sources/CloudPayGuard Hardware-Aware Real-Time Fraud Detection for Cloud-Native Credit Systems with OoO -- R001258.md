---
type: research-source
item_id: 1258
title: "CloudPayGuard: Hardware-Aware Real-Time Fraud Detection for Cloud-Native Credit Systems with OoO CPU Microarchitecture Optimization"
source: "openalex"
published: "2026-05-25"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.63313/jcsft.9079"
url: "https://doi.org/10.63313/jcsft.9079"
generated_by: codex-research-db
aliases:
  - "CloudPayGuard: Hardware-Aware Real-Time Fraud Detection for Cloud-Native Credit Systems with OoO CPU Microarchitecture Optimization"
topics:
  - "kubernetes"
---

# CloudPayGuard: Hardware-Aware Real-Time Fraud Detection for Cloud-Native Credit Systems with OoO CPU Microarchitecture Optimization

[원문 열기](https://doi.org/10.63313/jcsft.9079)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`UJGI8CNC`)
- 발행일: 2026-05-25
- 저자: Hanqing YAO, Jixiang Ding, Zifan Wang
- 식별자: `doi:10.63313/jcsft.9079`

## 요약·초록

Real-time fraud detection in cloud-native credit payment systems is a critical challenge due to the increasing complexity of transaction networks, the rapid evolution of fraudulent behaviors, and the high computational demands of modern deep learning models. To address these challenges, we propose CloudPayGuard, a hardware-aware framework that integrates Temporal Heterogeneous Graph Neural Networks (TH-GNN) for dynamic transaction modeling, Large Language Models (LLM) for automated security policy generation, and out-of-order (OoO) CPU microarchitecture performance prediction for hardware-accelerated inference. CloudPayGuard constructs multi-modal transaction graphs incorporating user behavior sequences, device fingerprints, and geolocation information, enabling real-time identification of suspicious activities with millisecond-level latency. The framework dynamically generates and verifies risk policies through LLM-based reasoning and constraint checking, ensuring trustworthy and adaptive deployment in cloud-native environments. To optimize inference performance, a deep learning-based CPU microarchitecture predictor estimates IPC and identifies potential bottlenecks in ROB, IQ, and LSQ resources, allowing dynamic adjustment of CPU parameters and task scheduling. Experiments on a large-scale financial transaction dataset show that CloudPayGuard achieves an F1-score of 0.91 and an average inference latency of 6 milliseconds, outperforming baseline TH-GNN and other models. The OoO CPU microarchitecture optimization reduces latency by 34–40%, while LLM-driven policy generation and TH-GNN-based graph modeling ensure accurate fraud detection. These results demonstrate CloudPayGuard’s efficiency, scalability, and effectiveness for real-time fraud detection in cloud-native credit systems.

## 내 메모


