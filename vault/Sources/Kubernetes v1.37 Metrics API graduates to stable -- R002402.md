---
type: research-source
item_id: 2402
title: "Kubernetes v1.37: Metrics API graduates to stable"
source: "rss:Kubernetes Blog"
published: "2026-08-27T18:30:00+00:00"
first_seen: "2026-08-31"
review_status: "pending"
canonical_key: "url:3b5080acff0154853d9d0a88a850d37ca8500854ed165bba9cfe92e2c90dd8a4"
url: "https://kubernetes.io/blog/2026/08/27/kubernetes-v1-37-metrics-api-ga/"
generated_by: codex-research-db
aliases:
  - "Kubernetes v1.37: Metrics API graduates to stable"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Kubernetes v1.37: Metrics API graduates to stable

[원문 열기](https://kubernetes.io/blog/2026/08/27/kubernetes-v1-37-metrics-api-ga/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-08-31|2026-08-31]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- 발행일: 2026-08-27T18:30:00+00:00
- 식별자: `url:3b5080acff0154853d9d0a88a850d37ca8500854ed165bba9cfe92e2c90dd8a4`

## 요약·초록

Kubernetes v1.37 promotes the metrics.k8s.io API to stable ( v1 ). This API provides CPU and memory usage for nodes and Pods, and is the API behind commands such as kubectl top and resource-metrics-based autoscaling. For cluster operators and application developers, this graduation means that the API now has the stability guarantees associated with a Kubernetes stable API. The v1 API has the same resource types and fields as v1beta1 ; this is an API-version graduation, not a change to the metrics that are collected or returned. A long-lived API reaches stable The resource Metrics API was introduced as alpha in Kubernetes v1.6 and became beta in v1.8. It has remained unchanged and has been used in production for years by clients including the HorizontalPodAutoscaler (HPA) and kubectl top . Kubernetes v1.37 formally graduates that proven API to metrics.k8s.io/v1 . The API exposes two resource types: NodeMetrics , for CPU and memory usage for a node. PodMetrics , for CPU and memory usage for a Pod, with a per-container breakdown in its containers field. The API remains intentionally small. It provides the resource metrics needed for autoscaling and basic inspection; it is not a replacement for a full monitoring pipeline or the custom metrics ( custom.metrics.k8s.io ) API. What changed with the v1.37 release? The v1 API surface is identical to v1beta1 , except for the API version. There are no renamed fields, new fields, or changes to the meaning of the returned CPU and memory values. For example, a client can retrieve node metrics from the stable endpoint: kubectl get --raw /apis/metrics.k8s.io/v1/nodes Likewise, it can retrieve metrics for the pods in a namespace: kubectl get --raw /apis/metrics.k8s.io/v1/namespaces/default/pods kubectl top supports both API versions. It prefers v1 when available and automatically falls back to v1beta1 on clusters that do not yet serve v1 . The HPA controller currently supports only v1beta1 . Support for discovery-based selection between v1 and v1beta1 is planned, but is not available in Kubernetes v1.37. What you need to do You don't need to enable any feature gate. The Metrics API is served through the API aggregation layer , by an implementation such as metrics-server . You can choose any implementation of metrics.k8s.io ; for the v1 metrics API to be available in your cluster, your chosen implementation must serve the v1.metrics.k8s.io API, and you need to register an associated APIService . During the transition, implementations should serve both v1 and v1beta1 . Keeping both versions available maintains compatibility with older clients. The v1beta1 API remains available in Kubernetes v1.37. You can see which versions your cluster serves with: kubectl get --raw /apis/metrics.k8s.io/ | jq . Once your metrics implementation supports v1 , you can also check that its APIService is available: kubectl get apiservice v1.metrics.k8s.io Learn more Read the Resource metrics pipeline documentation. Read KEP-5207 , the proposal for (graduating) this API. Learn about the Metrics API and its reference implementation, metrics-server . Get involved The Metrics API is maintained by SIG Instrumentation . To ask questions, share feedback, or contribute, join the #sig-instrumentation channel on Kubernetes Slack or attend a SIG Instrumentation meeting.

## 내 메모


