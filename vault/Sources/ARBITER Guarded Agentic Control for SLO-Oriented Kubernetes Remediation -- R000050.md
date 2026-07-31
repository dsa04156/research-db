---
type: research-source
item_id: 50
title: "ARBITER: Guarded Agentic Control for SLO-Oriented Kubernetes Remediation"
source: "arxiv"
published: "2026-07-21T15:15:56Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.19182"
url: "https://arxiv.org/abs/2607.19182v2"
generated_by: codex-research-db
aliases:
  - "ARBITER: Guarded Agentic Control for SLO-Oriented Kubernetes Remediation"
topics:
  - "kubernetes"
---

# ARBITER: Guarded Agentic Control for SLO-Oriented Kubernetes Remediation

[원문 열기](https://arxiv.org/abs/2607.19182v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RXUUIG7W`)
- 발행일: 2026-07-21T15:15:56Z
- 저자: Pooyan Habibi, Alberto Leon-Garcia
- 식별자: `arxiv:2607.19182`

## 요약·초록

Maintaining service-level objectives (SLOs) on Kubernetes microservices remains difficult because autoscalers observe coarse resource metrics, recent SLO controllers often depend on custom telemetry, and unconstrained agentic operators cannot safely mutate production clusters. We present ARBITER, a guarded control plane for SLO-oriented Kubernetes remediation. ARBITER builds an OpenTelemetry-native causal resource graph, assembles bounded DiagnosisContext objects, and exposes a finite typed-action interface that separates planning from execution. The same interface supports deterministic planners and an LLM-backed planning harness, with deterministic schema checks, policy gates, resource/disruption budgets, approval, and bounded execution forming the safety substrate. We evaluate ARBITER on a 4-node Kubernetes cluster using DeathStarBench Social Network and Online Boutique. The evaluation tests two forms of SLO-oriented control that resource autoscaling alone does not provide: selecting the right remediation action and selecting the right downstream target. For bad-image deployment regressions, ARBITER selects rollback_canary in all ten CPU-burn and pure-latency runs; HPA either scales the faulty image or never triggers. For a downstream critical-path fault, the user-visible breach appears at the frontend, but trace evidence identifies home-timeline-service as the remediable bottleneck. Deterministic ARBITER and a live approval-gated Sonnet harness target that downstream service in every replicate, whereas HPA/resource-only control never does. Additional experiments cover guarded placement repair, Online Boutique portability, adversarial safety rejection, offline multi-model replay, and KWOK-based control-plane scale evidence. We release the controller, replay corpus, harnesses, safety tests, and figure artifacts: https://github.com/pooyan/arbiter.

## 내 메모


