---
type: research-source
item_id: 877
title: "SLIM: A Heterogeneous Accelerator for Edge Inference of Sparse Large Language Model via Adaptive Thresholding"
source: "arxiv"
published: "2025-07-12T08:44:38Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.09201"
url: "https://arxiv.org/abs/2507.09201v1"
generated_by: codex-research-db
aliases:
  - "SLIM: A Heterogeneous Accelerator for Edge Inference of Sparse Large Language Model via Adaptive Thresholding"
topics:
  - "edge-computing"
---

# SLIM: A Heterogeneous Accelerator for Edge Inference of Sparse Large Language Model via Adaptive Thresholding

[원문 열기](https://arxiv.org/abs/2507.09201v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`M47AZWPF`)
- 발행일: 2025-07-12T08:44:38Z
- 저자: Weihong Xu, Haein Choi, Po-kai Hsu, Shimeng Yu, Tajana Rosing
- 식별자: `arxiv:2507.09201`

## 요약·초록

Large language models (LLMs) have demonstrated exceptional proficiency in understanding and generating human language, but efficient inference on resource-constrained embedded devices remains challenging due to large model sizes and memory-intensive operations in feedforward network (FFN) and multi-head attention (MHA) layers. While existing accelerators offload LLM inference to expensive heterogeneous computing systems, they fail to exploit the significant sparsity inherent in LLM operations, leaving hardware resources underutilized. We propose SLIM, an algorithm-hardware co-design optimized for sparse LLM serving on edge devices. SLIM exploits LLM sparsity through an adaptive thresholding algorithm that enables runtime-configurable sparsity with negligible accuracy loss, fetching only activated neurons to dramatically reduce data movement. Our heterogeneous hardware architecture strategically combines near-storage processing (NSP) and processing-in-memory (PIM): FFN weights are stored in high-density 3D NAND and computed using NSP units, while memory-intensive MHA operations are processed in PIM modules. This design significantly reduces memory footprint, data movement, and energy consumption. Our comprehensive evaluation demonstrates SLIM's effectiveness, achieving 13-18x throughput improvements over SSD-GPU systems and 9-10x better energy efficiency over DRAM-GPU systems while maintaining low latency, making cost-effective LLM deployment viable for edge computing environments.

## 내 메모


