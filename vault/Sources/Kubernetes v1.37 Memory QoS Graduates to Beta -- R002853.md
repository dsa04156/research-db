---
type: research-source
item_id: 2853
title: "Kubernetes v1.37: Memory QoS Graduates to Beta"
source: "rss:Kubernetes Blog"
published: "2026-09-14T18:30:00+00:00"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "url:f8ff73e4f9b79dc3a49e054c33920381831ba44bb70fb631679a2d152a5b25cc"
url: "https://kubernetes.io/blog/2026/09/14/kubernetes-v1-37-memory-qos-graduates-to-beta/"
generated_by: codex-research-db
aliases:
  - "Kubernetes v1.37: Memory QoS Graduates to Beta"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Kubernetes v1.37: Memory QoS Graduates to Beta

[원문 열기](https://kubernetes.io/blog/2026/09/14/kubernetes-v1-37-memory-qos-graduates-to-beta/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- Zotero: created (`NAAFUA8N`)
- 발행일: 2026-09-14T18:30:00+00:00
- 식별자: `url:f8ff73e4f9b79dc3a49e054c33920381831ba44bb70fb631679a2d152a5b25cc`

## 요약·초록

Memory QoS has graduated to Beta in Kubernetes v1.37 and is now enabled by default. On Linux nodes running cgroup v2, the feature uses the memory controller to give the kernel better guidance on how to treat container memory. It was first introduced as Alpha in v1.22, and expanded in v1.36 with tiered memory reservation. This post covers what changed in v1.37, what the Beta promotion means for cluster operators, and how to configure the feature. What changed in v1.37 Memory QoS is Beta and enabled by default The MemoryQoS feature gate is now Beta in v1.37. This means every v1.37 kubelet has the feature gate turned on without any configuration change. Turning on the feature by default is safe because the default kubelet configuration does not enable memory throttling or memory reservation. No memory.high , memory.min , or memory.low values are written to cgroups unless you explicitly configure them. You can opt into specific behaviors through kubelet configuration fields: Set memoryThrottlingFactor (for example, 0.9 ) to enable memory.high throttling on Burstable and BestEffort containers. The default is null , which means no throttling. Set memoryReservationPolicy to TieredReservation to enable tiered memory protection via memory.min and memory.low . The default is None , which means no memory reservation. Default memoryThrottlingFactor changed to null In earlier Alpha releases, memoryThrottlingFactor defaulted to 0.9 , which meant enabling the feature gate caused the kubelet to set memory.high on containers. In v1.37, the default is null , so the kubelet does not set memory.high unless you configure a value. This change was made because, with the feature gate now on by default, an automatic memory.high could throttle workloads that were previously running without throttling. Making it null ensures that upgrading to v1.37 does not change runtime behavior for existing clusters. If your kubelet configuration file already contains an explicit memoryThrottlingFactor value, that value is preserved during the upgrade and throttling continues to work as before. If your configuration file does not include memoryThrottlingFactor , the kubelet uses the new null default and stops setting memory.high . To keep throttling in that case, add memoryThrottlingFactor explicitly: apiVersion : kubelet.config.k8s.io/v1beta1 kind : KubeletConfiguration memoryThrottlingFactor : 0.9 How to configure MemoryQoS in v1.37 For full details on configuring Memory QoS, see Memory QoS with cgroup v2 , Configuring memory reservation , and System requirements Enable memory throttling only Set memoryThrottlingFactor to a value between 0 and 1. The kubelet uses this factor to calculate memory.high for Burstable and BestEffort containers. See Memory throttling for how memory.high is calculated for each QoS class. apiVersion : kubelet.config.k8s.io/v1beta1 kind : KubeletConfiguration memoryThrottlingFactor : 0.9 Enable memory throttling and tiered reservation apiVersion : kubelet.config.k8s.io/v1beta1 kind : KubeletConfiguration memoryThrottlingFactor : 0.9 memoryReservationPolicy : TieredReservation Enable tiered reservation without throttling apiVersion : kubelet.config.k8s.io/v1beta1 kind : KubeletConfiguration memoryReservationPolicy : TieredReservation Disable Memory QoS entirely To disable the feature after upgrading, set the feature gate to false and ensure a compatible kubelet configuration. The kubelet rejects the configuration if memoryThrottlingFactor is set to anything other than the former default of 0.9 , or if memoryReservationPolicy is TieredReservation , so remove or adjust those fields if you set them. apiVersion : kubelet.config.k8s.io/v1beta1 kind : KubeletConfiguration featureGates : MemoryQoS : false When the feature gate is off, or memoryReservationPolicy is not TieredReservation , the kubelet resets stale protection at startup on cgroup v2 nodes: memory.min=0 and memory.low=0 on the root kubepods cgroup, and memory.low=0 on the Burstable QoS cgroup. For containers, stale memory.high values are reset to max on reconciliation paths such as restart or resize. Known limitation: memory reservation is node-wide memoryReservationPolicy applies to every pod on the node. With TieredReservation , every Guaranteed pod gets memory.min and every Burstable pod gets memory.low ; there is no way to opt individual pods in or out. A node that mixes workloads needing hard reservation with workloads that should stay reclaimable has to choose one policy for all of them. Hard reservation also covers everything charged to the container's cgroup, including page cache, so a pod that reads large files can hold memory the kernel would otherwise reclaim to serve its neighbors. SIG Node is tracking both in kubernetes/kubernetes#140246 . If this affects you, that issue is the best place to describe your workload. What to expect next The next milestone for Memory QoS is graduation to GA. Feedback from Beta users will shape any remaining adjustments before that step. If you run into issues, please file bugs at kubernetes/kubernetes . How can I learn more? KEP-2570: Memory QoS Pod Quality of Service Classes Memory QoS with cgroup v2 Managing Resources for Containers Kubernetes cgroups v2 support Linux kernel cgroups v2 documentation Getting involved This feature is driven by SIG Node . If you are interested in contributing or have feedback, you can reach out through: Slack: #sig-node Mailing list SIG Node meetings

## 내 메모
