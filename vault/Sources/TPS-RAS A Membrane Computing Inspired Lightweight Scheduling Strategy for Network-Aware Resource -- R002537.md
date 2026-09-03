---
type: research-source
item_id: 2537
title: "TPS-RAS: A Membrane Computing Inspired Lightweight Scheduling Strategy for Network-Aware Resource Allocation in Fog Computing"
source: "openalex"
published: "2026-08-31"
first_seen: "2026-09-03"
review_status: "pending"
canonical_key: "doi:10.3837/tiis.2026.08.013"
url: "https://doi.org/10.3837/tiis.2026.08.013"
generated_by: codex-research-db
aliases:
  - "TPS-RAS: A Membrane Computing Inspired Lightweight Scheduling Strategy for Network-Aware Resource Allocation in Fog Computing"
topics:
  - "kubernetes"
---

# TPS-RAS: A Membrane Computing Inspired Lightweight Scheduling Strategy for Network-Aware Resource Allocation in Fog Computing

[원문 열기](https://doi.org/10.3837/tiis.2026.08.013)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-03|2026-09-03]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`SJU75N33`)
- 발행일: 2026-08-31
- 저자: Yuanhan Zhang, Zhenzhou Ji
- 식별자: `doi:10.3837/tiis.2026.08.013`

## 요약·초록

Fog computing has reshaped data generation patterns for addressing the latency constraint problem of cloud-based IoT networks by offloading tasks to the network edge.However, an efficient resource allocation strategy in a heterogeneous fog network is still difficult and essential.Standard industry schedulers (e.g., Kubernetes) often overlook the underlying network topology heterogeneity, leading to high transmission delays, while emerging Deep Reinforcement Learning (DRL) approaches suffer from excessive inference overhead.To address these issues, we propose TPS-RAS, a lightweight membrane-inspired resource allocation strategy.We model the fog topology as a Tissue-like P System with a Broker Membrane, mapping physical nodes to parallel evolutionary units.TPS-RAS incorporates a vectorized Micro-Grey Wolf Optimizer (Micro-GWO) kernel to resolve high-concurrency resource conflicts deterministically.Furthermore, a Dynamic Scarcity Weight Vector mechanism is introduced to adaptively balance multi-dimensional resource demands (CPU, RAM, Bandwidth) against network transmission penalties.Experimental results demonstrate that TPS-RAS achieves comparable resource utilization with significantly lower decision latency, reducing scheduling decision latency by ~95% while maintaining a high resource utilization rate (~65%) under saturation.

## 내 메모


