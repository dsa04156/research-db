---
type: research-source
item_id: 482
title: "Athena: Efficient Block-Wise Post-Training Quantization for Large Language Models Using Second-Order Matrix Derivative Information"
source: "arxiv"
published: "2024-05-24T03:14:29Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2405.17470"
url: "https://arxiv.org/abs/2405.17470v1"
generated_by: codex-research-db
aliases:
  - "Athena: Efficient Block-Wise Post-Training Quantization for Large Language Models Using Second-Order Matrix Derivative Information"
topics:
  - "edge-computing"
---

# Athena: Efficient Block-Wise Post-Training Quantization for Large Language Models Using Second-Order Matrix Derivative Information

[원문 열기](https://arxiv.org/abs/2405.17470v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`QIENWEXZ`)
- 발행일: 2024-05-24T03:14:29Z
- 저자: Yanshu Wang, Wenyang He, Tong Yang
- 식별자: `arxiv:2405.17470`

## 요약·초록

Large Language Models (LLMs) have significantly advanced natural language processing tasks such as machine translation, text generation, and sentiment analysis. However, their large size, often consisting of billions of parameters, poses challenges for storage, computation, and deployment, particularly in resource-constrained environments like mobile devices and edge computing platforms. Effective compression and quantization techniques are crucial for addressing these issues, reducing memory footprint and computational requirements without significantly compromising performance. Traditional methods that uniformly map parameters to compressed spaces fail to account for the uneven distribution of parameters, leading to substantial accuracy loss. In this work, we propose Athena, a novel algorithm for efficient block-wise post-training quantization of LLMs. Athena leverages Second-Order Matrix Derivative Information to guide the quantization process using the curvature information of the loss landscape. By grouping parameters by columns or rows and iteratively optimizing the quantization process, Athena updates the model parameters and Hessian matrix to achieve significant compression while maintaining high accuracy. This makes Athena a practical solution for deploying LLMs in various settings.

## 내 메모


