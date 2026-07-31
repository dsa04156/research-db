---
type: research-source
item_id: 997
title: "Falsifiable Release Gates for Self-Improving Systems: Standing Invariants at Scale"
source: "arxiv"
published: "2026-07-11T06:06:34Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.13070"
url: "https://arxiv.org/abs/2607.13070v2"
generated_by: codex-research-db
aliases:
  - "Falsifiable Release Gates for Self-Improving Systems: Standing Invariants at Scale"
topics:
  - "self-evolving-harness"
---

# Falsifiable Release Gates for Self-Improving Systems: Standing Invariants at Scale

[원문 열기](https://arxiv.org/abs/2607.13070v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`N4MPBMR6`)
- 발행일: 2026-07-11T06:06:34Z
- 저자: Deepak Soni
- 식별자: `arxiv:2607.13070`

## 요약·초록

Safety claims for self-improving agent runtimes are almost always self-graded: a policy file, a guardrail, a promise in a README. We describe falsifiable release gates, a methodology in which every new capability must pass a pre-declared, machine-checkable acceptance suite before it ships, while a fixed set of standing invariants is preserved across every gate. We instantiate it in Antahkarana, an open runtime, then do what a method paper is only vindicated by: we follow the same runtime as it grows and ask whether the guarantees survive. The safety-critical property, that no action reaches an effector without a capability token minted by a control ring, is machine-checked exhaustively over the reachable states of a bounded model; a deliberately broken model yields the shortest counterexample, so the checker demonstrably has teeth. We then carry the runtime through six further releases. Across every one, the action-safety invariants INV-1 through INV-6 held without a single change, and one release added three capabilities while introducing no new invariant. Under the same teeth discipline, six more machine-checked families were added: memory with provable unlearning, a governed agent, calibrated abstention over a post-quantum record, a harness of many sub-agents, the self-improvement loop itself, and the residency of what it produces. The acceptance suite grew from 122 tests to 563. The load-bearing result sits in the negative space: across more than a doubling of capability, the safety core was neither weakened nor redesigned. The last families are the first on real hardware: gated self-improvement compounds a small model from 20% to 70% accuracy while auto-rejecting a candidate that only inflates confidence, and the whole governed path costs 0.021 ms per request, 0.008% of model inference. We release the runtime, tools, and gate suite; every number reproduces with a single command.

## 내 메모


