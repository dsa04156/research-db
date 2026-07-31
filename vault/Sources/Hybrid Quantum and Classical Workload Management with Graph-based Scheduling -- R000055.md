---
type: research-source
item_id: 55
title: "Hybrid Quantum and Classical Workload Management with Graph-based Scheduling"
source: "arxiv"
published: "2026-07-10T07:09:32Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.09151"
url: "https://arxiv.org/abs/2607.09151v2"
generated_by: codex-research-db
aliases:
  - "Hybrid Quantum and Classical Workload Management with Graph-based Scheduling"
topics:
  - "kubernetes"
---

# Hybrid Quantum and Classical Workload Management with Graph-based Scheduling

[원문 열기](https://arxiv.org/abs/2607.09151v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TKN4XGQM`)
- 발행일: 2026-07-10T07:09:32Z
- 저자: Vanessa Sochat, Daniel Milroy
- 식별자: `arxiv:2607.09151`

## 요약·초록

High Performance Computing (HPC) centers are expanding to encompass resources that extend beyond traditional computing. By extending resources to quantum computing, hybrid quantum-classical workflows tackle complex optimization problems that have never before been possible. However, integrating quantum processing units (QPUs) into cloud-native and scientific workload managers presents a unique orchestration challenge: remote quantum devices introduce a second, external queue -- a two-queue problem -- alongside the queue owned by the traditional scheduler. In this work we present Fluence, a Kubernetes scheduler plugin backed by the Fluxion graph-based scheduler, that enables informed, gang-scheduled placement for quantum-classical workloads and custom resources. We evaluate Fluence across three scenarios using AWS Braket simulators and real QPUs. First, under node contention, Fluence's atomic gang placement all but eliminates the wasted node-time that a default scheduler accrues by partially placing gangs. Second, we introduce a synchronization primitive for the two-queue problem in which a single producer submits a shared quantum task while consumers remain scheduling-gated, reducing worker idle time by roughly 5x under short device queues and by orders of magnitude when a real device queue stretched to hours. Third, cost- and queue-aware backend selection pins the cheapest or shortest-queue device satisfying a workload, cutting mean per-run cost by roughly 70x and time-to-result from hours to under a minute. Together, these results show that quantum-awareness can be added to a cloud-native scheduler without modifying user containers.

## 내 메모


