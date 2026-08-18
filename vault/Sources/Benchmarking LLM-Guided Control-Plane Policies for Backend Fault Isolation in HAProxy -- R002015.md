---
type: research-source
item_id: 2015
title: "Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy"
source: "openalex"
published: "2026-08-11"
first_seen: "2026-08-18"
review_status: "pending"
canonical_key: "doi:10.48550/arxiv.2608.10532"
url: "https://arxiv.org/abs/2608.10532"
generated_by: codex-research-db
aliases:
  - "Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy"
topics:
  - "kubernetes"
---

# Benchmarking LLM-Guided Control-Plane Policies for Backend Fault Isolation in HAProxy

[원문 열기](https://arxiv.org/abs/2608.10532)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-18|2026-08-18]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`B2ZSMXN2`)
- 발행일: 2026-08-11
- 저자: Aman Chauhan, Vishnu Pendyala
- 식별자: `doi:10.48550/arxiv.2608.10532`

## 요약·초록

Static load balancers cannot mitigate a backend that is degraded rather than down: round-robin and least-connections keep routing traffic to a server returning HTTP 500s until an operator intervenes. We ask whether a Large Language Model can replace the static routing policy itself, reading HAProxy and Prometheus telemetry every 10 seconds and isolating faulty servers through guardrailed calls to the HAProxy Data Plane API. On a reproducible benchmark with a persistent structural fault built into roughly one-third of a heterogeneous fleet, we sweep 15 open-weight models across five families (0.35B to 35B total parameters; dense, mixture-of-experts, and efficient-sparse architectures), reasoning modes, fleet scales of 3 to 9 backends, and two routing algorithms, totaling 240 runs. We find a capability threshold near 3B active parameters. Below it, LLM policies are typically unreliable and sometimes worse than no policy; above it, every model, regardless of architecture, saturates near an 88% reduction in client-perceived 5xx errors over the static baseline. The threshold is approximate: Gemma 4 E2B clears it with 2B active parameters, while the dense 3B Granite 4.0 Micro does not. The availability gain has costs. Draining concentrates load onto surviving servers, inflating tail latency 2.6 to 2.8 times, and enabling reasoning multiplies token spend roughly tenfold, overrunning the control interval and degrading effectiveness. The efficient operating point is a supra-threshold model in its cheapest non-reasoning mode, wrapped inside deterministic guardrails.

## 내 메모


