---
type: research-source
item_id: 312
title: "Dirigent: Lightweight Serverless Orchestration"
source: "arxiv"
published: "2024-04-25T08:01:11Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3694715.3695966"
url: "https://arxiv.org/abs/2404.16393v3"
generated_by: codex-research-db
aliases:
  - "Dirigent: Lightweight Serverless Orchestration"
topics:
  - "cloud-infrastructure"
  - "kubernetes"
---

# Dirigent: Lightweight Serverless Orchestration

[원문 열기](https://arxiv.org/abs/2404.16393v3)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`K5IVAWVB`)
- 발행일: 2024-04-25T08:01:11Z
- 저자: Lazar Cvetković, François Costa, Mihajlo Djokic, Michal Friedman, Ana Klimovic
- 식별자: `doi:10.1145/3694715.3695966`

## 요약·초록

While Function as a Service (FaaS) platforms can initialize function sandboxes on worker nodes in 10-100s of milliseconds, the latency to schedule functions in real FaaS clusters can be orders of magnitude higher. The current approach of building FaaS cluster managers on top of legacy orchestration systems (e.g., Kubernetes) leads to high scheduling delays when clusters experience high sandbox churn, which is common for FaaS. Generic cluster managers use many hierarchical abstractions and internal components to manage and reconcile cluster state with frequent persistent updates. This becomes a bottleneck for FaaS since the cluster state frequently changes as sandboxes are created on the critical path of requests. Based on our root cause analysis of performance issues in existing FaaS cluster managers, we propose Dirigent, a clean-slate system architecture for FaaS orchestration with three key principles. First, Dirigent optimizes internal cluster manager abstractions to simplify state management. Second, it eliminates persistent state updates on the critical path of function invocations, leveraging the fact that FaaS abstracts sandbox locations from users to relax exact state reconstruction guarantees. Finally, Dirigent runs monolithic control and data planes to minimize internal communication overheads and maximize throughput. We compare Dirigent to state-of-the-art FaaS platforms and show that Dirigent reduces 99th percentile per-function scheduling latency for a production workload by 2.79x compared to AWS Lambda. Dirigent can spin up 2500 sandboxes per second at low latency, which is 1250x more than Knative.

## 내 메모


