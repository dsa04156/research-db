---
type: research-source
item_id: 1045
title: "LLM-as-Code: Agentic Programming for Agent Harness"
source: "arxiv"
published: "2026-06-14T15:47:27Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.15874"
url: "https://arxiv.org/abs/2606.15874v2"
generated_by: codex-research-db
aliases:
  - "LLM-as-Code: Agentic Programming for Agent Harness"
topics:
  - "self-evolving-harness"
---

# LLM-as-Code: Agentic Programming for Agent Harness

[원문 열기](https://arxiv.org/abs/2606.15874v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`IVB8WKPM`)
- 발행일: 2026-06-14T15:47:27Z
- 저자: Junjia Qi, Zichuan Fu, Jingtong Gao, Wenlin Zhang, Hanyu Yan, Xian Wu, Xiangyu Zhao
- 식별자: `arxiv:2606.15874`

## 요약·초록

Every major LLM agent framework gives the LLM the role of orchestrator; the model decides what to do next, when to call tools, and when to stop. We argue that token explosion, control-flow hallucination, and unreliable completion are not implementation bugs but architectural consequences of assigning the deterministic work of looping, branching, and sequencing to a probabilistic system. A better prompt or a stronger model cannot guarantee the reliability of the LLM agent. We therefore propose Agentic Programming, in which the program governs all control flow, and the LLM is itself part of it, an adaptive component we call LLM-as-Code and invoke only where a task calls for reasoning or generation. Within each call the model keeps full flexibility, but it cannot alter the program's execution path. With control in the program, the LLM's context is built from the execution history's call tree and forms a directed acyclic graph (DAG). Each call's context length is then determined by its call depth rather than by accumulation over steps. A case study of computer-use agents shows that the design is practical, not just a theoretical stance, substantially improving the stability of long visual operation sequences.

## 내 메모


