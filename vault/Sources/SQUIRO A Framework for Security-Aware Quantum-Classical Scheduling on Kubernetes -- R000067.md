---
type: research-source
item_id: 67
title: "SQUIRO: A Framework for Security-Aware Quantum-Classical Scheduling on Kubernetes"
source: "openalex"
published: "2026-07-17"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.16089"
url: "https://arxiv.org/abs/2607.16089"
generated_by: codex-research-db
aliases:
  - "SQUIRO: A Framework for Security-Aware Quantum-Classical Scheduling on Kubernetes"
topics:
  - "kubernetes"
---

# SQUIRO: A Framework for Security-Aware Quantum-Classical Scheduling on Kubernetes

[원문 열기](https://arxiv.org/abs/2607.16089)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`BVBV9KD9`)
- 발행일: 2026-07-17
- 저자: Ignazio Pedone, Edoardo Giusto
- 식별자: `arxiv:2607.16089`

## 요약·초록

Distributed infrastructure schedulers traditionally optimise capacity, locality, and cost, but provide limited support for security posture and emerging quantum-classical workloads. As hybrid quantum-classical computing becomes increasingly practical and post-quantum security requirements begin to affect infrastructure deployment, schedulers must jointly reason about heterogeneous compute resources, security constraints, and quantum backend characteristics. We present SQUIRO, a framework for security-aware quantum-classical scheduling based on a platform-independent Unified Scheduling Model (USM) and a six-step Scheduler Design Methodology (SDM) that together enable the derivation of concrete schedulers for Kubernetes, high-performance computing (HPC), and federated environments. The framework combines multidimensional security posture enforcement through hard feasibility constraints with residual-risk optimisation, and introduces a circuit-aware quantum backend selector that accounts for coherence margin, calibration freshness, queue pressure, and hardware capabilities through a forward-compatible colocation hierarchy. Evaluation on synthetic Kubernetes clusters shows that the security model enforces complete compliance for regulated workloads by construction, while global optimisation reduces infrastructure cost by up to 51% and energy consumption by up to 63% compared with greedy placement in underloaded scenarios, without compromising admission priorities. Additional experiments characterise the solve-time growth of the current CP-SAT formulation and show that circuit-aware backend selection systematically diverges from naive error-rate ranking under coherence- and queue-limited conditions.

## 내 메모


