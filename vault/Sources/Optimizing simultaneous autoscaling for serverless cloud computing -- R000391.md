---
type: research-source
item_id: 391
title: "Optimizing simultaneous autoscaling for serverless cloud computing"
source: "arxiv"
published: "2023-10-29T14:00:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2310.19013"
url: "https://arxiv.org/abs/2310.19013v1"
generated_by: codex-research-db
aliases:
  - "Optimizing simultaneous autoscaling for serverless cloud computing"
topics:
  - "cloud-infrastructure"
---

# Optimizing simultaneous autoscaling for serverless cloud computing

[원문 열기](https://arxiv.org/abs/2310.19013v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TCVWSDMP`)
- 발행일: 2023-10-29T14:00:41Z
- 저자: Harold Ship, Evgeny Shindin, Chen Wang, Diana Arroyo, Asser Tantawi
- 식별자: `arxiv:2310.19013`

## 요약·초록

This paper explores resource allocation in serverless cloud computing platforms and proposes an optimization approach for autoscaling systems. Serverless computing relieves users from resource management tasks, enabling focus on application functions. However, dynamic resource allocation and function replication based on changing loads remain crucial. Typically, autoscalers in these platforms utilize threshold-based mechanisms to adjust function replicas independently. We model applications as interconnected graphs of functions, where requests probabilistically traverse the graph, triggering associated function execution. Our objective is to develop a control policy that optimally allocates resources on servers, minimizing failed requests and response time in reaction to load changes. Using a fluid approximation model and Separated Continuous Linear Programming (SCLP), we derive an optimal control policy that determines the number of resources per replica and the required number of replicas over time. We evaluate our approach using a simulation framework built with Python and simpy. Comparing against threshold-based autoscaling, our approach demonstrates significant improvements in average response times and failed requests, ranging from 15% to over 300% in most cases. We also explore the impact of system and workload parameters on performance, providing insights into the behavior of our optimization approach under different conditions. Overall, our study contributes to advancing resource allocation strategies, enhancing efficiency and reliability in serverless cloud computing platforms.

## 내 메모


