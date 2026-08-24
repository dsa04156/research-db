---
type: research-source
item_id: 2160
title: "Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection"
source: "arxiv"
published: "2026-08-20T15:24:54Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.20169"
url: "https://arxiv.org/abs/2608.20169v1"
generated_by: codex-research-db
aliases:
  - "Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection"
topics:
  - "self-evolving-harness"
---

# Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selection

[원문 열기](https://arxiv.org/abs/2608.20169v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-20T15:24:54Z
- 저자: Atsuyuki Miyai, Kiyoharu Aizawa, Toshihiko Yamasaki
- 식별자: `arxiv:2608.20169`

## 요약·초록

We present a novel approach to efficient LLM agent harness optimization through adaptive validation task selection. Harness optimization iteratively rewrites the harness code based on validation performance, enabling substantial performance gains without updating the underlying model weights. Existing approaches, however, evaluate a fixed validation set in full at every iteration, incurring substantial evaluation costs even on tasks that become less discriminative as the harness evolves. We propose $\textbf{Task-CoEvolve}$, which co-evolves the validation tasks with the harness by addressing two challenges: selecting informative tasks and estimating full-set performance from partial evaluations. Task-CoEvolve builds on the observation that tasks on which candidate harnesses disagree are more informative for distinguishing among them than tasks that are consistently solved or failed. It uses variance-weighted sampling based on past outcomes to focus evaluation on tasks near the agent's capability frontier, with the sampling distribution adapting as the harness evolves. It then estimates full-set scores from the sampled tasks by accounting for their sampling probabilities, enabling consistent comparisons across iterations despite evaluating different subsets. Experiments on online text classification and Terminal-Bench 2.1 show that Task-CoEvolve consistently outperforms fixed-subset baselines and matches the final performance of full-set search while reducing the number of evaluations during optimization by 80%. Code will be released at https://github.com/Agent4Science-UTokyo/Task-CoEvolve.

## 내 메모


