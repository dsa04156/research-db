---
type: research-source
item_id: 1793
title: "Edge-Compute AI Surveillance: A Low-Cost Predictive Maintenance System for Marginal Field ESPs Validated on Real Offshore ESP Vibration Data"
source: "crossref"
published: "2026-08-10"
first_seen: "2026-08-10"
review_status: "pending"
canonical_key: "doi:10.2118/235017-ms"
url: "https://doi.org/10.2118/235017-ms"
generated_by: codex-research-db
aliases:
  - "Edge-Compute AI Surveillance: A Low-Cost Predictive Maintenance System for Marginal Field ESPs Validated on Real Offshore ESP Vibration Data"
topics:
  - "kubernetes"
---

# Edge-Compute AI Surveillance: A Low-Cost Predictive Maintenance System for Marginal Field ESPs Validated on Real Offshore ESP Vibration Data

[원문 열기](https://doi.org/10.2118/235017-ms)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-10|2026-08-10]]
- 수집 채널: `crossref`
- 검토 상태: `pending`
- 발행일: 2026-08-10
- 저자: U. S. Ahmad
- 식별자: `doi:10.2118/235017-ms`

## 요약·초록

Abstract Electrical submersible pumps (ESPs) are the primary artificial lift mechanism for marginal oilfields in the Niger Delta, yet continuous condition monitoring remains economically prohibitive for most indigenous operators. Conventional supervisory control and data acquisition (SCADA) systems cost between USD 800 and USD 2,500 per monitoring point and require cloud infrastructure that is incompatible with remote field operations. This study presents a semi-supervised Isolation Forest fault detection framework trained exclusively on normal-condition vibration data, requiring no historical failure records, deployed on a low-cost Wi-Fi-enabled edge microcontroller with a locally hosted Progressive Web Application (PWA) dashboard for real-time field surveillance without internet connectivity. Model development and validation used the ESPset real offshore vibration dataset (Pellegrini et al. 2025), comprising 6,032 records from 11 pump units representing five operating conditions: Normal, Unbalance, Faulty Sensor, Rubbing, and Misalignment. Seven frequency-domain features derived from shaft-speed-normalised vibration spectra were used as model inputs. Training used 3,840 Normal-class records only; evaluation used a held-out test set of 2,192 records (961 Normal, 1,231 Fault). The system achieved an area under the receiver operating characteristic curve (AUC-ROC) of 0.9585, an area under the precision-recall curve (PR-AUC) of 0.9542, a recall of 0.9748, a precision of 0.8584, and an F1-score of 0.9129. Per-fault recall rates were 0.9948 for Unbalance, 0.9898 for Faulty Sensor, 0.9138 for Rubbing, and a perfect 1 for Misalignment. Five-fold stratified cross-validation confirmed AUC-ROC stability at 0.9549 +/- 0.004. Total hardware cost per monitoring node is below USD 50, against a USD 4 million average cost per unplanned ESP failure. This paper provides the first published performance benchmark for a semi-supervised, edge-deployed vibration fault detector validated on real offshore ESP data with a local field interface designed for the constraints of Nigerian marginal oilfields.

## 내 메모


