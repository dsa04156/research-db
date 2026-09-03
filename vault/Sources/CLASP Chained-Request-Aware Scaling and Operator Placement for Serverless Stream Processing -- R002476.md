---
type: research-source
item_id: 2476
title: "CLASP: Chained-Request-Aware Scaling and Operator Placement for Serverless Stream Processing"
source: "kurate"
published: "2026-08-29T07:19:48Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.29103"
url: "http://arxiv.org/abs/2608.29103v1"
generated_by: codex-research-db
aliases:
  - "CLASP: Chained-Request-Aware Scaling and Operator Placement for Serverless Stream Processing"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# CLASP: Chained-Request-Aware Scaling and Operator Placement for Serverless Stream Processing

[원문 열기](http://arxiv.org/abs/2608.29103v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- Zotero: created (`GNSASI7F`)
- 발행일: 2026-08-29T07:19:48Z
- 저자: Tianyu Qi, Maria A. Rodriguez, Rajkumar Buyya
- 식별자: `arxiv:2608.29103`

## 요약·초록

Stateful serverless (Function-as-a-Service) environments, whose workers host state servers, are increasingly used for stream processing. A stream application is a pipeline of operators, where each operator forwards intermediate data downstream through a chained request. As input rates fluctuate, the system should adjust operator parallelism and place instances across workers to sustain the incoming rate. Existing approaches do so without fully accounting for chained-request overhead, leading them to misestimate the required number of workers. Too few leave the cluster unable to keep up with the input rate, while too many route a larger fraction of chained requests across worker boundaries, increasing end-to-end latency. We propose CLASP, a scaling and scheduling strategy for stream processing in stateful serverless environments. At runtime, CLASP estimates execution cost and chained-request cost from observed metrics. Under a capacity model that covers the two costs, it adjusts operator parallelism and packs operators onto the fewest workers that can sustain the target input rate. Once a scaling decision is made, CLASP migrates each operator's state together with its instances, thereby minimizing execution pause time. Experiments show that CLASP improves throughput by up to 3.3x and reduces median end-to-end latency by up to 76% compared with state-of-the-art scaling strategies.

## 내 메모


