---
type: research-source
item_id: 1164
title: "A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification"
source: "arxiv"
published: "2026-05-21T21:47:52Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.23058"
url: "https://arxiv.org/abs/2605.23058v1"
generated_by: codex-research-db
aliases:
  - "A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification"
topics:
  - "kubernetes"
---

# A measurement substrate for agentic Kubernetes operations: Methodology and a case study in retrieval-compounding falsification

[원문 열기](https://arxiv.org/abs/2605.23058v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`59MFCFNB`)
- 발행일: 2026-05-21T21:47:52Z
- 저자: Joshua Odmark, Gideon Rubin, Deon van der Vyver
- 식별자: `arxiv:2605.23058`

## 요약·초록

Empirical claims about autonomous Kubernetes operations agents are largely unfalsifiable. Published work reports observational results without controlled comparisons against an agent-disabled baseline, selection bias is endemic, pre-registered decision matrices are absent, and samples are typically too small for the noise level of the underlying scoring system. The cause is the same gap that limits the agents themselves: code agents have a verification substrate that turns "did it work" into a fast, falsifiable, ground-truth signal, and operations has nothing equivalent. We present agent-breakage, a closed-loop measurement framework that injects faults into a target Kubernetes cluster, observes how an autonomous agent responds, scores the response on four axes against ground truth, and accumulates outcome-labeled (state, action, outcome) tuples. The framework distinguishes framework error from reasoning error, supports a true off-condition control via a deterministic-embedder mechanism, and enforces pre-registered decision matrices. We use it as a case study to test whether retrieval over past postmortems compounds an agent's capability. The methodological payload is three confounds the substrate caught during that case study, each of which would have produced a wrong published claim on a less instrumented version of the same work: a pgvector index bug, a +19% selection-bias artifact, and small-sample estimates that overstated effects by roughly 3x. The retrieval result itself is a partial falsification: 1 of 3 dense-corpus scenarios significant at p<0.05, pooled effect +3.9 percentage points, not significant at n=60. A within-scenario corpus-density sweep at 360 runs shows that mechanistic alignment of near-neighbors dominates raw count. The framework is released open source.

## 내 메모


