---
type: research-source
item_id: 745
title: "Dynamic In-node Group-Aware Scheduling for Multi-Tenant Machine Learning Services on Kubernetes"
source: "openalex"
published: "2025-07-07"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/cloud67622.2025.00017"
url: "https://doi.org/10.1109/cloud67622.2025.00017"
generated_by: codex-research-db
aliases:
  - "Dynamic In-node Group-Aware Scheduling for Multi-Tenant Machine Learning Services on Kubernetes"
topics:
  - "kubernetes"
---

# Dynamic In-node Group-Aware Scheduling for Multi-Tenant Machine Learning Services on Kubernetes

[원문 열기](https://doi.org/10.1109/cloud67622.2025.00017)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`NIBHUFWX`)
- 발행일: 2025-07-07
- 저자: Peini Liu, Jordi Guitart
- 식별자: `doi:10.1109/cloud67622.2025.00017`

## 요약·초록

Machine Learning (ML) is becoming pervasive and integrated into different kinds of businesses. Hosting multi-tenant ML services on a unified platform requires efficient orchestration. Service orchestration considers two levels: an in-cluster scheduling to decide the node allocation, followed by an in-node scheduling to manage the resource distribution within the node. Previous works introduced multi-container deployments for ML services, demonstrating that partitioning the ML service and enabling CPU/Memory affinity for each container improves performance. These multi-container deployments have been enabled for Kubernetes at in-cluster level to allocate multiple groups of containers across nodes. However, when the containers are launched in the node, the in-node scheduler lacks awareness of the group information which challenges those containers for a fine-grained resource allocation, especially when multiple groups of containers share the same node. This paper presents an in-node group-aware scheduling mechanism for multiple ML services, where each service scheduling contains a group resource selection and container resource assignment. Moreover, we also provide a dynamic resource controller (DRC) to dynamically reallocate the resource allocation for containers using the mechanism, which monitors the group changes and acts with the real containers' system cgroups adaptation. Our results show that for deploying ML services with the same ML model and different ML models, DRC throughput outperforms other deployment scenarios by up to 258% and 319% respectively. In an experiment deploying a dynamic workload of multiple mixed ML services, DRC outperforms baseline NONE-Single by 242 %, 75 %, and 28 % for the average throughput of services with Mobilenet, Resnet50, and VGG 16, respectively, and also DRC results in a makespan 44% faster than NONE-Single and 4% faster than CM-Multi.

## 내 메모


