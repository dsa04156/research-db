---
type: research-source
item_id: 2845
title: "Serverless Guardian: An Integrated Intrusion Detection and Automated Response Framework for Cloud-Native Security"
source: "openalex"
published: "2026-09-15"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "doi:10.63345/jqst.v3i3.434"
url: "https://doi.org/10.63345/jqst.v3i3.434"
generated_by: codex-research-db
aliases:
  - "Serverless Guardian: An Integrated Intrusion Detection and Automated Response Framework for Cloud-Native Security"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Serverless Guardian: An Integrated Intrusion Detection and Automated Response Framework for Cloud-Native Security

[원문 열기](https://doi.org/10.63345/jqst.v3i3.434)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`REAMUIFU`)
- 발행일: 2026-09-15
- 저자: Jon Garcia
- 식별자: `doi:10.63345/jqst.v3i3.434`

## 요약·초록

Serverless computing platforms such as AWS Lambda have revolutionized cloud application design by enabling stateless, event-driven architectures with automatic scaling and fine-grained billing. However, the ephemeral and opaque nature of these environments poses significant challenges for traditional intrusion detection systems, which are often incompatible with transient execution flows and lack fine-grained observability [1]. This paper presents SageShield-SOAR, a comprehensive serverless-aware intrusion detection and automated response framework that extends the SageShield detection engine [1] with Security Orchestration, Automation, and Response (SOAR) capabilities [2], [3]. The framework combines cold-start-aware telemetry modeling, transformer-based embedding of execution traces, probabilistic anomaly detection using hybrid density estimation techniques, and a serverless SOAR pipeline for automated incident response [1], [4]. The system integrates seamlessly with AWS services including CloudWatch, X-Ray, Step Functions, GuardDuty, EventBridge, Lambda, and SQS to provide real-time alerts and policy-driven mitigation without interfering with business logic [1], [5]. Building upon the cyber defense system framework of Mistry et al. [6], SageShield-SOAR implements a case-based threat scoring mechanism where related events are aggregated into cases, threat scores are dynamically updated, and significance conditions trigger automated response actions [6]. The framework also incorporates the automated anomaly detection and response system described in the Mistry patent [7], which provides contextual analysis and adaptive response capabilities for cloud security. Extensive experiments on synthetic and real-world Lambda workloads demonstrate that SageShield achieves a detection accuracy of 96.2%, maintains a low false positive rate of 2.8%, and introduces less than 3.1% runtime overhead [1].

## 내 메모
