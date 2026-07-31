---
type: research-source
item_id: 786
title: "Enabling Efficient Serverless Inference Serving for LLM (Large Language Model) in the Cloud"
source: "arxiv"
published: "2024-11-23T22:19:37Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2411.15664"
url: "https://arxiv.org/abs/2411.15664v1"
generated_by: codex-research-db
aliases:
  - "Enabling Efficient Serverless Inference Serving for LLM (Large Language Model) in the Cloud"
topics:
  - "cloud-infrastructure"
---

# Enabling Efficient Serverless Inference Serving for LLM (Large Language Model) in the Cloud

[원문 열기](https://arxiv.org/abs/2411.15664v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HGSHDVHE`)
- 발행일: 2024-11-23T22:19:37Z
- 저자: Himel Ghosh
- 식별자: `arxiv:2411.15664`

## 요약·초록

This review report discusses the cold start latency in serverless inference and existing solutions. It particularly reviews the ServerlessLLM method, a system designed to address the cold start problem in serverless inference for large language models. Traditional serverless approaches struggle with high latency due to the size of LLM checkpoints and the overhead of initializing GPU resources. ServerlessLLM introduces a multitier checkpoint loading system, leveraging underutilized GPU memory and storage to reduce startup times by 6--8x compared to existing methods. It also proposes live inference migration and a startup-time-optimized model scheduler, ensuring efficient resource allocation and minimizing delays. This system significantly improves performance and scalability in serverless environments for LLM workloads. Besides ServerlessLLM, several other methods from recent research literature, including Rainbowcake, are reviewed in this paper. Further discussions explore how FaaS providers tackle cold starts and the possible future scopes.

## 내 메모


