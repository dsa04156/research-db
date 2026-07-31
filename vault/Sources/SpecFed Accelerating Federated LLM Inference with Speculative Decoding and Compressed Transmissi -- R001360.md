---
type: research-source
item_id: 1360
title: "SpecFed: Accelerating Federated LLM Inference with Speculative Decoding and Compressed Transmission"
source: "arxiv"
published: "2026-04-28T15:44:50Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.25777"
url: "https://arxiv.org/abs/2604.25777v2"
generated_by: codex-research-db
aliases:
  - "SpecFed: Accelerating Federated LLM Inference with Speculative Decoding and Compressed Transmission"
topics:
  - "edge-computing"
---

# SpecFed: Accelerating Federated LLM Inference with Speculative Decoding and Compressed Transmission

[원문 열기](https://arxiv.org/abs/2604.25777v2)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`K9V2NJHN`)
- 발행일: 2026-04-28T15:44:50Z
- 저자: Ce Zheng, Xinghan Wang, Jiahong Ning, Yuxuan Shi, Ning Huang, Tingting Yang
- 식별자: `arxiv:2604.25777`

## 요약·초록

Federated inference enhances LLM performance in edge computing through weighted averaging of distributed model predictions. However, autoregressive LLM inference requires frequent full-model forward passes across workers, severely limiting decoding throughput. Distributed deployment further aggravates this due to a communication bottleneck: each worker must transmit full token probability distributions per draft token, dominating end-to-end latency. To address these challenges, we introduce speculative decoding to enable parallel LLM processing and propose a top-K compressed transmission scheme with two server-side reconstruction strategies. We theoretically analyze the robustness of our method in terms of local reconstruction error, aggregation bias, and acceptance-rate bias, and derive corresponding bounds. Experiments demonstrate that our scheme achieves high generation fidelity while significantly reducing communication overhead.

## 내 메모


