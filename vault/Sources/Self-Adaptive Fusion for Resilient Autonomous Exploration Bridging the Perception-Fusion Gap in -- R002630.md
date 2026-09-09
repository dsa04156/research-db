---
type: research-source
item_id: 2630
title: "Self-Adaptive Fusion for Resilient Autonomous Exploration: Bridging the Perception-Fusion Gap in Deep Space Missions"
source: "openalex"
published: "2026-09-04"
first_seen: "2026-09-07"
review_status: "pending"
canonical_key: "doi:10.58830/ozgur.pub1403.c5650"
url: "https://doi.org/10.58830/ozgur.pub1403.c5650"
generated_by: codex-research-db
aliases:
  - "Self-Adaptive Fusion for Resilient Autonomous Exploration: Bridging the Perception-Fusion Gap in Deep Space Missions"
topics:
  - "edge-computing"
---

# Self-Adaptive Fusion for Resilient Autonomous Exploration: Bridging the Perception-Fusion Gap in Deep Space Missions

[원문 열기](https://doi.org/10.58830/ozgur.pub1403.c5650)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-09-07|2026-09-07]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`24HE6DFQ`)
- 발행일: 2026-09-04
- 저자: Ayfer Göksu Bakır, Murat Gökşin Bakir
- 식별자: `doi:10.58830/ozgur.pub1403.c5650`

## 요약·초록

Deep-space exploration requires autonomous systems capable of navigating environments where sensor reliability is compromised by cosmic radiation, solar flares, and hardware degradation. This research addresses the "Perception-Fusion Gap"—the failure of static AI models to adapt when environmental conditions shift dynamically. We propose a modular framework that treats data integration as a continuous state estimation problem rather than a static weighted average. At the core of this strategy is a Kalman Filter-based fusion engine [1]. By utilizing the state prediction and fusion update equations, the system models the reliability of heterogeneous sensor streams in real-time. The Kalman Gain serves as a dynamic weighting mechanism, automatically favoring the model’s internal state prediction or the incoming sensor measurement based on the calculated covariance of their respective errors. This allows the vehicle to "self-repair" its perception logic during flight without manual re-calibration. To further enhance resilience, we integrate Meta-Learning Controllers (planned for WP3) that observe past fusion errors to predict future sensor drifts. This dual approach ensures that even if a primary modality, such as LiDAR, is blinded or compromised, the system can seamlessly shift reliance to secondary modalities like multispectral imagery or inertial sensors. Experimental benchmarks against static fusion baselines demonstrate that this adaptive approach significantly improves system robustness under abrupt data shifts. By bridging the gap between raw data perception and intelligent decision-making, this methodology provides a reliable foundation for the next generation of autonomous deepspace vehicles [6]. Keywords: Autonomous Systems, Self-Adaptive Fusion, Meta-Learning, Edge Computing, Sensor Resilience, State Estimation.

## 내 메모


