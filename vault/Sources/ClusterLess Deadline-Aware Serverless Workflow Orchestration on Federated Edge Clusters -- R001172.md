---
type: research-source
item_id: 1172
title: "ClusterLess: Deadline-Aware Serverless Workflow Orchestration on Federated Edge Clusters"
source: "arxiv"
published: "2026-05-05T21:15:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2605.04310"
url: "https://arxiv.org/abs/2605.04310v1"
generated_by: codex-research-db
aliases:
  - "ClusterLess: Deadline-Aware Serverless Workflow Orchestration on Federated Edge Clusters"
topics:
  - "edge-computing"
  - "kubernetes"
  - "cloud-infrastructure"
---

# ClusterLess: Deadline-Aware Serverless Workflow Orchestration on Federated Edge Clusters

[원문 열기](https://arxiv.org/abs/2605.04310v1)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`XMX663T2`)
- 발행일: 2026-05-05T21:15:43Z
- 저자: Reza Farahani, Mario Colosi, Ilir Murturi, Stefan Nastic, Massimo Villari, Schahram Dustdar, Radu Prodan
- 식별자: `arxiv:2605.04310`

## 요약·초록

The recent convergence of edge computing, serverless execution, and Kubernetes (K8s) based container orchestration has enabled the processing of application workflows close to data sources. While effective within a single edge cluster, existing schemes do not generalize to federated multi edge environments, where multiple workflows execute concurrently under strict end to end (E2E) deadline constraints. This paper introduces ClusterLess, a deadline aware serverless workflow orchestration method for federated multi edge K8s clusters. ClusterLess manages the E2E lifecycle of workflow execution, including dependency analysis, execution mode selection, and resource aware placement. To this end, it integrates structured intra cluster orchestration with a leader selected, super master driven intercluster coordination layer, determining where and how each workflow function should be executed across the federated edge clusters. We implement ClusterLess using OpenFaaS as the serverless execution substrate and Argo for workflow management, and deploy it on a realistic testbed of six edge clusters comprising 64 heterogeneous edge nodes. Experimental results with concurrent serverless workflows, spanning 18 workload configurations across different input sizes and deadline classes, show that ClusterLess reduces workflow completion time by up to 40 %, increases deadline satisfaction from below 50 % to over 90 %, and confines deadline violations to single digit seconds compared to four baseline methods.

## 내 메모


