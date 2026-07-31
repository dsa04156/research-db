---
type: research-source
item_id: 987
title: "Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0"
source: "arxiv"
published: "2026-07-15T16:36:04Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.14004"
url: "https://arxiv.org/abs/2607.14004v1"
generated_by: codex-research-db
aliases:
  - "Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0"
topics:
  - "self-evolving-harness"
---

# Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0

[원문 열기](https://arxiv.org/abs/2607.14004v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`65BPP4NN`)
- 발행일: 2026-07-15T16:36:04Z
- 저자: Wenxiao Wang, Priyatham Kattakinda, Soheil Feizi
- 식별자: `arxiv:2607.14004`

## 요약·초록

Most reported gains from agent-optimization methods are one-shot: an agent is optimized against a fixed benchmark and the resulting improvement is reported as if it were a stable property of the method. This does not test the setting that matters for deployed agents, where optimization is applied recursively as new failures and new tasks appear over time. The central question this raises is whether optimizer-driven gains compound: after an agent has been optimized once, can it be optimized again on newly arrived tasks without eroding the gains the first round produced? We study this question with a two-phase continual-learning evaluation built from hard tasks in Terminal-Bench 2.0, comparing three approaches to agent-harness optimization (GEPA, Meta Harness, and RELAI's Verifiable Continual Learning, RELAI-VCL) under identical optimization budgets. All three methods improve over the baseline agent in the conventional, static, single-phase setting. However, once new tasks are introduced, the methods diverge sharply: GEPA's optimized agent transfers below the unoptimized baseline, Meta Harness transfers well but fails to improve further once given a second optimization budget, and RELAI-VCL is the only method that both transfers positively to unseen tasks and continues improving after those tasks are folded into the optimization objective, reaching the highest pass rate at every evaluated stage and the highest lifelong average pass rate overall (76.4% vs. 66.0% for GEPA, 64.6% for Meta Harness, and 58.7% for the baseline). Our key observation was that optimization gains compounded only when regression control was built into the optimization loop, providing an inductive bias against shortcut solutions that fail to generalize.

## 내 메모


