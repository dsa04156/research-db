---
type: research-source
item_id: 1339
title: "Q-FE: A Quantum-Native 6G Far-Edge Architecture Securing Industrial IoT Digital Twins via CSIDH-PQC and Asynchronous Federated Learning"
source: "arxiv"
published: "2026-06-02T13:13:44Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.03611"
url: "https://arxiv.org/abs/2606.03611v1"
generated_by: codex-research-db
aliases:
  - "Q-FE: A Quantum-Native 6G Far-Edge Architecture Securing Industrial IoT Digital Twins via CSIDH-PQC and Asynchronous Federated Learning"
topics:
  - "edge-computing"
---

# Q-FE: A Quantum-Native 6G Far-Edge Architecture Securing Industrial IoT Digital Twins via CSIDH-PQC and Asynchronous Federated Learning

[원문 열기](https://arxiv.org/abs/2606.03611v1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8ZBEN72J`)
- 발행일: 2026-06-02T13:13:44Z
- 저자: Vincenzo Sammartino
- 식별자: `arxiv:2606.03611`

## 요약·초록

Sixth-generation (6G) wireless networks will underpin ultra-dense Industrial IoT (IIoT) ecosystems in which resource-constrained Far-Edge devices -- autonomous mobile robots, industrial actuators, connected vehicles -- must simultaneously satisfy sub-millisecond latency, $10^{-7}$-class reliability, and decades-long cryptographic security. Current architectures delegate Digital Twin (DT) computation to centralised cloud or Mobile Edge Computing (MEC) servers, incurring prohibitive round-trip latency, and rely on classical public-key cryptography vulnerable to quantum attacks under the harvest-now, decrypt-later (HNDL) threat model. We propose Q-FE, a Quantum-Native 6G Far-Edge architecture integrating three co-designed components: (i) Micro-Digital Twins ($μ$DTs) co-located with 6G base stations and high-capability endpoints; (ii) a Cross-Layer Post-Quantum Key Exchange module embedding CSIDH-512 isogeny key material directly within MAC-layer control frames, exploiting the scheme's uniquely compact keys ($\le 64$ bytes) to avoid packet fragmentation; and (iii) an Asynchronous Federated Learning (AFL) protocol governed by lightweight DAG smart contracts at MEC nodes, eliminating straggler bottlenecks and preventing model-poisoning and Sybil attacks without exposing raw data. End-to-end simulations (NS-3 + PySyft) demonstrate that Q-FE reduces MAC-layer overhead by 62% versus ML-KEM/Kyber-1024, maintains P99.9 URLLC latency at 0.78 ms, and accelerates global-model convergence by 31% over synchronous Federated Learning. Protocol complexity analysis confirms $O(N \log R)$ per aggregation round, and $μ$DT handover migration completes in $1.9 \pm 0.3$ ms across $10^4$ simulated events. A formal threat model confirms resilience against quantum eavesdropping, model-poisoning, and Sybil attacks.

## 내 메모


