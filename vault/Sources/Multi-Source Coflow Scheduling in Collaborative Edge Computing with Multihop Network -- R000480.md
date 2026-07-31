---
type: research-source
item_id: 480
title: "Multi-Source Coflow Scheduling in Collaborative Edge Computing with Multihop Network"
source: "arxiv"
published: "2024-05-29T14:41:57Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2405.19136"
url: "https://arxiv.org/abs/2405.19136v1"
generated_by: codex-research-db
aliases:
  - "Multi-Source Coflow Scheduling in Collaborative Edge Computing with Multihop Network"
topics:
  - "edge-computing"
---

# Multi-Source Coflow Scheduling in Collaborative Edge Computing with Multihop Network

[원문 열기](https://arxiv.org/abs/2405.19136v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`A325HU3N`)
- 발행일: 2024-05-29T14:41:57Z
- 저자: Yuvraj Sahni, Jiannong Cao, Lei Yang, Shengwei Wang
- 식별자: `arxiv:2405.19136`

## 요약·초록

Collaborative edge computing has become a popular paradigm where edge devices collaborate by sharing resources. Data dissemination is a fundamental problem in CEC to decide what data is transmitted from which device and how. Existing works on data dissemination have not focused on coflow scheduling in CEC, which involves deciding the order of flows within and across coflows at network links. Coflow implies a set of parallel flows with a shared objective. The existing works on coflow scheduling in data centers usually assume a non-blocking switch and do not consider congestion at different links in the multi-hop path in CEC, leading to increased coflow completion time (CCT). Furthermore, existing works do not consider multiple flow sources that cannot be ignored, as data can have duplicate copies at different edge devices. This work formulates the multi-source coflow scheduling problem in CEC, which includes jointly deciding the source and flow ordering for multiple coflows to minimize the sum of CCT. This problem is shown to be NP-hard and challenging as each flow can have multiple dependent conflicts at multiple links. We propose a source and coflow-aware search and adjust (SCASA) heuristic that first provides an initial solution considering the coflow characteristics. SCASA further improves the initial solution using the source search and adjust heuristic by leveraging the knowledge of both coflows and network congestion at links. Evaluation done using simulation experiments shows that SCASA leads to up to 83% reduction in the sum of CCT compared to benchmarks without a joint solution.

## 내 메모


