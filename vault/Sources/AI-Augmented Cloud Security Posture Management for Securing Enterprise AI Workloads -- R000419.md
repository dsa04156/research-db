---
type: research-source
item_id: 419
title: "AI-Augmented Cloud Security Posture Management for Securing Enterprise AI Workloads"
source: "openalex"
published: "2024-06-30"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.32628/cseit25113585"
url: "https://doi.org/10.32628/cseit25113585"
generated_by: codex-research-db
aliases:
  - "AI-Augmented Cloud Security Posture Management for Securing Enterprise AI Workloads"
topics:
  - "cloud-infrastructure"
---

# AI-Augmented Cloud Security Posture Management for Securing Enterprise AI Workloads

[원문 열기](https://doi.org/10.32628/cseit25113585)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`43XI8JPM`)
- 발행일: 2024-06-30
- 저자: Lakshmi Kiran Meesala Lakshmi Kiran Meesala
- 식별자: `doi:10.32628/cseit25113585`

## 요약·초록

Cloud Security Posture Management (CSPM) has historically targeted infrastructure misconfigurations - exposed storage buckets, overprivileged IAM roles, and open network ports. The proliferation of AI workloads across enterprise clouds introduces fundamentally novel attack vectors: GPU resource hijacking, model training data exfiltration, shadow AI deployments, prompt injection surfaces, and insecure ML pipeline configurations. Existing CSPM frameworks lack semantics for AI asset discovery, AI-specific policy enforcement, and behavioral anomaly detection across ephemeral GPU compute clusters. This paper proposes AI-Aware CSPM (AA-CSPM), an architectural extension that integrates ML-based risk scoring, AI-specific misconfiguration detection rules, data lineage monitoring, and convergent posture management across CSPM, Data Security Posture Management (DSPM), and Cloud Infrastructure Entitlement Management (CIEM). We formalize a threat taxonomy of twelve AI-era attack classes, implement detection pipelines across three major cloud providers (AWS SageMaker, Google Vertex AI, Azure ML), and benchmark AA-CSPM against three baseline CSPM platforms. AA-CSPM achieves a mean detection accuracy of 94.3%, a false-positive reduction of 38.7%, and reduces mean time-to-detect (MTTD) for AI-specific misconfigurations by 61.4% over legacy baselines. These results demonstrate that AI workloads constitute a distinct and underserved risk domain that demands dedicated posture management tooling.

## 내 메모


