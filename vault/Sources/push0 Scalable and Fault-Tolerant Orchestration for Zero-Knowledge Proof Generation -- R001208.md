---
type: research-source
item_id: 1208
title: "push0: Scalable and Fault-Tolerant Orchestration for Zero-Knowledge Proof Generation"
source: "arxiv"
published: "2026-02-18T10:22:33Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2602.16338"
url: "https://arxiv.org/abs/2602.16338v1"
generated_by: codex-research-db
aliases:
  - "push0: Scalable and Fault-Tolerant Orchestration for Zero-Knowledge Proof Generation"
topics:
  - "kubernetes"
---

# push0: Scalable and Fault-Tolerant Orchestration for Zero-Knowledge Proof Generation

[원문 열기](https://arxiv.org/abs/2602.16338v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`F6XD2ZR8`)
- 발행일: 2026-02-18T10:22:33Z
- 저자: Mohsen Ahmadvand, Rok Pajnič, Ching-Lun Chiu
- 식별자: `arxiv:2602.16338`

## 요약·초록

Zero-knowledge proof generation imposes stringent timing and reliability constraints on blockchain systems. For ZK-rollups, delayed proofs cause finality lag and economic loss; for Ethereum's emerging L1 zkEVM, proofs must complete within the 12-second slot window to enable stateless validation. The Ethereum Foundation's Ethproofs initiative coordinates multiple independent zkVMs across proving clusters to achieve real-time block proving, yet no principled orchestration framework addresses the joint challenges of (i) strict head-of-chain ordering, (ii) sub-slot latency bounds, (iii) fault-tolerant task reassignment, and (iv) prover-agnostic workflow composition. We present push0, a cloud-native proof orchestration system that decouples prover binaries from scheduling infrastructure. push0 employs an event-driven dispatcher--collector architecture over persistent priority queues, enforcing block-sequential proving while exploiting intra-block parallelism. We formalize requirements drawn from production ZK-rollup operations and the Ethereum real-time proving specification, then demonstrate via production Kubernetes cluster experiments that push0 achieves 5 ms median orchestration overhead with 99--100% scaling efficiency at 32 dispatchers for realistic workloads--overhead negligible (less than 0.1%) relative to typical proof computation times of 7+ seconds. Controlled Docker experiments validate these results, showing comparable performance (3--10 ms P50) when network variance is eliminated. Production deployment on the Zircuit zkrollup (14+ million mainnet blocks since March 2025) provides ecological validity for these controlled experiments. Our design enables seamless integration of heterogeneous zkVMs, supports automatic task recovery via message persistence, and provides the scheduling primitives necessary for both centralized rollup operators and decentralized multi-prover networks.

## 내 메모


