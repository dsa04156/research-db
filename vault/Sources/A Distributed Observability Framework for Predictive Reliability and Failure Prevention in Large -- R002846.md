---
type: research-source
item_id: 2846
title: "A Distributed Observability Framework for Predictive Reliability and Failure Prevention in Large-Scale Cloud Infrastructure"
source: "openalex"
published: "2026-09-13"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "doi:10.58425/ajt.v5i11.608"
url: "https://doi.org/10.58425/ajt.v5i11.608"
generated_by: codex-research-db
aliases:
  - "A Distributed Observability Framework for Predictive Reliability and Failure Prevention in Large-Scale Cloud Infrastructure"
topics:
  - "cloud-infrastructure"
  - "kubernetes"
---

# A Distributed Observability Framework for Predictive Reliability and Failure Prevention in Large-Scale Cloud Infrastructure

[원문 열기](https://doi.org/10.58425/ajt.v5i11.608)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-09-13
- 저자: Chiranjevi Sai Venkat Kaushik Dhulipudi
- 식별자: `doi:10.58425/ajt.v5i11.608`

## 요약·초록

Aim: This study aimed to develop, implement, and evaluate a Distributed Observability Framework (DOF) for proactive reliability management in large-scale cloud-native infrastructures. The framework integrates telemetry collection, dependency-aware observability analysis, machine learning, dynamic observability scoring, and policy-driven automated actions to support early identification and prioritization of potential reliability risks. Methods: The framework was implemented in a Kubernetes environment and integrated OpenTelemetry, Jaeger, Prometheus, and Grafana to monitor application and infrastructure services. We contextualized observability data using logs, infrastructure metrics, application data, distributed traces, Kubernetes events, and service-dependency information. Historical operational data and multiple simulated failure scenarios were used to develop and evaluate predictive models. We compared the proposed framework's performance with a reference monitoring strategy based on conventional static thresholds. Results: The evaluation showed that the proposed framework reduced unwanted alerts in the evaluated context, improved the prioritization of critical services during high-alert scenarios, and enabled earlier detection of service deterioration compared with conventional threshold-based monitoring. However, the study did not report quantitative measures of prediction accuracy, mean time to detect (MTTD), mean time to breakdown (MTTB), or service availability. Consequently, the magnitude and statistical significance of the observed improvements could not be fully established. Conclusion: The proposed DOF provides a basis for supporting preventive reliability practices across cloud engineering, DevOps, and Site Reliability Engineering (SRE) teams. Recommendations: Future evaluations should report quantitative performance indicators, including prediction accuracy, precision, recall, F1-score, MTTD, MTTB, service availability, false-positive rates, and effect sizes. Future research should also evaluate the framework using larger real-world operational datasets, diverse failure conditions, and longer observation periods to establish its generalizability and practical effectiveness.

## 내 메모
