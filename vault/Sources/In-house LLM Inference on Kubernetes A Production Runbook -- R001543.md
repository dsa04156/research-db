---
type: research-source
item_id: 1543
title: "In-house LLM Inference on Kubernetes: A Production Runbook"
source: "social:reddit"
published: "2026-07-29"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:210b524d499e5483a5960db73d8ad43c00b13d0c35166ef4e55b431bdcf78196"
url: "https://www.reddit.com/r/kubernetes/comments/1v9msqf/inhouse_llm_inference_on_kubernetes_a_production/"
generated_by: codex-research-db
aliases:
  - "In-house LLM Inference on Kubernetes: A Production Runbook"
topics:
  - "kubernetes"
---

# In-house LLM Inference on Kubernetes: A Production Runbook

> [!warning] SNS 탐색 신호
> 원문이나 1차 자료를 확인하기 전에는 근거로 인용하지 않습니다.

[원문 열기](https://www.reddit.com/r/kubernetes/comments/1v9msqf/inhouse_llm_inference_on_kubernetes_a_production/)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `social:reddit`
- 검토 상태: `pending`
- 발행일: 2026-07-29
- 식별자: `url:210b524d499e5483a5960db73d8ad43c00b13d0c35166ef4e55b431bdcf78196`

## 요약·초록

Great stuff, I just did something really similar, but instead I am using the vllm production-stack and I am using way smaller 8B models, my use case is for a small naming validation task. I didnt know about Bifrost and I will start looking into it. Thanks for sharing I think that the extremely laggy website is not the place to post static text+image only pages. Also doing this at a large scale(200+ nodes and 1700+ accelerators) at a university, and created https://github.com/thediymaker/obleth-gateway specifically to handle self hosted ai inference. Provides some cool features that only make sense for self hosted infrastructure.

## 내 메모


