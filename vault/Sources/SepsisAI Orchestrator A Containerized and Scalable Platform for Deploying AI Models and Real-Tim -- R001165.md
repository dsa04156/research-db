---
type: research-source
item_id: 1165
title: "SepsisAI Orchestrator: A Containerized and Scalable Platform for Deploying AI Models and Real-Time Monitoring in Early Sepsis Detection"
source: "arxiv"
published: "2026-05-21T11:19:31Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.22331"
url: "https://arxiv.org/abs/2605.22331v1"
generated_by: codex-research-db
aliases:
  - "SepsisAI Orchestrator: A Containerized and Scalable Platform for Deploying AI Models and Real-Time Monitoring in Early Sepsis Detection"
topics:
  - "kubernetes"
---

# SepsisAI Orchestrator: A Containerized and Scalable Platform for Deploying AI Models and Real-Time Monitoring in Early Sepsis Detection

[원문 열기](https://arxiv.org/abs/2605.22331v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8RB348KS`)
- 발행일: 2026-05-21T11:19:31Z
- 저자: Santiago Ospitia, John Sanabria, John Garcia-Henao
- 식별자: `arxiv:2605.22331`

## 요약·초록

Despite strong predictive results in the clinical machine learning literature, the translation of these models into bedside use remains limited by systems-level barriers: heterogeneous data representations, the absence of standardized deployment workflows, and a mismatch between research prototypes and the concurrency and latency requirements of hospital environments. We present the SepsisAI-Orchestrator, an open-source modular platform that addresses this deployment gap for early sepsis detection. The platform integrates HL7 FHIR-inspired Clinical Document Architecture (CDA) preprocessing, NoSQL storage, a containerized LightGBM classifier served via REST APIs, and a Streamlit clinical dashboard, orchestrated with Docker and Kubernetes. A previously validated LightGBM model (F1 0.87-0.94 on PhysioNet 2019) is reused without modification; the contribution lies in the surrounding infrastructure and its empirical characterization under load. Using k6 with 50-1000 concurrent virtual users, we find that replica count must be matched to the physical CPU thread count of the host: scaling from 3 to 12 replicas on a 12-thread CPU reduces p95 latency from 3.3s to 1.41s (57.3% reduction) and eliminates all request failures, while over-provisioning to 24 or 48 replicas degrades performance due to scheduler contention. To our knowledge this U-shaped scaling behavior has not been quantified previously for clinical AI inference workloads. We do not claim prospective clinical validation. Source code and deployment manifests are available at https://github.com/nucleusai/sepsisai-orchestrator.

## 내 메모


