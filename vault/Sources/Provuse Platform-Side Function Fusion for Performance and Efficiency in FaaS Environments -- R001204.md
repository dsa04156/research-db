---
type: research-source
item_id: 1204
title: "Provuse: Platform-Side Function Fusion for Performance and Efficiency in FaaS Environments"
source: "arxiv"
published: "2026-03-06T11:28:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.06170"
url: "https://arxiv.org/abs/2603.06170v2"
generated_by: codex-research-db
aliases:
  - "Provuse: Platform-Side Function Fusion for Performance and Efficiency in FaaS Environments"
topics:
  - "kubernetes"
---

# Provuse: Platform-Side Function Fusion for Performance and Efficiency in FaaS Environments

[원문 열기](https://arxiv.org/abs/2603.06170v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TZ9MEFZ9`)
- 발행일: 2026-03-06T11:28:40Z
- 저자: Niklas Kowallik, Natalie Carl, Leon Pöllinger, Wei Wang, Sharan Santhanam, David Bermbach
- 식별자: `arxiv:2603.06170`

## 요약·초록

Function-as-a-Service (FaaS) platforms provide scalable and cost-efficient execution but suffer from increased latency and resource overheads in complex applications comprising multiple functions, particularly due to double billing when functions call each other. This paper presents Provuse, a transparent, platform-side optimization that automatically performs function fusion at runtime for independently deployed functions, thereby eliminating redundant function instances. This approach reduces both cost and latency without requiring users to change any code. Provusetargets provider-managed FaaS platforms that retain control over function entry points and deployment artifacts, enabling transparent, runtime execution consolidation without developer intervention. We provide two implementations for this approach using the tinyFaaS platform as well as Kubernetes, demonstrating compatibility with container orchestration frameworks. An evaluation shows consistent improvements, achieving an average end-to-end latency reduction of 26.33% and a mean RAM usage reduction of 53.57%. These results indicate that automatic function fusion is an effective platform-side strategy for reducing latency and RAM consumption in composed FaaS applications, highlighting the potential of transparent infrastructure-level optimizations in serverless systems.

## 내 메모


