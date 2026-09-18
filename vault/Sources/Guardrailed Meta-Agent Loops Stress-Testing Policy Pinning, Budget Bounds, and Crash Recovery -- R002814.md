---
type: research-source
item_id: 2814
title: "Guardrailed Meta-Agent Loops: Stress-Testing Policy Pinning, Budget Bounds, and Crash Recovery"
source: "arxiv"
published: "2026-09-10T21:22:08Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.12216"
url: "https://arxiv.org/abs/2609.12216v1"
generated_by: codex-research-db
aliases:
  - "Guardrailed Meta-Agent Loops: Stress-Testing Policy Pinning, Budget Bounds, and Crash Recovery"
topics:
  - "self-evolving-harness"
---

# Guardrailed Meta-Agent Loops: Stress-Testing Policy Pinning, Budget Bounds, and Crash Recovery

[원문 열기](https://arxiv.org/abs/2609.12216v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FRTWFRRT`)
- 발행일: 2026-09-10T21:22:08Z
- 저자: Qinzhen Ma, Jialin Wu
- 식별자: `arxiv:2609.12216`

## 요약·초록

Self-improving agent workflows create an audit problem when the same controller can change both its behavior and the conditions under which that behavior is judged. We present GuardrailLoop, a simulation-based testbed that makes three operational contracts jointly testable: preservation of human-defined policy, compute accounting at every recorded execution prefix, and recovery of a specified scientific state after crashes. A hash-pinned policy fixes goals, scope, evaluation identity, budget, and release conditions; machine-directed evolution is restricted to a code-owned feature catalog and bounded knobs. The contribution is an executable boundary and an evaluation protocol that separates useful adaptation, state recovery, and repeated execution. In a paired 50-seed 2 x 2 study, round-stage growth changes target attainment by +1.00 and restricted mean compute to target by -56.97 simulated GPU-hours (95% paired-bootstrap interval [-58.91,-54.70]); idle growth has zero measured utility effect. Across 240 enumerated crash injections, all runs recover the defined outcome, but only 210 preserve the normalized trace: 30 pre-commit crashes repeat a planner call. Resource-drift, kill-switch, integrity, and output-guard matrices satisfy their specified checks. These findings show why successful outcome recovery is insufficient evidence of exactly-once execution. They establish conformance within one calibrated deterministic testbed, rather than general safety or real-world self-improvement.

## 내 메모
