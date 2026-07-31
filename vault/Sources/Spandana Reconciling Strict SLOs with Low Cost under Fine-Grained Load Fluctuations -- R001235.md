---
type: research-source
item_id: 1235
title: "Spandana: Reconciling Strict SLOs with Low Cost under Fine-Grained Load Fluctuations"
source: "openalex"
published: "2026-06-29"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.30533"
url: "https://arxiv.org/abs/2606.30533"
generated_by: codex-research-db
aliases:
  - "Spandana: Reconciling Strict SLOs with Low Cost under Fine-Grained Load Fluctuations"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Spandana: Reconciling Strict SLOs with Low Cost under Fine-Grained Load Fluctuations

[원문 열기](https://arxiv.org/abs/2606.30533)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`XXNM7PHQ`)
- 발행일: 2026-06-29
- 저자: Dilina Dehigama, Shyam Jesalpura, Zhewei Xu, Marton Nemeth, Shengda Zhu, Marios Kogias, Boris Grot
- 식별자: `arxiv:2606.30533`

## 요약·초록

Cloud-based online services face significant sub-second load fluctuations while needing to meet strict Service Level Objectives (SLOs). Cluster operators often over-provision resources to protect SLOs, sacrificing utilization and cost efficiency. Existing reactive and proactive autoscalers, serverless (FaaS) deployments, and VM/FaaS hybrid systems fail to reconcile strict SLO compliance with low cost and high utilization under fine-grained load fluctuation. We introduce Spandana, an architecture that addresses this trade off by decoupling SLO enforcement from cost optimization. A lightweight controller colocated with each application VM enforces SLOs by steering each arriving request between the VM and FaaS. Requests that can meet the SLO stay on the VM; the remaining requests are forwarded to a stock FaaS layer such as AWS Lambda. For cost optimization, Spandana's resource allocator determines the most-efficient VM provisioning by accounting for VM cost, FaaS cost, and traffic volatility, allowing the VM pool to run at high utilization. Our evaluation shows that Spandana maintains strict SLO adherence, achieves 76-86% CPU utilization, and reduces cost by 5-44% over three SOTA baselines.

## 내 메모


