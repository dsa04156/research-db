---
type: research-source
item_id: 1650
title: "WASP: A Configurable Framework for Portable Stateful Serverless Applications"
source: "openalex"
published: "2026-07-28"
first_seen: "2026-08-03"
review_status: "pending"
canonical_key: "arxiv:2607.25493"
url: "https://arxiv.org/abs/2607.25493"
generated_by: codex-research-db
aliases:
  - "WASP: A Configurable Framework for Portable Stateful Serverless Applications"
topics:
  - "cloud-infrastructure"
---

# WASP: A Configurable Framework for Portable Stateful Serverless Applications

[원문 열기](https://arxiv.org/abs/2607.25493)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-08-03|2026-08-03]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-07-28
- 저자: Matteo Cenzato, Dario d'Abate, Arianna Dragoni, Giacomo Orsenigo, Luca Tosetti, Alessandro Margara
- 식별자: `arxiv:2607.25493`

## 요약·초록

WebAssembly (WASM) is emerging as a lightweight alternative to containers for Function-as-a-Service (FaaS) across the edge-cloud continuum. However, existing WASM-based serverless platforms are tightly coupled to specific execution engines and predominantly designed for stateless workloads. This clashes with the heterogeneity of edge deployments, which demand support for stateful applications under diverse hardware and workload constraints. We introduce WASP, a configurable framework that brings stateful serverless execution to the edge-cloud continuum. By abandoning monolithic architectures in favor of strictly decoupled, pluggable components, WASP lets system administrators swap the WASM runtime and the datastore to fit available resources and application requirements, without altering application code. Configurable lifecycle and caching policies further enable fine-tuning for diverse non-functional requirements. Our experimental evaluation demonstrates that WASP introduces negligible runtime overhead and, by swapping runtimes, datastores, and policies, exposes radically different memory and latency profiles, confirming its adaptability to the heterogeneous constraints of the edge-cloud continuum.

## 내 메모


