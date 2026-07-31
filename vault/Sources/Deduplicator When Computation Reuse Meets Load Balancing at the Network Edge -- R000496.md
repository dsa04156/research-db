---
type: research-source
item_id: 496
title: "Deduplicator: When Computation Reuse Meets Load Balancing at the Network Edge"
source: "arxiv"
published: "2024-05-04T14:48:19Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2405.02682"
url: "https://arxiv.org/abs/2405.02682v1"
generated_by: codex-research-db
aliases:
  - "Deduplicator: When Computation Reuse Meets Load Balancing at the Network Edge"
topics:
  - "edge-computing"
---

# Deduplicator: When Computation Reuse Meets Load Balancing at the Network Edge

[원문 열기](https://arxiv.org/abs/2405.02682v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RVDE2THU`)
- 발행일: 2024-05-04T14:48:19Z
- 저자: Md Washik Al Azad, Spyridon Mastorakis
- 식별자: `arxiv:2405.02682`

## 요약·초록

Load balancing has been a fundamental building block of cloud and, more recently, edge computing environments. At the same time, in edge computing environments, prior research has highlighted that applications operate on similar (correlated) data. Based on this observation, prior research has advocated for the direction of "computation reuse", where the results of previously executed computational tasks are stored at the edge and are reused (if possible) to satisfy incoming tasks with similar input data, instead of executing incoming tasks from scratch. Both load balancing and computation reuse are critical to the deployment of scalable edge computing environments, yet they are contradictory in nature. In this paper, we propose the Deduplicator, a middlebox that aims to facilitate both load balancing and computation reuse at the edge. The Deduplicator features mechanisms to identify and deduplicate similar tasks offloaded by user devices, collect information about the usage of edge servers' resources, manage the addition of new edge servers and the failures of existing edge servers, and ultimately balance the load imposed on edge servers. Our evaluation results demonstrate that the Deduplicator achieves up to 20% higher percentages of computation reuse compared to several other load balancing approaches, while also effectively balancing the distribution of tasks among edge servers at line rate.

## 내 메모


