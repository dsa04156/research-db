---
type: research-source
item_id: 1810
title: "Edge-Deployed Machine Learning Sensor (MLSensor) for Real-Time Anomaly Detection in Electrical Submersible"
source: "crossref"
published: "2026-08-10"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "doi:10.2118/235027-ms"
url: "https://doi.org/10.2118/235027-ms"
generated_by: codex-research-db
aliases:
  - "Edge-Deployed Machine Learning Sensor (MLSensor) for Real-Time Anomaly Detection in Electrical Submersible"
topics:
  - "edge-computing"
---

# Edge-Deployed Machine Learning Sensor (MLSensor) for Real-Time Anomaly Detection in Electrical Submersible

[원문 열기](https://doi.org/10.2118/235027-ms)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `crossref`
- 검토 상태: `pending`
- 발행일: 2026-08-10
- 저자: T. M. Busoye, Q. A. Jokomba, O. M. Busoye, A. O. Joledo
- 식별자: `doi:10.2118/235027-ms`

## 요약·초록

Abstract Electrical Submersible Pumps (ESPs) are critical artificial lift assets whose unexpected failure causes significant non-productive time and workover costs, with unplanned shutdowns lasting up to several weeks. Existing monitoring systems rely on reactive, threshold-based alarms applied to surface measurements. These traditional methods cannot detect incipient faults—such as early-stage gas locking, progressive impeller erosion, and developing bearing friction—and struggle to distinguish between faults that produce overlapping, single-channel signal signatures. While the governing equations of ESP operation are well established, their direct application to fault detection remains impractical in the field. Fault-relevant parameters like effective fluid density are not directly measurable from surface instrumentation, and differentiating noisy speed measurements to recover analytical quantities amplifies uncertainty to impractical levels. To address these limitations, this paper presents MLSensor, an edge-deployed machine learning framework that bridges physics-based understanding with data-driven implementation. To overcome the scarcity of labelled field data, a multi-domain Digital Twin was developed in OpenModelica, coupling Kloss motor dynamics with Affinity Law hydraulics. This twin generated twelve labelled simulation runs across three fault types at three severity levels, incorporating Gaussian sensor noise at 10–45 dB SNR to mimic real-world conditions. A 46-element feature vector, including four novel cross-modal electrical-hydraulic decoupling features (such as the highly discriminative decouplingIQ, was extracted per 2-second window. A Random Forest classifier achieved a 100% precision, recall, and F1-score classification accuracy under a temporal train/test split, validating the discriminative completeness of the cross-modal feature representation on simulation data. Finally, the trained model was deployed on an ESP32 microcontroller, achieving a 427 µs average inference latency while utilizing only 23% of program flash and 6% of SRAM, proving the viability of cloud-independent, real-time edge inference.

## 내 메모


