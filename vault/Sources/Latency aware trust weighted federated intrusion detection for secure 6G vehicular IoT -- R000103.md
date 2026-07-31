---
type: research-source
item_id: 103
title: "Latency aware trust weighted federated intrusion detection for secure 6G vehicular IoT"
source: "openalex"
published: "2026-07-27"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1007/s10791-026-10344-1"
url: "https://doi.org/10.1007/s10791-026-10344-1"
generated_by: codex-research-db
aliases:
  - "Latency aware trust weighted federated intrusion detection for secure 6G vehicular IoT"
topics:
  - "edge-computing"
---

# Latency aware trust weighted federated intrusion detection for secure 6G vehicular IoT

[원문 열기](https://doi.org/10.1007/s10791-026-10344-1)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`HI9NEWXF`)
- 발행일: 2026-07-27
- 저자: Quazi Mamun, Md Mujibur Rahman, Md Mehedi Hasan, Muhammad Rana
- 식별자: `doi:10.1007/s10791-026-10344-1`

## 요약·초록

Abstract This paper proposes a federated intrusion-detection framework for autonomous-vehicle Internet of Things (IoT) networks in future 6G transport systems. Here, IoT refers to the connected sensors, vehicles, roadside units, and control platforms that continuously exchange operational data. The framework, FL-AIID-AV, allows vehicles to train a shared detection model without sending raw traffic or sensor data to a central server. Its secure aggregation mechanism for autonomous vehicle (SecAggAV), combines anomaly screening of model updates, history-based trust weighting, client-side differential privacy, encrypted update transport, and latency-aware round control. In the current implementation, the aggregation server is trusted for decryption, anomaly scoring, and trust computation, while encryption protects updates in transit. This trusted-server assumption is intended as a pragmatic transitional design choice for near-term edge-cloud 6G deployments rather than as the end-state of a fully decentralised 6G architecture; the same trust-weighting logic can later be migrated to server-opaque or multi-coordinator secure aggregation. On the CICIoV2024 benchmark, the method reaches 98.2% accuracy in benign settings and 95.4% under 20% poisoning, with edge inference latency below 50 ms. We additionally evaluate the method on TON-IoT, Edge-IIoTset, and a strict de-duplicated CICIoV2024 split. Under this complementary evaluation track, SecAggAV attains 97.42% accuracy on TON-IoT, 95.84% on Edge-IIoTset, and a macro-F1 score, that is, the unweighted average F1 across classes, of 0.712 on the de-duplicated CICIoV2024 corpus. Overall, the results show that the proposed framework remains robust under heterogeneous data, adversarial updates, and latency constraints while providing better visibility into minority-attack detection.

## 내 메모


