---
type: research-source
item_id: 2191
title: "Scalable Distributed Simulation-Based Testing for Automated Driving Systems"
source: "arxiv"
published: "2026-08-21T09:22:45Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.20904"
url: "https://arxiv.org/abs/2608.20904v1"
generated_by: codex-research-db
aliases:
  - "Scalable Distributed Simulation-Based Testing for Automated Driving Systems"
topics:
  - "kubernetes"
---

# Scalable Distributed Simulation-Based Testing for Automated Driving Systems

[원문 열기](https://arxiv.org/abs/2608.20904v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`58GTXR33`)
- 발행일: 2026-08-21T09:22:45Z
- 저자: Christian Geller, Benedikt Haas, Lutz Eckstein
- 식별자: `arxiv:2608.20904`

## 요약·초록

Virtual scenario-based testing is a key enabler for validating automated driving systems (ADS) and intelligent transport systems (ITS). However, executing large-scale test suites involving possibly thousands of scenarios remains labor-intensive and difficult to scale. This paper presents an end-to-end, DevOps-driven framework that automates build, deployment, and distributed execution of CARLA-based scenario tests of an ADS on a lightweight Kubernetes cluster. ROS 2 applications are packaged as standardized Kubernetes Helm charts generated from repository specifications, while entire simulation environments are composed declaratively via dynamic Helmfile manifests. The paper describes how a distributed testing workflow can be implemented in Argo Workflows to provision environments, aggregate and batch OpenSCENARIO test cases from configurable sources, execute scenarios in parallel across cluster nodes, and collect logs and resource metrics. In an evaluation on a multi-node K3s cluster running 200 scenarios, the best configuration speeds up end-to-end workflow time by more than a factor of eight compared to a sequential baseline. The results demonstrate significant gains in end-to-end execution time and quantify trade-offs between parallelism, orchestration overhead, and cluster stability. The framework is further demonstrated in a real-world ADS test application with connections to scenario sources and downstream evaluation modules. This demonstrates that the approach provides a strong foundation not only for scalable simulation testing, but also for generating traceable evidence that can support safety arguments.

## 내 메모


