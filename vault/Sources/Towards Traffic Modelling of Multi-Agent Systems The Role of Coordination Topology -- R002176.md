---
type: research-source
item_id: 2176
title: "Towards Traffic Modelling of Multi-Agent Systems: The Role of Coordination Topology"
source: "arxiv"
published: "2026-08-20T18:30:46Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "doi:10.1145/3789240.3828749"
url: "https://arxiv.org/abs/2608.20494v1"
generated_by: codex-research-db
aliases:
  - "Towards Traffic Modelling of Multi-Agent Systems: The Role of Coordination Topology"
topics:
  - "ai-agents"
---

# Towards Traffic Modelling of Multi-Agent Systems: The Role of Coordination Topology

[원문 열기](https://arxiv.org/abs/2608.20494v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-20T18:30:46Z
- 저자: Davide Lamagna, Albert Cabellos, Alberto Rodriguez-Natal, Gábor Rétvári, Berta Serracanta
- 식별자: `doi:10.1145/3789240.3828749`

## 요약·초록

Multi-agent LLM systems are an emerging networked workload whose rapid deployment raises questions about the traffic patterns they generate. Compared to conventional applications, these systems generate requests internally: a single user task can induce a structured sequence of model calls whose timing is governed by coordination logic rather than by user arrival rate. It is not clear whether classical traffic models, designed for human-driven workloads, apply to this setting. We present an empirical characterisation of LLM-call interarrival time distributions across sequential, star, and full-mesh agentic coordination topologies, using a multi-layer measurement framework over 500 repeated runs per topology. We find that topology fundamentally shapes the arrival process of requests to the LLM backend: fan-out coordination introduces a structural bimodality absent in sequential execution, and the reasoningphase component is best described by a log-normal distribution, with the Poisson exponential null model decisively rejected across all topologies. These differences propagate to inference and network level metrics. The framework and analysis pipeline are released openly at https://github.com/dlamagna/agentraffic.

## 내 메모


