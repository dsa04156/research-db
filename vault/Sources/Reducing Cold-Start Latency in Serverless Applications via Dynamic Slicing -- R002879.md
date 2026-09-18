---
type: research-source
item_id: 2879
title: "Reducing Cold-Start Latency in Serverless Applications via Dynamic Slicing"
source: "kurate"
published: "2026-09-12T16:49:58Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.14040"
url: "http://arxiv.org/abs/2609.14040v1"
generated_by: codex-research-db
aliases:
  - "Reducing Cold-Start Latency in Serverless Applications via Dynamic Slicing"
topics:
  - "cloud-infrastructure"
---

# Reducing Cold-Start Latency in Serverless Applications via Dynamic Slicing

[원문 열기](http://arxiv.org/abs/2609.14040v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- Zotero: created (`GZB7686B`)
- 발행일: 2026-09-12T16:49:58Z
- 저자: Georgios Alexopoulos, Konstantinos Karakatsanis, Nikolaos Alexopoulos, Dimitris Mitropoulos, Thodoris Sotiropoulos
- 식별자: `arxiv:2609.14040`

## 요약·초록

We present PyXtrim, a system that reduces the cold-start latency of serverless applications through debloating. We focus on Python, a dominant language for serverless applications whose dynamic features and extensive use of native extensions make traditional static debloating particularly challenging. PyXtrim frames debloating as a dynamic slicing problem, using the application's externally visible behavior as the slicing criterion. Everything outside the resulting slice is removed, both from the application and its dependencies. Our key technical contribution is that the slice is computed by a cross-language dynamic dependence engine that tracks data and control dependences across Python and native code and identifies operations that interact with the operating system, which form the slicing criterion. As a result, PyXtrim can effectively handle real-world applications that rely on dynamic features such as reflection, interoperate with native code and interact with system resources. Across 31 applications on AWS Lambda, PyXtrim reduces cold-start latency by 21.7% and peak memory usage by 17.1% at the median. This is more than double the reduction achieved by the state of the art, while debloating each application in minutes.

## 내 메모
