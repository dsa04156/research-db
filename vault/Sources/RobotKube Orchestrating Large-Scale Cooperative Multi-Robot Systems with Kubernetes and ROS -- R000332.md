---
type: research-source
item_id: 332
title: "RobotKube: Orchestrating Large-Scale Cooperative Multi-Robot Systems with Kubernetes and ROS"
source: "arxiv"
published: "2023-08-14T10:27:20Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2308.07053"
url: "https://arxiv.org/abs/2308.07053v1"
generated_by: codex-research-db
aliases:
  - "RobotKube: Orchestrating Large-Scale Cooperative Multi-Robot Systems with Kubernetes and ROS"
topics:
  - "kubernetes"
---

# RobotKube: Orchestrating Large-Scale Cooperative Multi-Robot Systems with Kubernetes and ROS

[원문 열기](https://arxiv.org/abs/2308.07053v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UNW4XI22`)
- 발행일: 2023-08-14T10:27:20Z
- 저자: Bastian Lampe, Lennart Reiher, Lukas Zanger, Timo Woopen, Raphael van Kempen, Lutz Eckstein
- 식별자: `arxiv:2308.07053`

## 요약·초록

Modern cyber-physical systems (CPS) such as Cooperative Intelligent Transport Systems (C-ITS) are increasingly defined by the software which operates these systems. In practice, microservice architectures can be employed, which may consist of containerized microservices running in a cluster comprised of robots and supporting infrastructure. These microservices need to be orchestrated dynamically according to ever changing requirements posed at the system. Additionally, these systems are embedded in DevOps processes aiming at continually updating and upgrading both the capabilities of CPS components and of the system as a whole. In this paper, we present RobotKube, an approach to orchestrating containerized microservices for large-scale cooperative multi-robot CPS based on Kubernetes. We describe how to automate the orchestration of software across a CPS, and include the possibility to monitor and selectively store relevant accruing data. In this context, we present two main components of such a system: an event detector capable of, e.g., requesting the deployment of additional applications, and an application manager capable of automatically configuring the required changes in the Kubernetes cluster. By combining the widely adopted Kubernetes platform with the Robot Operating System (ROS), we enable the use of standard tools and practices for developing, deploying, scaling, and monitoring microservices in C-ITS. We demonstrate and evaluate RobotKube in an exemplary and reproducible use case that we make publicly available at https://github.com/ika-rwth-aachen/robotkube .

## 내 메모


