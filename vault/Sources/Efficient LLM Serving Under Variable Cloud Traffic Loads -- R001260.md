---
type: research-source
item_id: 1260
title: "Efficient LLM Serving Under Variable Cloud Traffic Loads"
source: "openalex"
published: "2026-05-23"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.52783/dxjb.v38.293"
url: "https://doi.org/10.52783/dxjb.v38.293"
generated_by: codex-research-db
aliases:
  - "Efficient LLM Serving Under Variable Cloud Traffic Loads"
topics:
  - "kubernetes"
---

# Efficient LLM Serving Under Variable Cloud Traffic Loads

[원문 열기](https://doi.org/10.52783/dxjb.v38.293)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`XAX23HZC`)
- 발행일: 2026-05-23
- 저자: MD Faruk Abdulla
- 식별자: `doi:10.52783/dxjb.v38.293`

## 요약·초록

Large Language Models (LLMs) have rapidly become core components of modern cloud-based applications, powering services ranging from conversational agents to automated code generation. However, serving LLMs efficiently under unpredictable and variable traffic conditions remains a critical open challenge. Unlike traditional web services, LLM inference is computationally intensive, memory-bound, and highly sensitive to request length variability, making conventional auto-scaling strategies insufficient. This paper presents AdaptServe, a cloud-native LLM serving system designed to handle dynamic traffic loads through intelligent request batching, predictive scaling, and model-tiering strategies. AdaptServe employs a traffic-aware scheduler that continuously monitors incoming request patterns and adjusts GPU resource allocation in real time. Evaluated on real-world traffic traces from production LLM deployments, AdaptServe achieves a 4.2x improvement in throughput, 58% reduction in tail latency, and 34% decrease in cloud serving costs compared to static deployment baselines, while maintaining response quality above acceptable thresholds.

## 내 메모


