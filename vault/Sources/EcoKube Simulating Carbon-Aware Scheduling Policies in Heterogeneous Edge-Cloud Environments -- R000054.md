---
type: research-source
item_id: 54
title: "EcoKube: Simulating Carbon-Aware Scheduling Policies in Heterogeneous Edge-Cloud Environments"
source: "arxiv"
published: "2026-07-10T11:57:42Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3802513.3803486"
url: "https://arxiv.org/abs/2607.09318v1"
generated_by: codex-research-db
aliases:
  - "EcoKube: Simulating Carbon-Aware Scheduling Policies in Heterogeneous Edge-Cloud Environments"
topics:
  - "kubernetes"
---

# EcoKube: Simulating Carbon-Aware Scheduling Policies in Heterogeneous Edge-Cloud Environments

[원문 열기](https://arxiv.org/abs/2607.09318v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`9NVD86J2`)
- 발행일: 2026-07-10T11:57:42Z
- 저자: Gonçalo Ferreira, Shashikant Ilager
- 식별자: `doi:10.1145/3802513.3803486`

## 요약·초록

Energy demand from cloud and edge computing is rising rapidly, with AI workloads further intensifying electricity use and associated carbon emissions. In hybrid edge-cloud settings, sustainability impact depends on time- and location-varying grid Carbon Intensity (CI), site Power Usage Effectiveness (PUE), and heterogeneous hardware characteristics. Existing carbon-aware work explores solutions such as temporal elasticity, spatio-temporal workload shifting, and carbon-aware placement across distributed sites. However, these solutions do not provide a consistent and reproducible workflow for evaluating sustainability-aware scheduling policies on heterogeneous, federated edge-cloud topologies. We present EcoKube: a configurable simulation framework for the reproducible evaluation of sustainability-aware scheduling policies in heterogeneous edge-cloud environments. The framework includes an event-driven deterministic simulator, policy hooks, and a heterogeneity-aware reference policy. We evaluate the framework with synthetic batch workloads, comparing the reference policy against the default Kubernetes scheduler, KEIDS, and TOPSIS/KCSS. The contribution is architectural and experimental: EcoKube provides a reproducible way to compare sustainability-aware policies before deployment.

## 내 메모


