---
type: research-source
item_id: 1267
title: "Bringing the Far-Edge into the IoT Continuum: A Framework for Service Orchestration on Constrained Devices"
source: "openalex"
published: "2026-05-15"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:80871a1284152352328f96a41ee969417c1ce6bf77479c793ee7bfc3e2359de3"
url: "https://hdl.handle.net/10216/174721"
generated_by: codex-research-db
aliases:
  - "Bringing the Far-Edge into the IoT Continuum: A Framework for Service Orchestration on Constrained Devices"
topics:
  - "edge-computing"
  - "kubernetes"
---

# Bringing the Far-Edge into the IoT Continuum: A Framework for Service Orchestration on Constrained Devices

[원문 열기](https://hdl.handle.net/10216/174721)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`SWPIUR9G`)
- 발행일: 2026-05-15
- 저자: João Carlos Viseu Oliveira
- 식별자: `url:80871a1284152352328f96a41ee969417c1ce6bf77479c793ee7bfc3e2359de3`

## 요약·초록

The Internet of Things (IoT) envisions a future in which a ubiquitous network of interconnected devices collects and processes valuable information across a wide range of application domains.This vision is increasingly being realized, supported by advances in low-power electronics, connectivity technologies, and computing infrastructures.To support the increasing pervasiveness of IoT systems, a layered architecture of devices with heterogeneous resource capabilities has emerged, forming the IoT continuum.This continuum is commonly structured into three layers: Cloud, Edge, and Far-Edge.To realize the IoT vision, these layers must collaborate to form distributed applications composed of services that can be deployed, updated, and interconnected.While this paradigm is well-established in the Cloud and Edge, the Far-Edge, where resource-constrained microcontroller-based devices sense and actuate upon the physical environment, remains largely disconnected from the rest of the continuum.Due to limited resources and the absence of standardized runtime and management mechanisms, such devices are commonly treated as static data producers rather than as computing resources, fragmenting the IoT continuum and limiting the dynamism of IoT applications.This Thesis addresses this fundamental gap by integrating Far-Edge devices as orchestrable computing resources within modern IoT application architectures.The first contribution of our work is embServe, an interoperable container-like execution runtime that enables dynamic, service-based deployment and reconfiguration on Far-Edge devices.While embServe establishes a foundational mechanism for dynamic Far-Edge management, it does not fully integrate the Far-Edge into the IoT continuum.Therefore, the second contribution is FITA, a platform that integrates embServe-enabled devices into Kubernetes, the widely adopted orchestration framework.FITA extends Kubernetes to support Far-Edge service deployments through standard Kubernetes interfaces, while exposing Far-Edge-specific capabilities, such as sensors and actuators, to the Kubernetes scheduler.By integrating Far-Edge devices as orchestrable entities, FITA enables unified application management across the IoT continuum, from the Cloud to the Far-Edge.Beyond unified management, embServe and FITA enable new application scenarios that leverage computation at the Far-Edge.Building on this, the third contribution of this Thesis is TinyKubeML, which extends FITA to support the distributed deployment of TinyML models across clusters of Far-Edge devices.TinyKubeML introduces a new component to FITA that partitions machine learning models according to the available cluster resources, converts model partitions into artifacts compatible with the embServe runtime, and generates deployments using configurable heuristics.By combining TinyML with cloud-native orchestration principles, TinyKubeML enables adaptive and distributed inference closer to data sources, while further leveraging the computational resources available at the Far-Edge.Through experimental evaluation and representative application scenarios, this Thesis demonstrates that Far-Edge devices can participate in orchestration processes and distributed computation.The presented results validate that extending cloud-native principles to the Far-Edge enables unified management, improved flexibility, and more dynamic IoT deployments, thereby bridging i ii a critical gap in the IoT continuum.

## 내 메모


