---
type: research-source
item_id: 2198
title: "When Do LLM Agents Help? Deadline-Aware Mixed-Criticality Task Scheduling at the Autonomous-Vehicle Edge"
source: "arxiv"
published: "2026-08-20T01:55:40Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.19557"
url: "https://arxiv.org/abs/2608.19557v1"
generated_by: codex-research-db
aliases:
  - "When Do LLM Agents Help? Deadline-Aware Mixed-Criticality Task Scheduling at the Autonomous-Vehicle Edge"
topics:
  - "edge-computing"
---

# When Do LLM Agents Help? Deadline-Aware Mixed-Criticality Task Scheduling at the Autonomous-Vehicle Edge

[원문 열기](https://arxiv.org/abs/2608.19557v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-20T01:55:40Z
- 저자: Reza Zakerian
- 식별자: `arxiv:2608.19557`

## 요약·초록

Autonomous vehicles offload latency-sensitive perception tasks to nearby mobile edge computing (MEC) servers, where a missed safety-critical task is unsafe rather than merely degraded. Large language models (LLMs) are increasingly proposed as adaptive, explainable schedulers, yet evidence of when they help is scarce. We study deadline-aware, mixed-criticality scheduling on heterogeneous MEC servers, where time-critical (TC) tasks must be protected at a controlled cost to best-effort traffic, and ask whether a multi-agent LLM control layer improves on a strong heuristic. We answer in two steps. First we build the heuristic: a windowed contract-net auction that orders each admission window time-critical-first by earliest deadline and places tasks by earliest-finish-time. Across 60 instances on three topologies and 15 baselines under an identical online constraint, it attains a TC completion rate of 0.902, above every baseline (Holm-corrected p < 0.001; best baseline 0.838) and at 0.87 of a CP-SAT upper bound. Second, we add the LLM control plane. A controlled decomposition traces the scheduler's advantage to two ordinary factors, the batching horizon and time-critical-first ordering; the auction, the per-window LLM policy, and online adaptation add nothing while the load is stationary, where the heuristic is already near-optimal. Under a mid-run surge of safety-critical tasks the picture changes, and the LLM control plane gains significantly over both the static heuristic and the bandit. LLM orchestration therefore earns its cost only when non-stationarity opens headroom a fixed policy cannot use. We report control-plane latency and rationale, and release all code and seeded instances.

## 내 메모


