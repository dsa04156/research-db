---
type: research-source
item_id: 1070
title: "SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems"
source: "arxiv"
published: "2026-07-28T03:55:47Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25255"
url: "https://arxiv.org/abs/2607.25255v1"
generated_by: codex-research-db
aliases:
  - "SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems"
topics:
  - "ai-agents"
---

# SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems

[원문 열기](https://arxiv.org/abs/2607.25255v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3IUCT263`)
- 발행일: 2026-07-28T03:55:47Z
- 저자: Haowen Dai, Zonghao Ying, Wenfeng Li, Xiangfan Wu, Yisong Xiao, Tianyuan Zhang, Jiaye Lin, Lei Wei, Guangyuan Dong, Xitong Ling, Xixun Lin, Quanchen Zou, Xiangzheng Zhang
- 식별자: `arxiv:2607.25255`

## 요약·초록

Multi-agent systems improve capability through task decomposition and role specialization, but these same mechanisms introduce an important safety blind spot: a harmful objective can be fragmented into locally plausible subtasks, allowing malicious intent to evade detection by any single agent. This is a growing social-impact challenge: systems handling sensitive information or consequential tools can turn routine delegation into unauthorized disclosure or unsafe action. We argue that this failure mode is better understood as a semantic information-flow problem than as a single-turn prompt classification task. To address this, we propose SafeFlow, a defense framework for multi-agent systems that formalizes malicious cross-agent propagation as a semantic information-flow problem. SafeFlow attaches structured semantic taints to root requests, propagates them through a dynamic collaboration graph, and performs workflow-level validation to reconstruct the global risk context before irreversible actions are committed. Evaluated on four benchmarks spanning prompt injection, jailbreak-based unsafe tool use, risky code execution, and harmful web-agent behavior, SafeFlow reduces attack success rates compared to undefended baselines and external defenses while retaining high benign task completion and a high paired safe--harm success rate. Our findings show that multi-agent systems still lack mechanisms for preserving risk semantics across delegation boundaries. This gap can turn routine delegation into privacy harms or unsafe actions that affect people and organizations. SafeFlow keeps this risk visible throughout the workflow, before it results in harm.

## 내 메모


