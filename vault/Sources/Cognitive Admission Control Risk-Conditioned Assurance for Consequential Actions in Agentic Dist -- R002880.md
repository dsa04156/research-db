---
type: research-source
item_id: 2880
title: "Cognitive Admission Control: Risk-Conditioned Assurance for Consequential Actions in Agentic Distributed Systems"
source: "kurate"
published: "2026-09-14T20:20:54Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.16313"
url: "http://arxiv.org/abs/2609.16313v1"
generated_by: codex-research-db
aliases:
  - "Cognitive Admission Control: Risk-Conditioned Assurance for Consequential Actions in Agentic Distributed Systems"
topics:
  - "cloud-infrastructure"
---

# Cognitive Admission Control: Risk-Conditioned Assurance for Consequential Actions in Agentic Distributed Systems

[원문 열기](http://arxiv.org/abs/2609.16313v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `kurate`
- 검토 상태: `pending`
- 발행일: 2026-09-14T20:20:54Z
- 저자: Jun He, Deying Yu
- 식별자: `arxiv:2609.16313`

## 요약·초록

In agentic distributed systems, an agent may be authorized to mutate external infrastructure while lacking evidence that the mutation is ready to execute. Cognitive Admission Control (CAC) makes this evidence requirement explicit. A policy maps a typed action and its modeled risk to assurance obligations specifying predicates, evidence classes, scope, freshness, and witness-set constraints. A deterministic evaluator distinguishes satisfied, violated, and unresolved obligations; unresolved conditions produce targeted evidence-acquisition requests. Successful admission produces a certificate binding the action, its witness manifest, and dispatch-time guards. We formalize the admission calculus and the assumptions connecting it to mediated execution. The guarantees are policy-relative: physical safety additionally requires sound evidence, an adequate environment model, and preservation of relevant conditions through the effect. A TypeScript prototype is evaluated in 2,730 controlled local trials with independent effect observation and matched fault schedules. Across 390 CAC trials, 120 effects complete without modeled harm and no harmful effects occur. A live-policy baseline achieves the same completion count but admits the constructed correlated-witness failure. Mechanism ablations isolate guard, evidence-class, structural-cut, and remediation behavior. A further 9,000 measurements exercise the complete local dispatch path with persistent replay protection. These results establish tested implementation behaviors and local costs, not production failure rates or comparisons of language-model capability.

## 내 메모
