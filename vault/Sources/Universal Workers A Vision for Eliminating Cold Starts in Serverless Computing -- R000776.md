---
type: research-source
item_id: 776
title: "Universal Workers: A Vision for Eliminating Cold Starts in Serverless Computing"
source: "arxiv"
published: "2025-05-26T12:06:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/cloud67622.2025.00051"
url: "https://arxiv.org/abs/2505.19880v2"
generated_by: codex-research-db
aliases:
  - "Universal Workers: A Vision for Eliminating Cold Starts in Serverless Computing"
topics:
  - "cloud-infrastructure"
---

# Universal Workers: A Vision for Eliminating Cold Starts in Serverless Computing

[원문 열기](https://arxiv.org/abs/2505.19880v2)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`D48KE9UT`)
- 발행일: 2025-05-26T12:06:12Z
- 저자: Saman Akbari, Manfred Hauswirth
- 식별자: `doi:10.1109/cloud67622.2025.00051`

## 요약·초록

Serverless computing enables developers to deploy code without managing infrastructure, but suffers from cold start overhead when initializing new function instances. Existing solutions such as "keep-alive" or "pre-warming" are costly and unreliable under bursty workloads. We propose universal workers, which are computational units capable of executing any function with minimal initialization overhead. Based on an analysis of production workload traces, our key insight is that requests in Function-as-a-Service (FaaS) platforms show a highly skewed distribution, with most requests invoking a small subset of functions. We exploit this observation to approximate universal workers through locality groups and three-tier caching (handler, install, import). With this work, we aim to enable more efficient and scalable FaaS platforms capable of handling diverse workloads with minimal initialization overhead.

## 내 메모


