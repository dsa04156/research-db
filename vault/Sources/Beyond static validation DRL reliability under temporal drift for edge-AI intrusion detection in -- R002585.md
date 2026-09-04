---
type: research-source
item_id: 2585
title: "Beyond static validation: DRL reliability under temporal drift for edge-AI intrusion detection in cyber-physical-social systems"
source: "crossref"
published: "2026-09-04"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "doi:10.1108/ijpcc-02-2026-0118"
url: "https://doi.org/10.1108/ijpcc-02-2026-0118"
generated_by: codex-research-db
aliases:
  - "Beyond static validation: DRL reliability under temporal drift for edge-AI intrusion detection in cyber-physical-social systems"
topics:
  - "kubernetes"
---

# Beyond static validation: DRL reliability under temporal drift for edge-AI intrusion detection in cyber-physical-social systems

[원문 열기](https://doi.org/10.1108/ijpcc-02-2026-0118)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `crossref`
- 검토 상태: `pending`
- 발행일: 2026-09-04
- 저자: Lakhdar Kachna, Noureddine Chaib
- 식별자: `doi:10.1108/ijpcc-02-2026-0118`

## 요약·초록

Purpose Edge-AI intrusion detection in cyber-physical-social systems (CPSS) must operate under temporal drift while respecting strict low-false-positive-rate (low-FPR) budgets. This study aims to evaluate whether a deep reinforcement learning intrusion detector, RO-DDDQN, provides a reliable low-FPR operating point under a strict temporal protocol. Design/methodology/approach The authors study a cost-sensitive Double Dueling Deep Q-Network with a GRU-based temporal encoder (RO-DDDQN) on CSE-CIC-IDS2018 under a strict day-level split (train: Feb. 14–20; validation/calibration source: Feb. 21; test: Feb. 22). Three thresholding protocols are compared at target FPR = 1%: naive validation-tail thresholding, deployable benign-tail thresholding and a non-deployable test-oracle diagnostic. RO-DDDQN is further compared with an edge-suitable XGBoost baseline under the same temporal protocol and robustness is assessed across five random seeds. Findings For the seed-42 run, validation-based threshold selection is highly misleading under drift: a threshold tuned to 1% FPR on validation inflates to 8.62% FPR on the future test day. Benign-tail calibration does not repair RO-DDDQN deployability: at a nominal 1% target, the achieved FPR rises to 9.10% with 53.39% recall. Even under a test-oracle threshold, this run reaches only 1.99% recall at 1% FPR. Multi-seed analysis shows that this outcome is not representative: across five seeds, RO-DDDQN achieves zero attack recall at oracle 1% FPR in four of five runs, with median oracle recall of 0.00%. By contrast, XGBoost generalizes more effectively (ROC-AUC 0.9736) and achieves 35.06% recall at 1.16% FPR under deployable calibration. Research limitations/implications This study is limited to one benchmark (CSE-CIC-IDS2018), one strict temporal split, one short-horizon windowing setup and one value-based DRL formulation (RO-DDDQN). Results should therefore not be interpreted as universal conclusions about all reinforcement-learning-based IDS methods or all CPSS telemetry settings. The experiments also do not include a full uncapped-window ablation and broader statistical characterization remains limited despite the added five-seed analysis. Future work should extend evaluation across rolling-origin days, additional datasets/traces and wider ablation/statistical studies. Practical implications For edge deployments operating under strict false-alarm budgets, validation metrics alone are insufficient. Practitioners should calibrate thresholds on benign-representative background traffic, explicitly test calibration transfer to future periods, run oracle and tail-overlap diagnostics to distinguish threshold mismatch from ranking collapse and assess robustness across random seeds. These checks reduce the risk of false-alarm inflation and help ensure that IDS models remain operational under temporal drift. Social implications In CPSS settings such as smart cities and critical infrastructure, unreliable intrusion alerts can waste scarce edge resources, desensitize operators and trigger unnecessary automated responses that affect services and users. More realistic evaluation of low-FPR behavior under drift supports safer deployment by reducing avoidable disruptions and improving trust in security monitoring systems that may influence cyber-physical decisions. Originality/value The study contributes a temporally faithful low-FPR evaluation protocol that separates threshold-transfer failure from ranking degradation under drift. The results show that, under the evaluated protocol, RO-DDDQN is highly seed-sensitive and does not provide a reliable low-FPR operating point, whereas calibration-transfer analysis and recall-at-fixed-FPR evaluation provide a clearer view of deployability. The findings are limited to one benchmark, one strict temporal split, one windowing setup and one DRL formulation, motivating broader rolling-origin and cross-dataset evaluation.

## 내 메모


