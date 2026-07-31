---
type: research-source
item_id: 700
title: "ELIS: Efficient LLM Iterative Scheduling System with Response Length Predictor"
source: "arxiv"
published: "2025-05-14T04:50:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2505.09142"
url: "https://arxiv.org/abs/2505.09142v1"
generated_by: codex-research-db
aliases:
  - "ELIS: Efficient LLM Iterative Scheduling System with Response Length Predictor"
topics:
  - "kubernetes"
---

# ELIS: Efficient LLM Iterative Scheduling System with Response Length Predictor

[원문 열기](https://arxiv.org/abs/2505.09142v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`C4K37QK2`)
- 발행일: 2025-05-14T04:50:00Z
- 저자: Seungbeom Choi, Jeonghoe Goo, Eunjoo Jeon, Mingyu Yang, Minsung Jang
- 식별자: `arxiv:2505.09142`

## 요약·초록

We propose ELIS, a serving system for Large Language Models (LLMs) featuring an Iterative Shortest Remaining Time First (ISRTF) scheduler designed to efficiently manage inference tasks with the shortest remaining tokens. Current LLM serving systems often employ a first-come-first-served scheduling strategy, which can lead to the "head-of-line blocking" problem. To overcome this limitation, it is necessary to predict LLM inference times and apply a shortest job first scheduling strategy. However, due to the auto-regressive nature of LLMs, predicting the inference latency is challenging. ELIS addresses this challenge by training a response length predictor for LLMs using the BGE model, an encoder-based state-of-the-art model. Additionally, we have devised the ISRTF scheduling strategy, an optimization of shortest remaining time first tailored to existing LLM iteration batching. To evaluate our work in an industrial setting, we simulate streams of requests based on our study of real-world user LLM serving trace records. Furthermore, we implemented ELIS as a cloud-native scheduler system on Kubernetes to evaluate its performance in production environments. Our experimental results demonstrate that ISRTF reduces the average job completion time by up to 19.6%.

## 내 메모


