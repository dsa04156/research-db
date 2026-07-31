---
type: research-source
item_id: 6
title: "Living-Harness Is an Interactive-Agent Evolver"
source: "arxiv"
published: "2026-07-29T08:20:11Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26598"
url: "https://arxiv.org/abs/2607.26598v1"
generated_by: codex-research-db
aliases:
  - "Living-Harness Is an Interactive-Agent Evolver"
topics:
  - "self-evolving-harness"
---

# Living-Harness Is an Interactive-Agent Evolver

[원문 열기](https://arxiv.org/abs/2607.26598v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`P2HA8WTV`)
- 발행일: 2026-07-29T08:20:11Z
- 저자: Yuetian Du, Yucheng Wang, He Xu, Jiexu Xu, Shanwen Tan, Bing Zhao, Boyu Yang, Zhijie Xu, Ming Kong, Hu Wei, Jie Liu, Qiang Zhu
- 식별자: `arxiv:2607.26598`

## 요약·초록

Large language model (LLM) agents may recover from a failure within an episode or after a retry, yet the same execution failure can recur in later tasks because post-episode feedback rarely revises the persistent harness that guides future interactions. Static harnesses improve reliability through fixed tools, context, memory, and workflow structures, but remain unchanged after deployment. We propose $\textbf{Living-Harness}$, a self-evolving agent harness that converts each completed trajectory and its evaluator signals into posterior evidence for bounded harness updates. Guided by a domain-level $\textbf{Evolution-SOP}$ ($\textbf{S}$tandard $\textbf{O}$perating $\textbf{P}$rocedure), Living-Harness extracts an episode abstraction and structured update evidence, and writes two complementary forms of procedural knowledge: episodic memory that records trigger conditions, failure patterns, and recovery actions, and a state graph that records state nodes, repair edges, and transition rules. The updated harness state is retrieved to guide future interactions, while tools and base context remain frozen, allowing procedural repairs to accumulate across evolution cycles. On eight interactive environments derived from $τ^2$-Bench and MultiWOZ-2.4, Living-Harness improves average Pass@1 over the strongest interactive baseline by 10.07 and 9.91 percentage points, respectively, and supports retrieval-only reuse of the evolved harness state across model backbones.

## 내 메모


