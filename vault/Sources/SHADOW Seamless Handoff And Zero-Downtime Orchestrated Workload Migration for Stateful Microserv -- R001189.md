---
type: research-source
item_id: 1189
title: "SHADOW: Seamless Handoff And Zero-Downtime Orchestrated Workload Migration for Stateful Microservices"
source: "arxiv"
published: "2026-03-26T14:24:12Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.25484"
url: "https://arxiv.org/abs/2603.25484v3"
generated_by: codex-research-db
aliases:
  - "SHADOW: Seamless Handoff And Zero-Downtime Orchestrated Workload Migration for Stateful Microservices"
topics:
  - "kubernetes"
---

# SHADOW: Seamless Handoff And Zero-Downtime Orchestrated Workload Migration for Stateful Microservices

[원문 열기](https://arxiv.org/abs/2603.25484v3)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6K6WD72T`)
- 발행일: 2026-03-26T14:24:12Z
- 저자: Hai Dinh-Tuan
- 식별자: `arxiv:2603.25484`

## 요약·초록

Migrating stateful microservices in Kubernetes requires careful state management because in-memory state is lost when a container restarts. For StatefulSet-managed workloads, the problem is amplified by identity constraints that prohibit two pods with the same ordinal from running simultaneously, forcing a sequential stop-restore cycle with unavoidable downtime. This paper presents SHADOW (Seamless Handoff And Zero-Downtime Orchestrated Workload Migration), a Kubernetes-native framework that implements the Message-based Stateful Microservice Migration (MS2M) approach as a Kubernetes Operator. SHADOW introduces the ShadowPod strategy, where a shadow pod is created from a CRIU checkpoint image on the target node while the source pod continues serving traffic, allowing concurrent operation during message replay. For StatefulSet workloads, an identity swap procedure with the ExchangeFence mechanism re-checkpoints the shadow pod, creates a StatefulSet-owned replacement, and drains both message queues to guarantee zero message loss during the handoff. An evaluation on a bare-metal Kubernetes cluster with 280 migration runs across four configurations and seven message rates shows that, compared to the sequential baseline on the same StatefulSet workload, the ShadowPod strategy reduces the restore phase by up to 92%, eliminates service downtime, and reduces total migration time by up to 77%, with zero message loss across all 280 runs.

## 내 메모


