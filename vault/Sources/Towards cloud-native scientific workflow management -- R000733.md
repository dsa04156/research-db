---
type: research-source
item_id: 733
title: "Towards cloud-native scientific workflow management"
source: "arxiv"
published: "2024-08-27T23:32:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2408.15445"
url: "https://arxiv.org/abs/2408.15445v1"
generated_by: codex-research-db
aliases:
  - "Towards cloud-native scientific workflow management"
topics:
  - "kubernetes"
---

# Towards cloud-native scientific workflow management

[원문 열기](https://arxiv.org/abs/2408.15445v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`Z2BB29GN`)
- 발행일: 2024-08-27T23:32:41Z
- 저자: Michal Orzechowski, Bartosz Balis, Krzysztof Janecki
- 식별자: `arxiv:2408.15445`

## 요약·초록

Cloud-native is an approach to building and running scalable applications in modern cloud infrastructures, with the Kubernetes container orchestration platform being often considered as a fundamental cloud-native building block. In this paper, we evaluate alternative execution models for scientific workflows in Kubernetes. We compare the simplest job-based model, its variant with task clustering, and finally we propose a cloud-native model based on microservices comprising auto-scalable worker-pools. We implement the proposed models in the HyperFlow workflow management system, and evaluate them using a large Montage workflow on a Kubernetes cluster. The results indicate that the proposed cloud-native worker-pools execution model achieves best performance in terms of average cluster utilization, resulting in a nearly 20\% improvement of the workflow makespan compared to the best-performing job-based model. However, better performance comes at the cost of significantly higher complexity of the implementation and maintenance. We believe that our experiments provide a valuable insight into the performance, advantages and disadvantages of alternative cloud-native execution models for scientific workflows.

## 내 메모


