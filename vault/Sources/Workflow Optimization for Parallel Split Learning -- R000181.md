---
type: research-source
item_id: 181
title: "Workflow Optimization for Parallel Split Learning"
source: "arxiv"
published: "2024-02-01T14:16:10Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/infocom52122.2024.10621348"
url: "https://arxiv.org/abs/2402.10092v1"
generated_by: codex-research-db
aliases:
  - "Workflow Optimization for Parallel Split Learning"
topics:
  - "self-evolving-harness"
---

# Workflow Optimization for Parallel Split Learning

[원문 열기](https://arxiv.org/abs/2402.10092v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MA6QH4ZN`)
- 발행일: 2024-02-01T14:16:10Z
- 저자: Joana Tirana, Dimitra Tsigkari, George Iosifidis, Dimitris Chatzopoulos
- 식별자: `doi:10.1109/infocom52122.2024.10621348`

## 요약·초록

Split learning (SL) has been recently proposed as a way to enable resource-constrained devices to train multi-parameter neural networks (NNs) and participate in federated learning (FL). In a nutshell, SL splits the NN model into parts, and allows clients (devices) to offload the largest part as a processing task to a computationally powerful helper. In parallel SL, multiple helpers can process model parts of one or more clients, thus, considerably reducing the maximum training time over all clients (makespan). In this paper, we focus on orchestrating the workflow of this operation, which is critical in highly heterogeneous systems, as our experiments show. In particular, we formulate the joint problem of client-helper assignments and scheduling decisions with the goal of minimizing the training makespan, and we prove that it is NP-hard. We propose a solution method based on the decomposition of the problem by leveraging its inherent symmetry, and a second one that is fully scalable. A wealth of numerical evaluations using our testbed's measurements allow us to build a solution strategy comprising these methods. Moreover, we show that this strategy finds a near-optimal solution, and achieves a shorter makespan than the baseline scheme by up to 52.3%.

## 내 메모


