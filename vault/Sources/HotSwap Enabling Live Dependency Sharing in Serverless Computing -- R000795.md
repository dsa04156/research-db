---
type: research-source
item_id: 795
title: "HotSwap: Enabling Live Dependency Sharing in Serverless Computing"
source: "arxiv"
published: "2024-09-13T21:31:45Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2409.09202"
url: "https://arxiv.org/abs/2409.09202v3"
generated_by: codex-research-db
aliases:
  - "HotSwap: Enabling Live Dependency Sharing in Serverless Computing"
topics:
  - "cloud-infrastructure"
---

# HotSwap: Enabling Live Dependency Sharing in Serverless Computing

[원문 열기](https://arxiv.org/abs/2409.09202v3)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KTQJ95Q6`)
- 발행일: 2024-09-13T21:31:45Z
- 저자: Rui Li, Devesh Tiwari, Gene Cooperman
- 식별자: `arxiv:2409.09202`

## 요약·초록

This work presents HotSwap, a novel provider-side cold-start optimization for serverless computing. This optimization reduces cold-start time when booting and loading dependencies at runtime inside a function container. Previous research has extensively focused on reducing cold-start latency for specific functions. However, little attention has been given to skewed production workloads. In such cases, cross-function optimization becomes essential. Without cross-function optimization, a cloud provider is left with two equally poor options: (i) Either the cloud provider gives up optimization for each function in the long tail (which is slow); or (ii) the cloud provider applies function-specific optimizations (e.g., cache function images) to every function in the long tail (which violates the vendor's cache constraints). HotSwap demonstrates cross-function optimization using a novel pre-warming strategy. In this strategy, a pre-initialized live dependency image is migrated to the new function instance. At the same time, HotSwap respects the provider's cache constraints, because a single pre-warmed dependency image in the cache can be shared among all serverless functions that require that image. HotSwap has been tested on seven representative functions from FunctionBench. In those tests, HotSwap accelerates dependency loading for those serverless functions with large dependency requirements by a factor ranging from 2.2 to 3.2. Simulation experiments using Azure traces indicate that HotSwap can save 88\% of space, compared with a previous function-specific method, PreBaking, when sharing a dependency image among ten different functions.

## 내 메모


