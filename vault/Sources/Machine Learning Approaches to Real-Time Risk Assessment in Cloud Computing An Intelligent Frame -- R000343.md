---
type: research-source
item_id: 343
title: "Machine Learning Approaches to Real-Time Risk Assessment in Cloud Computing: An Intelligent Framework for Proactive Threat Detection"
source: "openalex"
published: "2024-07-01"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.59324/ejaset.2024.2(4).11"
url: "https://doi.org/10.59324/ejaset.2024.2(4).11"
generated_by: codex-research-db
aliases:
  - "Machine Learning Approaches to Real-Time Risk Assessment in Cloud Computing: An Intelligent Framework for Proactive Threat Detection"
topics:
  - "cloud-infrastructure"
  - "kubernetes"
---

# Machine Learning Approaches to Real-Time Risk Assessment in Cloud Computing: An Intelligent Framework for Proactive Threat Detection

[원문 열기](https://doi.org/10.59324/ejaset.2024.2(4).11)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`U9632EN2`)
- 발행일: 2024-07-01
- 저자: M. A. M. Khan, Md Obayed Al Rahman, Md Kamrul Hasan
- 식별자: `doi:10.59324/ejaset.2024.2(4).11`

## 요약·초록

The high-velocity, dynamic and multi-tenant nature of cloud computing presents risks that conventional monitoring systems cannot effectively address. This work will develop an integrated machine-learning platform for real-time assessment of cloud risks, capable of recognising known prey, identifying new exceptions, predicting future risks, and adapting to dynamic workload states. The methodology was based on supervised learning (XGBoost, Random Forest), unsupervised anomaly detection (autoencoders, Isolation Forest), temporal deep learning (GRU/LSTM), and drift-sensitive retraining, deployed in a Kafka, Flink, and Kubernetes streaming system. The metrics used to evaluate model performance included accuracy, precision-recall, latency, scalability, drift resilience, fairness analysis, and operational cost. The best performance was achieved with XGBoost, with an accuracy of 98.6% and an ROC-AUC of 0.992, making the model the most powerful supervised classifier. The autoencoder achieves 89.7% and 93.4% accuracy at 1% and 0.5% alert thresholds, respectively, and achieves the highest accuracy among the anomaly detectors. GRU models achieved a prediction lead time of 61 seconds, which was sufficient to implement countermeasures. In contrast, drift-adaptation recovered F1 performance, which had dropped to 84.6% in drift to 95.2% after adaptation. Under the load, the system's median latency was 61 ms, indicating feasibility for real-time operation. The fairness analysis identified a notable -7.9% difference in detection for Tenant C, which is a governance requirement. In general, the framework is highly accurate, flexible, and operationally reliable. The recommended practices by cloud operators include using multi-model pipelines, constant drift monitoring, tenancy-achieving, thinning controls, alert thresholds, and explainability and governance controls, as well as features that ensure sustainable deployment and build trust.

## 내 메모


