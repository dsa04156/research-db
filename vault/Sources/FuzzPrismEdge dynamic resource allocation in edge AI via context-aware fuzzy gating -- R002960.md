---
type: research-source
item_id: 2960
title: "FuzzPrismEdge: dynamic resource allocation in edge AI via context-aware fuzzy gating"
source: "openalex"
published: "2026-09-19"
first_seen: "2026-09-22"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-72085-x"
url: "https://doi.org/10.1038/s41598-026-72085-x"
generated_by: codex-research-db
aliases:
  - "FuzzPrismEdge: dynamic resource allocation in edge AI via context-aware fuzzy gating"
topics:
  - "edge-computing"
---

# FuzzPrismEdge: dynamic resource allocation in edge AI via context-aware fuzzy gating

[원문 열기](https://doi.org/10.1038/s41598-026-72085-x)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-09-22|2026-09-22]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-09-19
- 저자: Mustafa Abdulkadhim, Sandor. R. Repas
- 식별자: `doi:10.1038/s41598-026-72085-x`

## 요약·초록

Abstract The use of Deep Neural Networks (DNNs) on autonomous Internet of Things (IoT) devices is bottlenecked and causes accelerated battery degradation, memory exhaustion and thermal throttling due to constant inference demands. While the current literature largely deals with this through static model quantization, in this paper, FuzzPrismEdge, an adaptive 3-tier hybrid fuzzy-neural architecture that dynamically scales computational payloads according to real-time environmental context is introduced. Using a lightweight Fuzzy Logic Controller (FLC) as a preliminary hardware gatekeeper, the framework assesses ambient telemetry; namely energy reserves and intensity of motion, to dynamically steer system states based on crisp defuzzified thresholds. In order to eliminate redundant spatial processing FuzzPrismEdge uses dynamic model substitution: Low-priority telemetry causes a deep hardware sleep (Tier 1), moderate telemetry triggers a lightweight spatial classifier (Tier 2), and critical telemetry triggers a computationally intensive, heavyweight object detection model (Tier 3). By dynamically allocating DNN complexity based on event priority, the FuzzPrismEdge architecture actively conserves the allocation of RAM, avoids unnecessary GPU spin-up in non-critical events, and extends the autonomous operational lifespan of edge nodes by 60.0% to 66.7% compared to static unoptimized baselines.

## 내 메모
