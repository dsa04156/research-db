---
type: research-source
item_id: 1211
title: "Evaluating Kubernetes Performance for GenAI Inference: From Automatic Speech Recognition to LLM Summarization"
source: "arxiv"
published: "2026-02-03T15:36:08Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2602.04900"
url: "https://arxiv.org/abs/2602.04900v3"
generated_by: codex-research-db
aliases:
  - "Evaluating Kubernetes Performance for GenAI Inference: From Automatic Speech Recognition to LLM Summarization"
topics:
  - "kubernetes"
---

# Evaluating Kubernetes Performance for GenAI Inference: From Automatic Speech Recognition to LLM Summarization

[원문 열기](https://arxiv.org/abs/2602.04900v3)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`WRD277EC`)
- 발행일: 2026-02-03T15:36:08Z
- 저자: Sai Sindhur Malleni, Raúl Sevilla, Aleksei Vasilevskii, José Castillo Lema, André Bauer
- 식별자: `arxiv:2602.04900`

## 요약·초록

As Generative AI (GenAI), particularly inference, rapidly emerges as a dominant workload category, the Kubernetes ecosystem is proactively evolving to natively support its unique demands. This industry paper demonstrates how emerging Kubernetes-native projects can be combined to deliver the benefits of container orchestration, such as scalability and resource efficiency, to complex AI workflows. We implement and evaluate an illustrative, multi-stage use case consisting of automatic speech recognition and summarization. First, we address batch inference by using Kueue to manage jobs that transcribe audio files with Whisper models and Dynamic Accelerator Slicer (DAS) to increase parallel job execution. Second, we address a discrete online inference scenario by feeding the transcripts to a Large Language Model for summarization hosted using llm-d, a novel solution utilizing the recent developments around the Kubernetes Gateway API Inference Extension (GAIE) for optimized routing of inference requests. Our findings illustrate that these complementary components (Kueue, DAS, and GAIE) form a cohesive, high-performance platform, proving Kubernetes' capability to serve as a unified foundation for demanding GenAI workloads: Kueue reduced total makespan by up to 15%; DAS shortened mean job completion time by 36\%; and GAIE working in conjunction with llm-d improved tail Time to First Token latency by up to 90% even under high loads.

## 내 메모


