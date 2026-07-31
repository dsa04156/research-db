---
type: research-source
item_id: 897
title: "SLED: A Speculative LLM Decoding Framework for Efficient Edge Serving"
source: "arxiv"
published: "2025-06-11T04:55:54Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2506.09397"
url: "https://arxiv.org/abs/2506.09397v5"
generated_by: codex-research-db
aliases:
  - "SLED: A Speculative LLM Decoding Framework for Efficient Edge Serving"
topics:
  - "edge-computing"
---

# SLED: A Speculative LLM Decoding Framework for Efficient Edge Serving

[원문 열기](https://arxiv.org/abs/2506.09397v5)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`NNTZQBVI`)
- 발행일: 2025-06-11T04:55:54Z
- 저자: Xiangchen Li, Dimitrios Spatharakis, Saeid Ghafouri, Jiakun Fan, Hans Vandierendonck, Deepu John, Bo Ji, Dimitrios Nikolopoulos
- 식별자: `arxiv:2506.09397`

## 요약·초록

The growing gap between the increasing complexity of large language models (LLMs) and the limited computational budgets of edge devices poses a key challenge for efficient on-device inference, despite gradual improvements in hardware capabilities. Existing strategies, such as aggressive quantization, pruning, or remote inference, trade accuracy for efficiency or lead to substantial cost burdens. This position paper introduces a new framework that leverages speculative decoding, previously viewed primarily as a decoding acceleration technique for autoregressive generation of LLMs, as a promising approach specifically adapted for edge computing by orchestrating computation across heterogeneous devices. We propose \acronym, a framework that allows lightweight edge devices to draft multiple candidate tokens locally using diverse draft models, while a single, shared edge server verifies the tokens utilizing a more precise target model. To further increase the efficiency of verification, the edge server batch the diverse verification requests from devices. This approach supports device heterogeneity and reduces server-side memory footprint by sharing the same upstream target model across multiple devices. Our initial experiments with Jetson Orin Nano, Raspberry Pi 4B/5, and an edge server equipped with 4 Nvidia A100 GPUs indicate substantial benefits: 2.2 more system throughput, 2.8 more system capacity, and better cost efficiency, all without sacrificing model accuracy.

## 내 메모


