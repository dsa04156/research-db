---
type: research-source
item_id: 724
title: "TraDE: Network and Traffic-aware Adaptive Scheduling for Microservices Under Dynamics"
source: "arxiv"
published: "2024-11-08T04:35:14Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/tpds.2025.3626424"
url: "https://arxiv.org/abs/2411.05323v2"
generated_by: codex-research-db
aliases:
  - "TraDE: Network and Traffic-aware Adaptive Scheduling for Microservices Under Dynamics"
topics:
  - "kubernetes"
---

# TraDE: Network and Traffic-aware Adaptive Scheduling for Microservices Under Dynamics

[원문 열기](https://arxiv.org/abs/2411.05323v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FAXBT968`)
- 발행일: 2024-11-08T04:35:14Z
- 저자: Ming Chen, Muhammed Tawfiqul Islam, Maria Rodriguez Read, Rajkumar Buyya
- 식별자: `doi:10.1109/tpds.2025.3626424`

## 요약·초록

The transition from monolithic architecture to microservices has enhanced flexibility in application design and its scalable execution. This approach typically uses a computing cluster managed by a container orchestration platform to deploy microservices. However, this shift introduces significant challenges, particularly in the efficient scheduling of containerized services. These challenges are compounded by unpredictable scenarios such as dynamic incoming workloads with various execution traffic and variable communication delays among cluster nodes. Existing works often overlook the real-time traffic impacts of dynamic requests on running microservices, as well as the varied communication delays across cluster nodes. Consequently, even optimally deployed microservices could suffer from significant performance degradation over time. To address these issues, we propose a network and traffic-aware adaptive scheduling framework, TraDE, which can adaptively redeploy microservice instances to maintain desired performance amid changing traffic and network conditions within the hosting cluster. We have implemented TraDE as an extension to the Kubernetes platform. Additionally, we deployed realistic microservice applications in a real compute cluster and conducted extensive experiments to assess our framework's performance in various scenarios. The results demonstrate the effectiveness of TraDE in rescheduling running microservices to enhance end-to-end performance while maintaining a high goodput ratio. Compared with the existing method NetMARKS, TraDE outperforms it by reducing the average response time of the application by up to 48.3%, and improving the throughput by up to 1.2-1.5x across workloads while maintaining a goodput ratio of 95.36%, and showing robust adaptive capability to meet QoS targets under sustained workloads and dynamic networking conditions.

## 내 메모


