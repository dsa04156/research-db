---
type: research-source
item_id: 1749
title: "Learning-Based Collaborative MEC for LLM Inference with Soft-Deadline Awareness via Transformer-Enhanced PPO"
source: "arxiv"
published: "2026-08-03T10:27:25Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.02031"
url: "https://arxiv.org/abs/2608.02031v1"
generated_by: codex-research-db
aliases:
  - "Learning-Based Collaborative MEC for LLM Inference with Soft-Deadline Awareness via Transformer-Enhanced PPO"
topics:
  - "edge-computing"
---

# Learning-Based Collaborative MEC for LLM Inference with Soft-Deadline Awareness via Transformer-Enhanced PPO

[원문 열기](https://arxiv.org/abs/2608.02031v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FPZK75MD`)
- 발행일: 2026-08-03T10:27:25Z
- 저자: Ngoc Hung Nguyen, Bjorn Landfeldt
- 식별자: `arxiv:2608.02031`

## 요약·초록

This paper investigates collaborative mobile edge computing (MEC) servers for large language model (LLM) inference under soft deadline constraints. In this system, to improve the quality of service, computations are expected to be completed within their deadlines. However, due to dependencies among tasks or subtasks, any missed deadline can lead to catastrophic consequences for the entire request. In this context, this work proposes an extended deadline mechanism with constrained flexibility. The main challenges lie in handling large-scale computations under strict latency constraints while limiting the number of allowable deadline extensions, especially in the presence of task dependencies within each request. To tackle these challenges, we develop a transformer-enhanced proximal policy optimization (PPO) framework that enables efficient collaboration among MEC servers. The proposed approach aims to maximize the number of tasks completed within their deadlines while minimizing the use of deadline extensions. By capturing temporal dependencies and cross-server interactions, the transformer improves decision-making for task migration. Simulation results demonstrate that the proposed method significantly outperforms conventional PPO and heuristic-based approaches in terms of task completion rate and overall system efficiency.

## 내 메모


