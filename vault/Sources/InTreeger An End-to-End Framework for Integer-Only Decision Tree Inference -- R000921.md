---
type: research-source
item_id: 921
title: "InTreeger: An End-to-End Framework for Integer-Only Decision Tree Inference"
source: "arxiv"
published: "2025-05-21T11:28:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.15391"
url: "https://arxiv.org/abs/2505.15391v1"
generated_by: codex-research-db
aliases:
  - "InTreeger: An End-to-End Framework for Integer-Only Decision Tree Inference"
topics:
  - "edge-computing"
---

# InTreeger: An End-to-End Framework for Integer-Only Decision Tree Inference

[원문 열기](https://arxiv.org/abs/2505.15391v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`XNAIDFNS`)
- 발행일: 2025-05-21T11:28:43Z
- 저자: Duncan Bart, Bruno Endres Forlin, Ana-Lucia Varbanescu, Marco Ottavi, Kuan-Hsun Chen
- 식별자: `arxiv:2505.15391`

## 요약·초록

Integer quantization has emerged as a critical technique to facilitate deployment on resource-constrained devices. Although they do reduce the complexity of the learning models, their inference performance is often prone to quantization-induced errors. To this end, we introduce InTreeger: an end-to-end framework that takes a training dataset as input, and outputs an architecture-agnostic integer-only C implementation of tree-based machine learning model, without loss of precision. This framework enables anyone, even those without prior experience in machine learning, to generate a highly optimized integer-only classification model that can run on any hardware simply by providing an input dataset and target variable. We evaluated our generated implementations across three different architectures (ARM, x86, and RISC-V), resulting in significant improvements in inference latency. In addition, we show the energy efficiency compared to typical decision tree implementations that rely on floating-point arithmetic. The results underscore the advantages of integer-only inference, making it particularly suitable for energy- and area-constrained devices such as embedded systems and edge computing platforms, while also enabling the execution of decision trees on existing ultra-low power devices.

## 내 메모


