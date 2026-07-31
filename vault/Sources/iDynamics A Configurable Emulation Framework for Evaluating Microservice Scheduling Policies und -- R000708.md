---
type: research-source
item_id: 708
title: "iDynamics: A Configurable Emulation Framework for Evaluating Microservice Scheduling Policies under Controllable Cloud-Edge Dynamics"
source: "arxiv"
published: "2025-03-20T10:52:50Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2503.16029"
url: "https://arxiv.org/abs/2503.16029v5"
generated_by: codex-research-db
aliases:
  - "iDynamics: A Configurable Emulation Framework for Evaluating Microservice Scheduling Policies under Controllable Cloud-Edge Dynamics"
topics:
  - "edge-computing"
  - "kubernetes"
---

# iDynamics: A Configurable Emulation Framework for Evaluating Microservice Scheduling Policies under Controllable Cloud-Edge Dynamics

[원문 열기](https://arxiv.org/abs/2503.16029v5)

## 연결

- 주제: [[vault/Topics/Edge computing]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`F35F2MM2`)
- 발행일: 2025-03-20T10:52:50Z
- 저자: Ming Chen, Muhammed Tawfiqul Islam, Maria Rodriguez Read, Rajkumar Buyya
- 식별자: `arxiv:2503.16029`

## 요약·초록

This paper presents iDynamics, a configurable emulation framework that exposes these dynamics as controllable experimental factors while running real microservice code on a Kubernetes-based cloud-edge cluster. iDynamics comprises three modular components. The Graph Dynamics Analyzer reconstructs application call graphs from service-mesh telemetry and quantifies bidirectional traffic between upstream-downstream microservice pairs. The Networking Dynamics Manager injects and measures realistic cross-node delay and bandwidth patterns via Linux traffic control primitives and distributed agents. The Scheduling Policy Extender offers a pluggable interface and utility library for implementing and evaluating arbitrary scheduling policies, expressed as pod placement and migration strategies. We use iDynamics to implement two representative policies -- a call-graph-aware policy and a hybrid policy that jointly considers traffic and latency -- as case studies demonstrating how the framework can be used to study SLA compliance under dynamic conditions. Experiments on a real cloud-edge cluster, running the DeathStarBench Social Network microservices, show that iDynamics can accurately emulate targeted network conditions, generate diverse call-graph and traffic patterns, and help quantify how different scheduling policies mitigate SLA violations under controllable and repeatable dynamics.

## 내 메모


