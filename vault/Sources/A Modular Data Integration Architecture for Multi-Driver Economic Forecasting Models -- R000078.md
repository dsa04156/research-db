---
type: research-source
item_id: 78
title: "A Modular Data Integration Architecture for Multi-Driver Economic Forecasting Models"
source: "openalex"
published: "2026-07-21"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.58425/ajt.v5i8.584"
url: "https://doi.org/10.58425/ajt.v5i8.584"
generated_by: codex-research-db
aliases:
  - "A Modular Data Integration Architecture for Multi-Driver Economic Forecasting Models"
topics:
  - "cloud-infrastructure"
---

# A Modular Data Integration Architecture for Multi-Driver Economic Forecasting Models

[원문 열기](https://doi.org/10.58425/ajt.v5i8.584)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`KM94PIEF`)
- 발행일: 2026-07-21
- 저자: Soumya Gummalla
- 식별자: `doi:10.58425/ajt.v5i8.584`

## 요약·초록

Aim: This study aims to design and evaluate a modular serverless ETL orchestration framework capable of producing temporally aligned, validated, and reproducible datasets for causal econometric modeling from heterogeneous enterprise data sources. Methods: Using a design science research approach, a modular serverless ETL pipeline was developed and evaluated using five heterogeneous production-scale data sources. Pipeline performance was assessed using temporal alignment, completeness, financial integrity, execution time, infrastructure cost, and downstream model stability. The proposed serverless ETL orchestration layer employs source-specific transformation jobs for temporal-range expansion of contractual data, multi-currency normalization, growth-rate-based backfilling of partial time series, and aggregation of multi-source forecasts. Pipeline correctness is verified through schema checkpoints, temporal alignment assertions, and automated quality gates. The pipeline is evaluated using production-size inputs comprising five heterogeneous data sources and approximately 50,000 monthly contract records, which are expanded into more than 500,000 monthly observations. Results: The pipeline consolidated heterogeneous data into a single dataset with no null values and maintained financial integrity within a $0.01 rounding error per contract. The serverless approach achieved an 86% cost reduction, operating at $7.20 per cycle with an approximately 45-minute runtime. Results showed a measurable reduction in inter-cycle coefficient variability following implementation of the automated pipeline. Conclusion: The findings indicate that principled data engineering at the data ingestion level plays a critical role in improving the validity and reliability of downstream causal econometric modeling Recommendation: Organizations should adopt a modular, federated serverless ETL pipeline with distributed processing, cross-cluster data federation, fine-grained access governance, and automated quality controls to improve the reliability of downstream causal attributions and address structural data heterogeneity.

## 내 메모


