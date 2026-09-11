---
type: research-source
item_id: 2783
title: "From Intent to Execution Grant: An Execution-Boundary Conformance Profile for High-Risk AI Actions"
source: "arxiv"
published: "2026-09-10T14:21:45Z"
first_seen: "2026-09-11"
review_status: "pending"
canonical_key: "arxiv:2609.11596"
url: "https://arxiv.org/abs/2609.11596v1"
generated_by: codex-research-db
aliases:
  - "From Intent to Execution Grant: An Execution-Boundary Conformance Profile for High-Risk AI Actions"
topics:
  - "ai-agents"
---

# From Intent to Execution Grant: An Execution-Boundary Conformance Profile for High-Risk AI Actions

[원문 열기](https://arxiv.org/abs/2609.11596v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-11|2026-09-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-10T14:21:45Z
- 저자: Mengting Wu, Lin Wang, Yong Zhang, Jiang Deng
- 식별자: `arxiv:2609.11596`

## 요약·초록

AI agents increasingly propose actions with external consequences, including financial transfers, infrastructure changes, software deployments, disclosures, and physical actuation. Authorization engines, policy languages, runtime monitors, provenance mechanisms, and agent guardrails provide important foundations, but do not necessarily define a common semantic contract for the final transition from a particular candidate action to execution authority. We specify EBL-Core, an execution-boundary conformance profile for deciding whether one canonical, fully materialized AI-generated candidate may receive action-scoped execution authority under explicit conditions. It binds a structured intent object, Root and Operational Policies, evidence obligations, typed evidence, context, time, and a verifiable Decision Derivation through an Execution Release Contract (ERC). An ERC is not an authority-bearing token; a verified ALLOW ERC may support a separate Execution Grant governed by Redemption-time validation. EBL-Core specifies action binding, policy non-weakening, evidence handling, deterministic adjudication, derivation verification, and grant lifecycle behavior. An accompanying reference artifact provides schemas, adjudication, separate verification and Semantic Replay, and a linearizable in-memory grant store. In the retained run, 34 static vectors and 15 lifecycle checks matched expected outcomes. Across 100 trials, 32 concurrent Redemption attempts yielded exactly one successful Redemption and protected test effect per trial; 100 Revoke-Redeem races ended in valid terminal outcomes. These bounded results demonstrate executability of the specified subset, not human-intent correctness, evidence truth, complete mediation, production readiness, mechanized correctness, or deployment-level security.

## 내 메모


