---
type: research-source
item_id: 322
title: "Cost Minimization in Multi-cloud Systems with Runtime Microservice Re-orchestration"
source: "arxiv"
published: "2024-01-02T19:11:55Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/icin60470.2024.10494463"
url: "https://arxiv.org/abs/2401.01408v4"
generated_by: codex-research-db
aliases:
  - "Cost Minimization in Multi-cloud Systems with Runtime Microservice Re-orchestration"
topics:
  - "kubernetes"
---

# Cost Minimization in Multi-cloud Systems with Runtime Microservice Re-orchestration

[원문 열기](https://arxiv.org/abs/2401.01408v4)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DGSDGFSN`)
- 발행일: 2024-01-02T19:11:55Z
- 저자: Marco Zambianco, Silvio Cretti, Domenico Siracusa
- 식별자: `doi:10.1109/icin60470.2024.10494463`

## 요약·초록

Multi-cloud systems facilitate a cost-efficient and geographically-distributed deployment of microservice-based applications by temporary leasing virtual nodes with diverse pricing models. To preserve the cost-efficiency of multi-cloud deployments, it is essential to redeploy microservices onto the available nodes according to a dynamic resource configuration, which is often performed to better accommodate workload variations. However, this approach leads to frequent service disruption since applications are continuously shutdown and redeployed in order to apply the new resource assignment. To overcome this issue, we propose a re-orchestration scheme that migrates microservice at runtime based on a rolling update scheduling logic. Specifically, we propose an integer linear optimization problem that minimizes the cost associated to multi-cloud virtual nodes and that ensures that delay-sensitive microservices are co-located on the same regional cluster. The resulting rescheduling order guarantees no service disruption by repacking microservices between the available nodes without the need to turn off the outdated microservice instance before redeploying the updated version. In addition, we propose a two-step heuristic scheme that effectively approximates the optimal solution at the expense of close-to-zero service disruption and QoS violation probability. Results show that proposed schemes achieve better performance in terms of cost mitigation, low service disruption and low QoS violation probability compared to baseline schemes replicating Kubernetes scheduler functionalities.

## 내 메모


