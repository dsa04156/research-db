---
type: research-source
item_id: 1185
title: "Causal Inference for Quantifying Noisy Neighbor Effects in Multi-Tenant Cloud Environments"
source: "arxiv"
published: "2026-04-03T16:06:30Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.03145"
url: "https://arxiv.org/abs/2604.03145v1"
generated_by: codex-research-db
aliases:
  - "Causal Inference for Quantifying Noisy Neighbor Effects in Multi-Tenant Cloud Environments"
topics:
  - "kubernetes"
---

# Causal Inference for Quantifying Noisy Neighbor Effects in Multi-Tenant Cloud Environments

[원문 열기](https://arxiv.org/abs/2604.03145v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MGWGKZE7`)
- 발행일: 2026-04-03T16:06:30Z
- 저자: Philipe S. Schiavo, João P. S. Milanezi, Moisés R. N. Ribeiro, Víctor M. G. Martínez, João Henrique Corrêa, José Marcos Nogueira, Fernando Frota Redigolo, Tereza C. Carvalho, Flávio de Oliveira Silva
- 식별자: `arxiv:2604.03145`

## 요약·초록

Resource sharing in multi-tenant cloud environments enables cost efficiency but introduces the Noisy Neighbor problem, i.e., co-located workloads that unpredictably degrade each other's performance. Despite extensive research on detecting such effects, there are no explainable methodologies for quantifying the severity of impact and establishing causal relationships among tenants. We propose an analytical that combines controlled experimentation with multi-stage causal inference and validates it across 10 independent rounds in a Kubernetes testbed. Our methodology not only quantifies severe performance degradations (e.g., up to 67\% in I/O-bound workloads under combined stress) but also statistically establishes causality through Granger causality analysis, revealing a 75\% increase in causal links when the noisy neighbor activates. Furthermore, we identify unique "degradation signatures" for each resource contention vector (i.e., CPU, memory, disk, network), enabling diagnostic capabilities that go beyond anomaly detection. This work transforms the Noisy Neighbor from an elusive problem into a quantifiable, diagnosable phenomenon, providing cloud operators with actionable insights for SLA management and smart resource allocation.

## 내 메모


