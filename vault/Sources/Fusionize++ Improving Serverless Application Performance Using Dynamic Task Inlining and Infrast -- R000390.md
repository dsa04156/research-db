---
type: research-source
item_id: 390
title: "Fusionize++: Improving Serverless Application Performance Using Dynamic Task Inlining and Infrastructure Optimization"
source: "arxiv"
published: "2023-11-08T18:22:42Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/tcc.2024.3451108"
url: "https://arxiv.org/abs/2311.04875v2"
generated_by: codex-research-db
aliases:
  - "Fusionize++: Improving Serverless Application Performance Using Dynamic Task Inlining and Infrastructure Optimization"
topics:
  - "cloud-infrastructure"
---

# Fusionize++: Improving Serverless Application Performance Using Dynamic Task Inlining and Infrastructure Optimization

[원문 열기](https://arxiv.org/abs/2311.04875v2)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8IWXHXCX`)
- 발행일: 2023-11-08T18:22:42Z
- 저자: Trever Schirmer, Joel Scheuner, Tobias Pfandzelter, David Bermbach
- 식별자: `doi:10.1109/tcc.2024.3451108`

## 요약·초록

The Function-as-a-Service (FaaS) execution model increases developer productivity by removing operational concerns such as managing hardware or software runtimes. Developers, however, still need to partition their applications into FaaS functions, which is error-prone and complex: Encapsulating only the smallest logical unit of an application as a FaaS function maximizes flexibility and reusability. Yet, it also leads to invocation overheads, additional cold starts, and may increase cost due to double billing during synchronous invocations. Conversely, deploying an entire application as a single FaaS function avoids these overheads but decreases flexibility. In this paper we present Fusionize, a framework that automates optimizing for this trade-off by automatically fusing application code into an optimized multi-function composition. Developers only need to write fine-grained application code following the serverless model, while Fusionize automatically fuses different parts of the application into FaaS functions, manages their interactions, and configures the underlying infrastructure. At runtime, it monitors application performance and adapts it to minimize request-response latency and costs. Real-world use cases show that Fusionize can improve the deployment artifacts of the application, reducing both median request-response latency and cost of an example IoT application by more than 35%.

## 내 메모


