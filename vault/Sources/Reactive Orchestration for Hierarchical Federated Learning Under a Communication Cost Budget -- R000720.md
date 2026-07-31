---
type: research-source
item_id: 720
title: "Reactive Orchestration for Hierarchical Federated Learning Under a Communication Cost Budget"
source: "arxiv"
published: "2024-12-04T15:12:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2412.03385"
url: "https://arxiv.org/abs/2412.03385v2"
generated_by: codex-research-db
aliases:
  - "Reactive Orchestration for Hierarchical Federated Learning Under a Communication Cost Budget"
topics:
  - "kubernetes"
---

# Reactive Orchestration for Hierarchical Federated Learning Under a Communication Cost Budget

[원문 열기](https://arxiv.org/abs/2412.03385v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`T4CAIKXG`)
- 발행일: 2024-12-04T15:12:00Z
- 저자: Ivan Čilić, Anna Lackinger, Pantelis Frangoudis, Ivana Podnar Žarko, Alireza Furutanpey, Ilir Murturi, Schahram Dustdar
- 식별자: `arxiv:2412.03385`

## 요약·초록

Deploying a Hierarchical Federated Learning (HFL) pipeline across the computing continuum (CC) requires careful organization of participants into a hierarchical structure with intermediate aggregation nodes between FL clients and the global FL server. This is challenging to achieve due to (i) cost constraints, (ii) varying data distributions, and (iii) the volatile operating environment of the CC. In response to these challenges, we present a framework for the adaptive orchestration of HFL pipelines, designed to be reactive to client churn and infrastructure-level events, while balancing communication cost and ML model accuracy. Our mechanisms identify and react to events that cause HFL reconfiguration actions at runtime, building on multi-level monitoring information (model accuracy, resource availability, resource cost). Moreover, our framework introduces a generic methodology for estimating reconfiguration costs to continuously re-evaluate the quality of adaptation actions, while being extensible to optimize for various HFL performance criteria. By extending the Kubernetes ecosystem, our framework demonstrates the ability to react promptly and effectively to changes in the operating environment, making the best of the available communication cost budget and effectively balancing costs and ML performance at runtime.

## 내 메모


