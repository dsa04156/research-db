---
type: research-source
item_id: 599
title: "Efficient and Scalable Agentic AI with Heterogeneous Systems"
source: "arxiv"
published: "2025-07-25T19:02:42Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.19635"
url: "https://arxiv.org/abs/2507.19635v1"
generated_by: codex-research-db
aliases:
  - "Efficient and Scalable Agentic AI with Heterogeneous Systems"
topics:
  - "ai-agents"
---

# Efficient and Scalable Agentic AI with Heterogeneous Systems

[원문 열기](https://arxiv.org/abs/2507.19635v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`7BCVV4CA`)
- 발행일: 2025-07-25T19:02:42Z
- 저자: Zain Asgar, Michelle Nguyen, Sachin Katti
- 식별자: `arxiv:2507.19635`

## 요약·초록

AI agents are emerging as a dominant workload in a wide range of applications, promising to be the vehicle that delivers the promised benefits of AI to enterprises and consumers. Unlike conventional software or static inference, agentic workloads are dynamic and structurally complex. Often these agents are directed graphs of compute and IO operations that span multi-modal data input and conversion), data processing and context gathering (e.g vector DB lookups), multiple LLM inferences, tool calls, etc. To scale AI agent usage, we need efficient and scalable deployment and agent-serving infrastructure. To tackle this challenge, in this paper, we present a system design for dynamic orchestration of AI agent workloads on heterogeneous compute infrastructure spanning CPUs and accelerators, both from different vendors and across different performance tiers within a single vendor. The system delivers several building blocks: a framework for planning and optimizing agentic AI execution graphs using cost models that account for compute, memory, and bandwidth constraints of different HW; a MLIR based representation and compilation system that can decompose AI agent execution graphs into granular operators and generate code for different HW options; and a dynamic orchestration system that can place the granular components across a heterogeneous compute infrastructure and stitch them together while meeting an end-to-end SLA. Our design performs a systems level TCO optimization and preliminary results show that leveraging a heterogeneous infrastructure can deliver significant TCO benefits. A preliminary surprising finding is that for some workloads a heterogeneous combination of older generation GPUs with newer accelerators can deliver similar TCO as the latest generation homogenous GPU infrastructure design, potentially extending the life of deployed infrastructure.

## 내 메모


