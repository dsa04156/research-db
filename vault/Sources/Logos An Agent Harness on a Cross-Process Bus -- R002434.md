---
type: research-source
item_id: 2434
title: "Logos: An Agent Harness on a Cross-Process Bus"
source: "arxiv"
published: "2026-08-28T17:30:10Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.28553"
url: "https://arxiv.org/abs/2608.28553v2"
generated_by: codex-research-db
aliases:
  - "Logos: An Agent Harness on a Cross-Process Bus"
topics:
  - "self-evolving-harness"
---

# Logos: An Agent Harness on a Cross-Process Bus

[원문 열기](https://arxiv.org/abs/2608.28553v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SVFHARCN`)
- 발행일: 2026-08-28T17:30:10Z
- 저자: Hanzhang Jia, Liheng Zeng, Hao Cheng, Yi Gao, Bo Ma
- 식별자: `arxiv:2608.28553`

## 요약·초록

Modern agent systems assemble capabilities at runtime, and this dynamic composition has recently received a complete formal treat ment in the spatiotemporal-composability calculus, in which a capability is a component carrying a tracked inverse, and agents are assembled as plugins. This plugin form is carried by a single process sharing one context, a carrier that places all components in one physical failure domain, a fault suspends every component at once, and process death interrupts every session the process hosts. This paper shows that neither the modeling nor the calculus binds an agent to one process, the statelessness of the language model keeps all cross-step state outside the model, and the soundness invariant is defined on the state space alone. These observations condense into four lemmas whose premises are the hypotheses of the calculus and the statelessness of language-model inference. On these lemmas this paper constructs Logos, a ROS-like cross process agent harness in which a plugin is a process and the only shared state is an append-only transcript. Eighty sessions resume with no repeated effect after kills placed at the four boundaries of the tool-call cycle, and a same-fault comparison with a single process reference configuration shows one fault interrupting every co-resident session while under the peer-process construction one fault ends at one node.

## 내 메모


