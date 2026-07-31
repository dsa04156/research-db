---
type: research-source
item_id: 327
title: "Mutating etcd Towards Edge Suitability"
source: "arxiv"
published: "2023-11-16T14:31:16Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2311.09929"
url: "https://arxiv.org/abs/2311.09929v1"
generated_by: codex-research-db
aliases:
  - "Mutating etcd Towards Edge Suitability"
topics:
  - "kubernetes"
---

# Mutating etcd Towards Edge Suitability

[원문 열기](https://arxiv.org/abs/2311.09929v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UGGJWX5H`)
- 발행일: 2023-11-16T14:31:16Z
- 저자: Andrew Jeffery, Heidi Howard, Richard Mortier
- 식별자: `arxiv:2311.09929`

## 요약·초록

In the edge environment servers are no longer being co-located away from clients, instead they are being co-located with clients away from other servers, focusing on reliable and performant operation. Orchestration platforms, such as Kubernetes, are a key system being transitioned to the edge but they remain unsuited to the environment, stemming primarily from their critical key-value stores. In this work we derive requirements from the edge environment showing that, fundamentally, the design of distributed key-value datastores, such as etcd, is unsuited to meet them. Using these requirements, we explore the design space for distributed key-value datastores and implement two successive mutations of etcd for different points: mergeable-etcd and dismerge, trading linearizability for causal consistency based on CRDTs. mergeable-etcd retains the linear revision history but encounters inherent shortcomings, whilst dismerge embraces the causal model. Both stores are local-first, maintaining reliable performance under network partitions and variability, drastically surpassing etcd's performance, whilst maintaining competitive performance in reliable settings.

## 내 메모


