---
type: research-source
item_id: 2851
title: "Kubernetes v1.37: Pod-Level Resource Managers graduated to Beta"
source: "rss:Kubernetes Blog"
published: "2026-09-15T18:30:00+00:00"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "url:5309177f19f859cab89d6cd940ab38fcfee3f4cae9bb83095476382f0cac2ca1"
url: "https://kubernetes.io/blog/2026/09/15/kubernetes-v1-37-pod-level-resource-managers-beta/"
generated_by: codex-research-db
aliases:
  - "Kubernetes v1.37: Pod-Level Resource Managers graduated to Beta"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Kubernetes v1.37: Pod-Level Resource Managers graduated to Beta

[원문 열기](https://kubernetes.io/blog/2026/09/15/kubernetes-v1-37-pod-level-resource-managers-beta/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- 발행일: 2026-09-15T18:30:00+00:00
- 식별자: `url:5309177f19f859cab89d6cd940ab38fcfee3f4cae9bb83095476382f0cac2ca1`

## 요약·초록

With the release of Kubernetes v1.37, the Pod-Level Resource Managers feature has graduated to Beta status (disabled by default)! First introduced as an Alpha feature in Kubernetes v1.36 , this enhancement builds on Pod-Level Resources by equipping Kubelet's Topology Manager, CPU Manager, and Memory Manager to use Pod-level resource declarations ( .spec.resources ) directly when making hardware placement decisions. Bringing pod-level resources to node managers Before this feature, obtaining exclusive NUMA-aligned CPU cores or memory for latency-critical applications forced cluster operators into an all-or-nothing choice: assign integer resource requests to every container in the Pod, or forfeit exclusive NUMA alignment entirely. For modern workloads running lightweight sidecars (such as logging agents or telemetry exporters), allocating dedicated physical cores to auxiliary containers was wasteful. Pod-Level Resource Managers solves this challenge by enabling hybrid allocation models. The Kubelet can reserve exclusive NUMA-aligned resources for primary application containers while placing non-Guaranteed sidecars into a pod-isolated shared pool. This ensures primary workloads get unthrottled, NUMA-local performance while sidecars benefit from running in a pod-isolated shared pool, enjoying local NUMA alignment and protection from external node interference without consuming dedicated physical cores. What's new in Beta Graduating to Beta brings key operational and API enhancements: Graduation to Beta: Controlled by the PodLevelResourceManagers feature gate, available to opt in (disabled by default) in Kubernetes v1.37. PodResources API Reporting: The v1 PodResources gRPC service ( PodResourcesLister ) introduces top-level cpu_ids and memory fields on PodResources responses. Monitoring tools and device plugins can query pod-level exclusive assignments directly without double-counting container allocations. Getting started and providing feedback For a deep dive into the technical details and configuration of this feature, check out the official documentation: Pod-level resource managers Pod-level resource managers reference To follow a step-by-step tutorial on configuring and deploying workloads: Use pod-level resources with Kubelet resource managers To learn more about how to assign resources to pods: Assign Pod-level CPU and memory resources As this feature moves through Beta toward GA, your feedback is invaluable. Please report any issues or share your experiences via the standard Kubernetes communication channels: Slack: #sig-node Mailing list Open Community Issues/PRs

## 내 메모
