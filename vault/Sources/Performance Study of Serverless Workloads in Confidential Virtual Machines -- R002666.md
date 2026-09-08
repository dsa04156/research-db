---
type: research-source
item_id: 2666
title: "Performance Study of Serverless Workloads in Confidential Virtual Machines"
source: "kurate"
published: "2026-09-03T21:01:13Z"
first_seen: "2026-09-08"
review_status: "pending"
canonical_key: "arxiv:2609.04478"
url: "http://arxiv.org/abs/2609.04478v1"
generated_by: codex-research-db
aliases:
  - "Performance Study of Serverless Workloads in Confidential Virtual Machines"
topics:
  - "cloud-infrastructure"
---

# Performance Study of Serverless Workloads in Confidential Virtual Machines

[원문 열기](http://arxiv.org/abs/2609.04478v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-08|2026-09-08]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- 발행일: 2026-09-03T21:01:13Z
- 저자: Rikesh Niroula, Jianchen Shan, Xiaoning Ding
- 식별자: `arxiv:2609.04478`

## 요약·초록

Confidential serverless computing is rapidly emerg- ing as a critical paradigm for application domains requiring strong confidentiality guarantees, such as healthcare, finance, and machine learning. To enable this paradigm in untrusted cloud environments, Confidential Virtual Machines (CVMs) provide isolation by encrypting the entire guest memory, and thus securing serverless workloads against host-level access and inter- ference. However, the implications of CVMs for serverless systems remain insufficiently understood. This paper presents an empirical study of serverless work- loads in CVMs, systematically covering memory efficiency and runtime overhead on both warm-starts and cold-starts. Our results show that CVMs incur substantial memory overhead because encrypted memory disables cross-VM page deduplication and reduces memory reclaimability, thereby limiting warm- container capacity under a fixed memory budget. Runtime overhead in warm-starts is workload dependent. Workloads with frequent VMEXITs, particularly idle transitions, suffer substantial slowdowns. These slowdowns are further amplified by common serverless deployment practice that couples vCPU allocation to memory size, as higher-memory configurations expose more vCPUs than some functions can use effectively. For cold starts, the study focuses on container creation, a common and major contributor to startup latency. Motivated by the memory-efficiency results, we consider the deployments in which multiple containers of the same function are consolidated within the same CVM to improve efficiency, and show that selectively relaxing certain isolation mechanisms in this setting can substan- tially reduce startup overhead. These results clarify the main performance tradeoffs of confidential serverless computing and suggest practical ways to improve efficiency and latency.

## 내 메모


