---
type: research-source
item_id: 1226
title: "Stateless Snowflake: A Cloud-Agnostic Distributed ID Generator Using Network-Derived Identity"
source: "arxiv"
published: "2025-12-12T15:21:33Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2512.11643"
url: "https://arxiv.org/abs/2512.11643v1"
generated_by: codex-research-db
aliases:
  - "Stateless Snowflake: A Cloud-Agnostic Distributed ID Generator Using Network-Derived Identity"
topics:
  - "kubernetes"
---

# Stateless Snowflake: A Cloud-Agnostic Distributed ID Generator Using Network-Derived Identity

[원문 열기](https://arxiv.org/abs/2512.11643v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`28WJ6PNC`)
- 발행일: 2025-12-12T15:21:33Z
- 저자: Manideep Reddy Chinthareddy
- 식별자: `arxiv:2512.11643`

## 요약·초록

Snowflake-style distributed ID generators are the industry standard for producing k-ordered, unique identifiers at scale. However, the traditional requirement for manually assigned or centrally coordinated worker IDs introduces significant friction in modern container-orchestrated environments (e.g., Kubernetes), where workloads are ephemeral and autoscaled. In such systems, maintaining stable worker identities requires complex stateful sets or external coordination services (e.g., ZooKeeper), negating the operational benefits of stateless microservices. This paper presents a cloud-agnostic, container-native ID generation protocol that eliminates the dependency on explicit worker IDs. By deriving node uniqueness deterministically from ephemeral network properties - specifically the container's private IPv4 address - the proposed method removes the need for centralized coordination. We introduce a modified bit-allocation scheme (1-41-16-6) that accommodates 16 bits of network-derived entropy while preserving strict monotonicity. We validate the approach across AWS, GCP, and Azure environments. Evaluation results demonstrate that while the design has a theoretical single-node ceiling of approximately 64,000 TPS, in practical microservice deployments the network I/O dominates latency, resulting in end-to-end performance (approximately 31,000 TPS on a 3-node cluster) comparable to classic stateful generators while offering effectively unbounded horizontal scalability.

## 내 메모


