---
type: research-source
item_id: 313
title: "Mutiny! How does Kubernetes fail, and what can we do about it?"
source: "arxiv"
published: "2024-04-17T08:38:04Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/dsn58291.2024.00016"
url: "https://arxiv.org/abs/2404.11169v1"
generated_by: codex-research-db
aliases:
  - "Mutiny! How does Kubernetes fail, and what can we do about it?"
topics:
  - "kubernetes"
---

# Mutiny! How does Kubernetes fail, and what can we do about it?

[원문 열기](https://arxiv.org/abs/2404.11169v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SICI3KXR`)
- 발행일: 2024-04-17T08:38:04Z
- 저자: Marco Barletta, Marcello Cinque, Catello Di Martino, Zbigniew T. Kalbarczyk, Ravishankar K. Iyer
- 식별자: `doi:10.1109/dsn58291.2024.00016`

## 요약·초록

In this paper, we i) analyze and classify real-world failures of Kubernetes (the most popular container orchestration system), ii) develop a framework to perform a fault/error injection campaign targeting the data store preserving the cluster state, and iii) compare results of our fault/error injection experiments with real-world failures, showing that our fault/error injections can recreate many real-world failure patterns. The paper aims to address the lack of studies on systematic analyses of Kubernetes failures to date. Our results show that even a single fault/error (e.g., a bit-flip) in the data stored can propagate, causing cluster-wide failures (3% of injections), service networking issues (4%), and service under/overprovisioning (24%). Errors in the fields tracking dependencies between object caused 51% of such cluster-wide failures. We argue that controlled fault/error injection-based testing should be employed to proactively assess Kubernetes' resiliency and guide the design of failure mitigation strategies.

## 내 메모


