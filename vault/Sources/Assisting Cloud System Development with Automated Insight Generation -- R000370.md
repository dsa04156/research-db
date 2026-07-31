---
type: research-source
item_id: 370
title: "Assisting Cloud System Development with Automated Insight Generation"
source: "openalex"
published: "2024-01-01"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.7302/25688"
url: "https://hdl.handle.net/2027.42/197262"
generated_by: codex-research-db
aliases:
  - "Assisting Cloud System Development with Automated Insight Generation"
topics:
  - "kubernetes"
---

# Assisting Cloud System Development with Automated Insight Generation

[원문 열기](https://hdl.handle.net/2027.42/197262)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`BJTEBDAJ`)
- 발행일: 2024-01-01
- 저자: Yiming Qiu
- 식별자: `doi:10.7302/25688`

## 요약·초록

As cloud computing revolutionizes the IT industry, the complexity of underlying cloud systems has been increasing rapidly. The advent of new hardware accelerators and software platforms has made it challenging for cloud users to master the growing development toolkits. Compounding the issue, the programming frameworks and internals of these new systems are highly heterogeneous, with different performance characteristics, resource constraints, management principles, and reliability considerations. Consequently, it is becoming crucial to minimize human effort when managing these new ecosystems. In this dissertation, we advocate for assisting cloud developers and operators by automatically generating system insights. These insights bridge the gap between user intentions and system requirements, providing clarity on the outcomes of user actions on a system without the need for tedious trial-and-error processes. This dissertation demonstrates how we generate various types of insights for different cloud systems. Firstly, the dissertation explores performance optimization insights, which are critically needed as users attempt to offload legacy code from on-premise servers to emerging accelerators like SmartNICs. These new hardware components feature entirely different programming abstractions, compilers, instruction sets, and architectures. Although a straightforward offloading strategy might functionally work, it could lead to significant performance degradation, undermining the benefits of using accelerators. To address this issue, we create a toolset called Clara, which can automatically predict offloading performance and suggest tuning strategies before extensive deployment efforts. This allows users to make informed decisions on whether and how to offload their legacy code. Secondly, the dissertation investigates safety compliance insights for the cloud networking stack, focusing on ensuring the correctness of system updates for the latest generation of runtime-programmable platforms. We observe that even if both the current and intended functionalities are correct and efficient, the intermediate transition state can still introduce consistency and capacity issues into the core network. To tackle this challenge, we employ formal reasoning techniques to achieve update clarity. We develop FlexPlan, an interactive platform that synthesizes runtime transition plans meeting dynamic user demands, greatly minimizing the need for manual intervention. Lastly, the dissertation unearths infrastructure management insights for emerging cloud orchestration platforms. Clouds are constructed by providers like Microsoft but are intended for third-party use. This user/owner division limits cloud users’ visibility and control over cloud service behavior. The adoption of Infrastructure-as-Code (IaC) style cloud orchestration platforms further complicates this semantic gap by adding another intermediate layer of abstraction. To address this complexity, we propose Zodiac, a pipeline that automatically uncovers cloud provider requirements, and clarifies their interaction with orchestration platforms. The outcome is a set of orchestration rules that cloud users must follow to ensure proper cloud management practices. Throughout these projects, we leverage and extend techniques from a wide variety of disciplines, such as formal reasoning, software testing, machine learning, and their intersections. The results demonstrate the feasibility of generating useful insights across cloud data, control, and management planes, while unveiling an even larger insight generation and integration design space yet to be explored.

## 내 메모


