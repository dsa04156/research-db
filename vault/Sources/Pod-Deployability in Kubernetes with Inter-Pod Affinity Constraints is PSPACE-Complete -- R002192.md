---
type: research-source
item_id: 2192
title: "Pod-Deployability in Kubernetes with Inter-Pod Affinity Constraints is PSPACE-Complete"
source: "arxiv"
published: "2026-08-20T09:19:10Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.19822"
url: "https://arxiv.org/abs/2608.19822v1"
generated_by: codex-research-db
aliases:
  - "Pod-Deployability in Kubernetes with Inter-Pod Affinity Constraints is PSPACE-Complete"
topics:
  - "kubernetes"
---

# Pod-Deployability in Kubernetes with Inter-Pod Affinity Constraints is PSPACE-Complete

[원문 열기](https://arxiv.org/abs/2608.19822v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-20T09:19:10Z
- 저자: Saverio Giallorenzo, Jacopo Mauro, Gianluigi Zavattaro
- 식별자: `arxiv:2608.19822`

## 요약·초록

Kubernetes is the de-facto platform for container orchestration. Its scheduler combines resource capacities with label-based affinity and anti-affinity rules, and the interaction of these features can make the eventual placement of a pod. In this paper, we study the pod-deployability problem: given an initial cluster, a pod type, and a designated node, does some legal sequence of pod deployments and deletions cover the target pair? We give three complexity results. First, when dynamic constraints contain no affinity (anti-affinity is allowed), pod-deployability is decidable in polynomial time. Second, required affinity together with required anti-affinity makes the problem PSPACE-complete. Third, required affinity alone is already enough for PSPACE-completeness on a single node with one scalar capacity. The lower bounds encode, respectively, 1-safe Petri-net coverability and bounded black pebbling. These results isolate two independent sources of state-space complexity in Kubernetes scheduling: logical exclusion and resource-bounded prerequisite management.

## 내 메모


