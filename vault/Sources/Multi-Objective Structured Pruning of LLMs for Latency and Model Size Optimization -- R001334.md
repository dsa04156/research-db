---
type: research-source
item_id: 1334
title: "Multi-Objective Structured Pruning of LLMs for Latency and Model Size Optimization"
source: "arxiv"
published: "2026-06-08T09:38:13Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.22583"
url: "https://arxiv.org/abs/2607.22583v1"
generated_by: codex-research-db
aliases:
  - "Multi-Objective Structured Pruning of LLMs for Latency and Model Size Optimization"
topics:
  - "edge-computing"
---

# Multi-Objective Structured Pruning of LLMs for Latency and Model Size Optimization

[원문 열기](https://arxiv.org/abs/2607.22583v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`BEN64WQT`)
- 발행일: 2026-06-08T09:38:13Z
- 저자: Muhammad Junaid Ali, Smail Niar, El-Ghazali Talbi
- 식별자: `arxiv:2607.22583`

## 요약·초록

Large Language Models (LLMs) have achieved widespread adoption because of their strong reasoning and query-response capabilities. However, deploying them in embedded and edge computing environments remains challenging because of strict latency, memory, and energy constraints. Their large parameter counts and computational demands hinder efficient execution on resource-constrained platforms. Although model pruning has emerged as a viable solution for reducing scale while preserving performance, jointly optimizing layers, attention heads, and Multi-Layer Perceptron (MLP) dimensions remains highly complex. Exhaustively exploring this combined design space is computationally expensive and often leads to local optima or unstable configurations. To address these limitations, we propose a hardware-aware, multi-objective structured pruning framework. The proposed two-stage method explicitly targets latency and model size for efficient deployment on edge devices. In the coarse-grained stage, multi-objective depth pruning removes entire attention and MLP blocks to reduce computational load and memory usage. In the subsequent fine-grained stage, Parallel Bayesian Optimization (PBO) searches for the optimal layer-wise pruning ratios for pruning under latency constraints, while importance-based strategies rank the specific components to be pruned within each layer's allocated budget. Experimental results show that our approach reduces model complexity with minimal impact on commonsense reasoning tasks and zero-shot performance. Our method achieves a favorable trade-off among accuracy, latency, and model size, making it suitable for edge deployment. Across multiple LLMs at 37.5% and 50% pruning ratios, the proposed approach achieves better performance on commonsense reasoning tasks than existing methods while significantly reducing inference cost.

## 내 메모


