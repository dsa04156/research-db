---
type: research-source
item_id: 1281
title: "Democratizing Scalable Cloud Applications: Transactional Stateful Functions on Streaming Dataflows"
source: "arxiv"
published: "2025-12-19T10:29:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.4233/uuid:837e043a-c6e3-4f87-a9b1-a59a9ade65f7"
url: "https://arxiv.org/abs/2512.17429v1"
generated_by: codex-research-db
aliases:
  - "Democratizing Scalable Cloud Applications: Transactional Stateful Functions on Streaming Dataflows"
topics:
  - "cloud-infrastructure"
---

# Democratizing Scalable Cloud Applications: Transactional Stateful Functions on Streaming Dataflows

[원문 열기](https://arxiv.org/abs/2512.17429v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`I4PKGDWU`)
- 발행일: 2025-12-19T10:29:43Z
- 저자: Kyriakos Psarakis
- 식별자: `doi:10.4233/uuid:837e043a-c6e3-4f87-a9b1-a59a9ade65f7`

## 요약·초록

Web applications underpin much of modern digital life, yet building scalable and consistent cloud applications remains difficult, requiring expertise across cloud computing, distributed systems, databases, and software engineering. These demands restrict development to a small number of highly specialized engineers. This thesis aims to democratize cloud application development by addressing three challenges: programmability, high-performance fault-tolerant serializable transactions, and serverless semantics. The thesis identifies strong parallels between cloud applications and the streaming dataflow execution model. It first explores this connection through T-Statefun, a transactional extension of Apache Flink Statefun, demonstrating that dataflow systems can support transactional cloud applications via a stateful functions-as-a-service API. However, this approach revealed significant limitations in programmability and performance. To overcome these issues, the thesis introduces Stateflow, a high-level object-oriented programming model that compiles applications into stateful dataflow graphs with minimal boilerplate. Building on this model, the thesis presents Styx, a distributed streaming dataflow engine that provides deterministic, multi-partition, serializable transactions with strong fault tolerance guarantees. Styx eliminates explicit transaction failure handling and significantly outperforms state-of-the-art systems. Finally, the thesis extends Styx with transactional state migration to support elasticity under dynamic workloads.

## 내 메모


