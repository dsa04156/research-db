---
type: research-source
item_id: 2737
title: "Beyond Prompts: Measuring and Optimizing LLM Tool-Agent Harnesses"
source: "arxiv"
published: "2026-09-04T21:35:00Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.05736"
url: "https://arxiv.org/abs/2609.05736v2"
generated_by: codex-research-db
aliases:
  - "Beyond Prompts: Measuring and Optimizing LLM Tool-Agent Harnesses"
topics:
  - "self-evolving-harness"
---

# Beyond Prompts: Measuring and Optimizing LLM Tool-Agent Harnesses

[원문 열기](https://arxiv.org/abs/2609.05736v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`P7N2DVVM`)
- 발행일: 2026-09-04T21:35:00Z
- 저자: Cen Mia Zhao, Haibo Ruan, Wenjie Chen, Pei-fen Tu, Usman Abbasi, Joel Hesch
- 식별자: `arxiv:2609.05736`

## 요약·초록

LLM tool agents can be improved without retraining by modifying the runtime harness around a fixed model: prompts, tool interfaces, middleware, state handling, and recovery logic. We study this setting as resource-bounded harness selection for fixed-model multi-turn tool agents, with the search surface scoped to prompts and tool-boundary middleware: edits are guarded intercepts at the tool boundary, not arbitrary rewriting of agent execution logic. Our optimizer-agnostic protocol reports mean held-out lift, worst-condition lift, repeatability, logged cost diagnostics, and RelLift95(B), a conservative estimate of the held-out gain of the harness selected under budget B. We instantiate the protocol with prompt-only and prompt-plus-middleware optimizers, including PRISM, which clusters failures and routes repairs to prompt, tool-boundary middleware, or joint edit surfaces within a Pareto search. On BFCL multi-round, tau2-Retail, and tau2-Telecom, PRISM obtains mean held-out lifts of 14.2, 14.9, and 10.1 percentage points and positive empirical RelLift95 on all three benchmarks, and a component ablation attributes the margin chiefly to failure-surface routing and the edit-pattern constraint. Across optimizers, the results show that some search procedures can occasionally find large gains but still choose brittle updates, so the reliability of the chosen harness should be reported alongside average held-out lift.

## 내 메모


