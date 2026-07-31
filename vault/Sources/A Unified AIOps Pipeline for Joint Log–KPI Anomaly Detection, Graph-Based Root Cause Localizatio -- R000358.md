---
type: research-source
item_id: 358
title: "A Unified AIOps Pipeline for Joint Log–KPI Anomaly Detection, Graph-Based Root Cause Localization, and LLM-Generated Runbooks"
source: "openalex"
published: "2024-03-17"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.69987/jacs.2024.40305"
url: "https://doi.org/10.69987/jacs.2024.40305"
generated_by: codex-research-db
aliases:
  - "A Unified AIOps Pipeline for Joint Log–KPI Anomaly Detection, Graph-Based Root Cause Localization, and LLM-Generated Runbooks"
topics:
  - "kubernetes"
---

# A Unified AIOps Pipeline for Joint Log–KPI Anomaly Detection, Graph-Based Root Cause Localization, and LLM-Generated Runbooks

[원문 열기](https://doi.org/10.69987/jacs.2024.40305)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`2AHB2GVE`)
- 발행일: 2024-03-17
- 저자: Hanqi Zhang
- 식별자: `doi:10.69987/jacs.2024.40305`

## 요약·초록

Modern cloud services emit heterogeneous operational signals—structured logs, KPIs, and traces—yet many anomaly detectors and diagnosis tools remain siloed by modality. This paper presents UniAIOps, an end-to-end pipeline that (i) scores anomalies jointly from logs and metrics, (ii) localizes probable root causes on a dependency graph with Top-k ranking, and (iii) produces operator-ready runbooks using an LLM-style agent constrained by safety and executability guardrails. We target three widely used public AIOps data sources: LogHub/LogPAI log corpora, the AIOps 2018 KPI anomaly detection challenge, and the AIOps 2020 multi-modal challenge data release. In environments where those archives cannot be fetched (e.g., broken mirrors, authentication gates, or bandwidth limits), full experimental evaluation becomes difficult to reproduce. To address this, we provide a proxy benchmark generator that follows the public schemas and typical anomaly patterns described for these datasets, and we report end-to-end results with fixed seeds. Across the proxy benchmarks, UniAIOps improves incident-level detection F1 by up to 0.25 over single-modality baselines, reaches 0.74 Top-1 and 1.00 Top-3 root cause hit rates on graph-injected faults, and yields runbooks with 1.00 average actionability under an eight-criterion rubric. We further analyze detection delay, runtime cost, and deployment constraints (data privacy, prompt injection, and permissioned actions) relevant to LLM-assisted AIOps.

## 내 메모


