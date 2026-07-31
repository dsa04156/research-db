---
type: research-source
item_id: 246
title: "Learning Branching-Time Properties in CTL and ATL via Constraint Solving"
source: "arxiv"
published: "2024-06-28T12:58:18Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2406.19890"
url: "https://arxiv.org/abs/2406.19890v1"
generated_by: codex-research-db
aliases:
  - "Learning Branching-Time Properties in CTL and ATL via Constraint Solving"
topics:
  - "ai-agents"
---

# Learning Branching-Time Properties in CTL and ATL via Constraint Solving

[원문 열기](https://arxiv.org/abs/2406.19890v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`SA5A3XMX`)
- 발행일: 2024-06-28T12:58:18Z
- 저자: Benjamin Bordais, Daniel Neider, Rajarshi Roy
- 식별자: `arxiv:2406.19890`

## 요약·초록

We address the problem of learning temporal properties from the branching-time behavior of systems. Existing research in this field has mostly focused on learning linear temporal properties specified using popular logics, such as Linear Temporal Logic (LTL) and Signal Temporal Logic (STL). Branching-time logics such as Computation Tree Logic (CTL) and Alternating-time Temporal Logic (ATL), despite being extensively used in specifying and verifying distributed and multi-agent systems, have not received adequate attention. Thus, in this paper, we investigate the problem of learning CTL and ATL formulas from examples of system behavior. As input to the learning problems, we rely on the typical representations of branching behavior as Kripke structures and concurrent game structures, respectively. Given a sample of structures, we learn concise formulas by encoding the learning problem into a satisfiability problem, most notably by symbolically encoding both the search for prospective formulas and their fixed-point based model checking algorithms. We also study the decision problem of checking the existence of prospective ATL formulas for a given sample. We implement our algorithms in an Python prototype and have evaluated them to extract several common CTL and ATL formulas used in practical applications.

## 내 메모


