---
type: research-source
item_id: 725
title: "Distributed Tracing for Cascading Changes of Objects in the Kubernetes Control Plane"
source: "arxiv"
published: "2024-11-02T18:40:01Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2411.01336"
url: "https://arxiv.org/abs/2411.01336v1"
generated_by: codex-research-db
aliases:
  - "Distributed Tracing for Cascading Changes of Objects in the Kubernetes Control Plane"
topics:
  - "kubernetes"
---

# Distributed Tracing for Cascading Changes of Objects in the Kubernetes Control Plane

[원문 열기](https://arxiv.org/abs/2411.01336v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`U5CCDN9X`)
- 발행일: 2024-11-02T18:40:01Z
- 저자: Tomoyuki Ehira, Daisuke Kotani, Yasuo Okabe
- 식별자: `arxiv:2411.01336`

## 요약·초록

Kubernetes is a container orchestration system that employs a declarative configuration management approach. In Kubernetes, each desired and actual state is represented by an ``object'', and multiple controllers autonomously monitor related objects and update their objects towards the desired state in the control plane. Because of this design, changes to one object propagate to other objects in a chain. The cluster operators need to know the time required for these cascading changes to complete, as it directly affects the quality of service of applications running on the cluster. However, there is no practical way to observe this kind of cascading change, including breakdown of the time taken by each change. Distributed tracing techniques are commonly used in the microservices architecture to monitor application performance, but they are not directly applicable to the control plane of Kubernetes; the microservices architecture relies on explicitly calling APIs on other services, but in Kubernetes the controllers just monitor objects to know when to start processing, and never call functions on other controllers directly. In this paper, we propose a system that automatically traces changes to objects in the control plane. Our method adds one identifier, a Change Propagation ID (CPID), to the metadata of an object, and the controller that observes an object change propagates its CPID to the objects that the controller is updated. When multiple changes need to be merged on an object, a new CPID is generated, and the relationship between the original CPID and the new CPID is sent to the external trace server. We confirmed that change propagation can be visualized and the required time measured. We also showed that this system's overhead is not significant.

## 내 메모


