---
type: research-source
item_id: 329
title: "The Flux Operator"
source: "arxiv"
published: "2023-09-29T17:29:35Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2309.17420"
url: "https://arxiv.org/abs/2309.17420v1"
generated_by: codex-research-db
aliases:
  - "The Flux Operator"
topics:
  - "kubernetes"
---

# The Flux Operator

[원문 열기](https://arxiv.org/abs/2309.17420v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6MQD6VUN`)
- 발행일: 2023-09-29T17:29:35Z
- 저자: Vanessa Sochat, Aldo Culquicondor, Antonio Ojea, Daniel Milroy
- 식별자: `arxiv:2309.17420`

## 요약·초록

Converged computing brings together the best of both worlds for high performance computing (HPC) and cloud-native communities. In fact, the economic impact of cloud-computing, and need for portability, flexibility, and manageability make it not important, but inevitable. Navigating this uncharted territory requires not just innovation in the technology space, but also effort toward collaboration and sharing of ideas. With these goals in mind, this work first tackles the central component of running batch workflows, whether in cloud or HPC: the workload manager. For cloud, Kubernetes has become the de facto tool for this kind of batch orchestration. For HPC, the next-generation HPC workload manager Flux Framework is analogous -- combining fully hierarchical resource management and graph-based scheduling to support intelligent scheduling and job management. Convergence of these managers would mean the implementation of Flux inside of Kubernetes, allowing for hierarchical resource management and scheduling that scales impressively without burdening the Kubernetes scheduler itself. This paper introduces the Flux Operator -- an on-demand HPC workload manager that is easily deployed in Kubernetes. The work here highlights design decisions, mapping of components between environments, experimental features, and shares the results of experiments that compare performance with an equivalent operator in the space, the MPI Operator. Finally, discussion closes with a review of challenges remaining, and hopes for the future for improved technological innovation and collaboration.

## 내 메모


