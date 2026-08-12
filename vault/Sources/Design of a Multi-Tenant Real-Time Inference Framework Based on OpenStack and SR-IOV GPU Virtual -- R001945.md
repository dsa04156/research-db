---
type: research-source
item_id: 1945
title: "Design of a Multi-Tenant Real-Time Inference Framework Based on OpenStack and SR-IOV GPU Virtualization"
source: "openalex"
published: "2026-08-09"
first_seen: "2026-08-12"
review_status: "pending"
canonical_key: "doi:10.13052/jicts2245-800x.1434"
url: "https://doi.org/10.13052/jicts2245-800x.1434"
generated_by: codex-research-db
aliases:
  - "Design of a Multi-Tenant Real-Time Inference Framework Based on OpenStack and SR-IOV GPU Virtualization"
topics:
  - "cloud-infrastructure"
---

# Design of a Multi-Tenant Real-Time Inference Framework Based on OpenStack and SR-IOV GPU Virtualization

[원문 열기](https://doi.org/10.13052/jicts2245-800x.1434)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-08-12|2026-08-12]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`9BKK7TCB`)
- 발행일: 2026-08-09
- 저자: Ma Rui, Shi Bingfeng, Ma Xin, Wei Bin
- 식별자: `doi:10.13052/jicts2245-800x.1434`

## 요약·초록

The deployment of real-time artificial intelligence inference services on shared cloud infrastructure poses significant challenges due to resource contention, latency variability, and tail-latency amplification. While cloud platforms offer scalability and flexibility, conventional accelerator sharing mechanisms often fail to provide the determinism required by latency-sensitive inference workloads. This paper presents a standards-based, multi-tenant cloud inference framework that integrates OpenStack orchestration with Single Root I/O Virtualization (SR-IOV)-enabled graphics processing unit (GPU) partitioning to achieve predictable and isolated real-time inference execution. In the proposed architecture, each tenant is assigned an exclusive GPU virtual function, enabling hardware-level isolation while remaining fully compatible with native OpenStack scheduling and resource management mechanisms. A comprehensive experimental evaluation is conducted on a private OpenStack cloud to assess inference latency distribution, tail behavior, scalability, robustness to background network and control-plane activity, and throughput-latency trade-offs. Experimental results show that median inference latency remains stable across single-tenant and multi-tenant configurations, while P95 and P99 tail latencies exhibit no measurable amplification under concurrent execution. The system scales linearly with the number of available GPU virtual functions, maintaining consistent latency behavior until hardware capacity is reached. Additional experiments demonstrate that background network traffic and control-plane operations introduce negligible impact on inference latency. Throughput analysis reveals a well-defined saturation knee, enabling clear identification of safe operating regions for real-time inference services. By leveraging mature ICT standards and open-source cloud infrastructure, this work provides a reusable reference architecture for deploying latency-sensitive inference services in private and hybrid clouds. The results highlight the effectiveness of hardware-assisted accelerator isolation in balancing performance determinism, scalability, and operational simplicity, and offer practical guidance for future system design and standardization efforts.

## 내 메모


