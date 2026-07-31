---
type: research-source
item_id: 1159
title: "Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation"
source: "arxiv"
published: "2026-05-27T09:37:55Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.28222"
url: "https://arxiv.org/abs/2605.28222v1"
generated_by: codex-research-db
aliases:
  - "Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation"
topics:
  - "kubernetes"
---

# Analyzing Quality-Latency-Resource Trade-offs in a Technical Documentation RAG Assistant Using LoRA Adaptation

[원문 열기](https://arxiv.org/abs/2605.28222v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`XWPTIS9S`)
- 발행일: 2026-05-27T09:37:55Z
- 저자: Evgenii Palnikov, Elizaveta Gavrilova
- 식별자: `arxiv:2605.28222`

## 요약·초록

We study quality-latency-resource trade-offs in a documentation-grounded retrieval-augmented generation (RAG) system that uses Low-Rank Adaptation (LoRA) of the generator. We build a manually verified benchmark of 5,144 question-answer pairs over the official Kubernetes documentation and combine it with a fixed hybrid-retrieval pipeline (BGE-M3 dense, BGE-M3 native sparse, Reciprocal Rank Fusion, cross-encoder reranking). Over this benchmark we ablate 20 LoRA configurations on Llama-3.2-3B-Instruct and Llama-3.1-8B-Instruct across rank and target-module choices, and evaluate each on token-level F1, LLM-judged groundedness and correctness (pass@4), inference latency, inference memory, and training cost, all reported with bootstrap 95% confidence intervals. Pareto analysis shows that LoRA adapters acting only on the q and v attention projections consistently dominate the front, while the 3B/8B choice mainly defines operating regime. A param-matched control comparison further indicates that the q/v advantage is structural rather than purely parametric. The benchmark, selected adapters, and code are available at https://github.com/EugPal/rag-lora-tradeoffs.

## 내 메모


