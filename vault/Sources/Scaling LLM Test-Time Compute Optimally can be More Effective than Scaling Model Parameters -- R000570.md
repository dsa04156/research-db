---
type: research-source
item_id: 570
title: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
source: "arxiv"
published: "2024-08-06T17:35:05Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2408.03314"
url: "https://arxiv.org/abs/2408.03314v1"
generated_by: codex-research-db
aliases:
  - "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
topics:
  - "self-evolving-harness"
---

# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

[원문 열기](https://arxiv.org/abs/2408.03314v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8IXEVD88`)
- 발행일: 2024-08-06T17:35:05Z
- 저자: Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar
- 식별자: `arxiv:2408.03314`

## 요약·초록

Enabling LLMs to improve their outputs by using more test-time computation is a critical step towards building generally self-improving agents that can operate on open-ended natural language. In this paper, we study the scaling of inference-time computation in LLMs, with a focus on answering the question: if an LLM is allowed to use a fixed but non-trivial amount of inference-time compute, how much can it improve its performance on a challenging prompt? Answering this question has implications not only on the achievable performance of LLMs, but also on the future of LLM pretraining and how one should tradeoff inference-time and pre-training compute. Despite its importance, little research attempted to understand the scaling behaviors of various test-time inference methods. Moreover, current work largely provides negative results for a number of these strategies. In this work, we analyze two primary mechanisms to scale test-time computation: (1) searching against dense, process-based verifier reward models; and (2) updating the model's distribution over a response adaptively, given the prompt at test time. We find that in both cases, the effectiveness of different approaches to scaling test-time compute critically varies depending on the difficulty of the prompt. This observation motivates applying a "compute-optimal" scaling strategy, which acts to most effectively allocate test-time compute adaptively per prompt. Using this compute-optimal strategy, we can improve the efficiency of test-time compute scaling by more than 4x compared to a best-of-N baseline. Additionally, in a FLOPs-matched evaluation, we find that on problems where a smaller base model attains somewhat non-trivial success rates, test-time compute can be used to outperform a 14x larger model.

## 내 메모


