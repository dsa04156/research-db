---
type: research-source
item_id: 1153
title: "A Low-Latency Semantic State Estimator using Latent Predictive Learning for Dynamic Network Monitoring and Orchestration"
source: "arxiv"
published: "2026-06-07T22:50:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.08869"
url: "https://arxiv.org/abs/2606.08869v1"
generated_by: codex-research-db
aliases:
  - "A Low-Latency Semantic State Estimator using Latent Predictive Learning for Dynamic Network Monitoring and Orchestration"
topics:
  - "edge-computing"
  - "kubernetes"
---

# A Low-Latency Semantic State Estimator using Latent Predictive Learning for Dynamic Network Monitoring and Orchestration

[원문 열기](https://arxiv.org/abs/2606.08869v1)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UI2V3ID7`)
- 발행일: 2026-06-07T22:50:00Z
- 저자: Hari Madhukumar, Haiyuan Li, Xiaolan Liu, Andy Corston-Petrie, Dimitra Simeonidou
- 식별자: `arxiv:2606.08869`

## 요약·초록

Closed-loop network monitoring and orchestration increasingly require semantic interpretations of live telemetry beyond raw counter collection. However, dynamic cloud-edge environments change both the active node set and the monitoring query at runtime, while control loops demand bounded millisecond-scale responses. We introduce a latent predictive state estimator (LPSE) for dynamic network monitoring and orchestration, built on latent predictive learning over streaming telemetry. The framework converts variable-cardinality node telemetry into topology-adaptive temporal representations, fuses them with monitoring questions, and returns bounded answers from a semantic codebook instead of autoregressive text generation. This design enables fixed-cost, single-pass inference while preserving semantic interpretability. By operating on permutation-invariant, slot-routed node representations keyed by stable identity, the model maintains a fixed input space and generalizes to node addition, removal, and reordering without retraining. Experimental results on a multi-node Kubernetes cluster show semantic prediction accuracy of 82.42% at approximately 41$\times$ lower mean inference latency and 15$\times$ smaller memory footprint compared with a deployable 4B LLM endpoint.

## 내 메모


