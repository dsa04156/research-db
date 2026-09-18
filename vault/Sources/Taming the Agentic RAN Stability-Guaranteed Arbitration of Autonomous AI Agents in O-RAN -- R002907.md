---
type: research-source
item_id: 2907
title: "Taming the Agentic RAN: Stability-Guaranteed Arbitration of Autonomous AI Agents in O-RAN"
source: "arxiv"
published: "2026-09-16T15:59:44Z"
first_seen: "2026-09-18"
review_status: "pending"
canonical_key: "arxiv:2609.18857"
url: "https://arxiv.org/abs/2609.18857v1"
generated_by: codex-research-db
aliases:
  - "Taming the Agentic RAN: Stability-Guaranteed Arbitration of Autonomous AI Agents in O-RAN"
topics:
  - "ai-agents"
---

# Taming the Agentic RAN: Stability-Guaranteed Arbitration of Autonomous AI Agents in O-RAN

[원문 열기](https://arxiv.org/abs/2609.18857v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-18|2026-09-18]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`XBZK4PES`)
- 발행일: 2026-09-16T15:59:44Z
- 저자: Seyed Bagher Hashemi Natanzi, Bo Tang
- 식별자: `arxiv:2609.18857`

## 요약·초록

The O-RAN control plane is becoming agentic: autonomous AI agents, deployed as rApps by different vendors, independently close control loops over shared radio resources. We demonstrate on a live O-RAN system that this independence is unsafe. Two agents with individually correct objectives, one protecting a latency SLA and one maximizing utilization for energy efficiency, jointly drive recurring opposing excursions of the shared resource partition that neither produces alone. Existing conflict-mitigation mechanisms presume a statically known application population and cannot govern agents whose behavior emerges at run time. We present AURA, a lightweight arbitration layer that admits agent actions only when they satisfy feasibility invariants, per-variable dwell times, and a deadband, and we prove the arbitrated system converges to a feasible operating point. Implemented on an OpenAirInterface (OAI) testbed with measured one-way latency and throughput, AURA reduces recurring shared-state excursions by more than an order of magnitude (from 8.4 to 0.4 PRB amplitude) and virtually eliminates cross-slice throughput starvation (from 40-55% to 0.3%), while leaving the protected slice's own latency compliance unchanged, a trade-off the convergence guarantee makes explicit.

## 내 메모


