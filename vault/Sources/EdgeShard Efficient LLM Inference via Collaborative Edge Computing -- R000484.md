---
type: research-source
item_id: 484
title: "EdgeShard: Efficient LLM Inference via Collaborative Edge Computing"
source: "arxiv"
published: "2024-05-23T09:46:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2405.14371"
url: "https://arxiv.org/abs/2405.14371v1"
generated_by: codex-research-db
aliases:
  - "EdgeShard: Efficient LLM Inference via Collaborative Edge Computing"
topics:
  - "edge-computing"
---

# EdgeShard: Efficient LLM Inference via Collaborative Edge Computing

[원문 열기](https://arxiv.org/abs/2405.14371v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`AXDRJ893`)
- 발행일: 2024-05-23T09:46:22Z
- 저자: Mingjin Zhang, Jiannong Cao, Xiaoming Shen, Zeyang Cui
- 식별자: `arxiv:2405.14371`

## 요약·초록

Large language models (LLMs) have shown great potential in natural language processing and content generation. However, current LLMs heavily rely on cloud computing, leading to prolonged latency, high bandwidth cost, and privacy concerns. Edge computing is promising to address such concerns by deploying LLMs on edge devices, closer to data sources. Some works try to leverage model quantization to reduce the model size to fit the resource-constraint edge devices, but they lead to accuracy loss. Other works use cloud-edge collaboration, suffering from unstable network connections. In this work, we leverage collaborative edge computing to facilitate the collaboration among edge devices and cloud servers for jointly performing efficient LLM inference. We propose a general framework to partition the LLM model into shards and deploy on distributed devices. To achieve efficient LLM inference, we formulate an adaptive joint device selection and model partition problem and design an efficient dynamic programming algorithm to optimize the inference latency and throughput, respectively. Experiments of Llama2 serial models on a heterogeneous physical prototype demonstrate that EdgeShard achieves up to 50% latency reduction and 2x throughput improvement over baseline methods.

## 내 메모


