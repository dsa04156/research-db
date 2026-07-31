---
type: research-source
item_id: 1180
title: "Beyond Pre-Training: The Full Lifecycle of Foundation Models on HPC Systems"
source: "arxiv"
published: "2026-04-14T11:26:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.12599"
url: "https://arxiv.org/abs/2604.12599v1"
generated_by: codex-research-db
aliases:
  - "Beyond Pre-Training: The Full Lifecycle of Foundation Models on HPC Systems"
topics:
  - "kubernetes"
---

# Beyond Pre-Training: The Full Lifecycle of Foundation Models on HPC Systems

[원문 열기](https://arxiv.org/abs/2604.12599v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`2IIVUH24`)
- 발행일: 2026-04-14T11:26:41Z
- 저자: Dino Conciatore, Elia Oggian, Federico Da Forno, Stefano Schuppli, Jerome Tissieres, Joost VandeVondele, Maxime Martinasso
- 식별자: `arxiv:2604.12599`

## 요약·초록

Large-scale pre-training of Foundational Models (FM) constitutes a computationally intensive first phase for enabling AI across diverse scientific and societal applications. This first phase has positioned High-Performance Computing (HPC) facilities as indispensable backbones of "Sovereign AI" initiatives. While the massive throughput requirements of FM pre-training align with the traditional capability-oriented mission of HPC, subsequent phases of the AI lifecycle, typically referred to as fine-tuning and inference, introduce operational paradigms that can conflict with established batch-processing environments. Moreover, these phases are not computationally trivial: they often require substantial high-end compute resources while exhibiting hardware utilization patterns that differ significantly from those of pre-training. This paper addresses the architectural and strategic challenges of operationalizing a complete AI lifecycle within a national supercomputing facility. We present a hybrid cloud-native platform being developed and deployed at the Swiss National Supercomputing Centre (CSCS) that combines diskless GPU-enabled HPE Cray EX compute nodes with virtualized commodity infrastructure. Orchestrated by Kubernetes, this novel service architecture bridges the gap between HPC batch processing and service-oriented workflows. We report our initial investigations into fine-tuning pipelines and highly available inference services, analyzing the associated trade-offs while improving user productivity. Our findings offer a blueprint for enabling supercomputers to integrate "AI Factories" services and workflows, supporting AI innovations into end-to-end scientific and industrial use cases.

## 내 메모


