---
type: research-source
item_id: 2843
title: "HED-ID: a federated expert system for interpretable and resource-adaptive intrusion detection on edge devices"
source: "openalex"
published: "2026-09-15"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-61336-6"
url: "https://doi.org/10.1038/s41598-026-61336-6"
generated_by: codex-research-db
aliases:
  - "HED-ID: a federated expert system for interpretable and resource-adaptive intrusion detection on edge devices"
topics:
  - "edge-computing"
---

# HED-ID: a federated expert system for interpretable and resource-adaptive intrusion detection on edge devices

[원문 열기](https://doi.org/10.1038/s41598-026-61336-6)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-09-15
- 저자: Kushboo Nasir, Sahar Badri, Asad Masood Khattak, Daniyal Alghazzawi, Mohammed Yahya Alghamdi, Mona Alkhozae, Abeer Almakky, Rania M. Alhazmi, Muhammad Zubair Asghar
- 식별자: `doi:10.1038/s41598-026-61336-6`

## 요약·초록

Abstract The proliferation of edge computing in industrial and IoT networks necessitates expert systems that support accurate, interpretable, and resource-efficient intrusion detection under strict privacy and computational constraints. This paper presents HED-ID , a fully integrated federated expert system designed for real-time, edge-oriented anomaly detection. The system combines: (i) a stacked bidirectional GRU (BiGRU) architecture with hybrid temporal–spatial attention for sequential and feature-level anomaly modeling, (ii) a resource-adaptive Grey Wolf Optimizer (A-GWO) that modulates exploration–exploitation behavior based on real-time CPU utilization and Bayesian epistemic uncertainty, with formal convergence proof under bounded resource shifts (Appendix A), (iii) federated SHAP, which aggregates local explanations using weighted averaging to produce consistent global attributions without sharing raw data, (iv) a multi-objective fitness function that simultaneously considers accuracy, model complexity, and predictive uncertainty, and (v) SHAP-guided iterative pruning for reducing computational overhead while preserving model fidelity. Empirical evaluation on CICIDS-2017, UNSW-NB15, ToN-IoT, and a noisy-edge variant of ToN-IoT (10–20% controlled packet loss and jitter) demonstrates 95.6% accuracy in cloud-like conditions and 93.8% on Raspberry Pi 4 (4 GB RAM) before pruning, with inference latency maintained within 18–22 ms. Post-pruning, memory usage decreases from 92 to 115 MB to 78–96 MB, with ≤ 1.1% accuracy degradation. To support deployment, Docker orchestration templates, pruning threshold configurations, and Grafana-based monitoring are provided—reducing retraining interventions from 11 to 4 per year in a simulated 50-device edge environment.

## 내 메모
