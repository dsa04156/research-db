---
type: research-source
item_id: 2852
title: "Kubernetes Changed Block Tracking API - Beta Differences"
source: "rss:Kubernetes Blog"
published: "2026-09-14T18:30:00+00:00"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "url:7193a9ff8eb6b0f956cc0898277bef75597d5eed1305bff5ad3e70049a1ef08e"
url: "https://kubernetes.io/blog/2026/09/14/csi-changed-block-tracking-beta/"
generated_by: codex-research-db
aliases:
  - "Kubernetes Changed Block Tracking API - Beta Differences"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Kubernetes Changed Block Tracking API - Beta Differences

[원문 열기](https://kubernetes.io/blog/2026/09/14/csi-changed-block-tracking-beta/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- Zotero: created (`KVZEFP5D`)
- 발행일: 2026-09-14T18:30:00+00:00
- 식별자: `url:7193a9ff8eb6b0f956cc0898277bef75597d5eed1305bff5ad3e70049a1ef08e`

## 요약·초록

Changed Block Tracking (CBT) support for CSI drivers shipped as Alpha in September 2025. With the March 2026 v1.0.0 release of the external-snapshot-metadata project, the feature moved to Beta . If you aren't yet familiar with changed block tracking for storage in Kubernetes, the Alpha announcement covers the motivation, the three primary components (the CSI SnapshotMetadata gRPC service, the SnapshotMetadataService CRD, and the external-snapshot-metadata sidecar), and a walkthrough of how to use the API. CBT currently applies to block volumes; file-volume and network file-share changed-list tracking is not covered by this feature. This post focuses on what is different in Beta. What's new in Beta The main change in that release was the promotion of the SnapshotMetadataService CRD from v1alpha1 to v1beta1 . The CRD used to advertise a driver's metadata service now serves cbt.storage.k8s.io/v1beta1 . The schema itself is unchanged, but this release removed v1alpha1 (rather than serving it alongside the new version). If you are upgrading from Alpha, you need to: Re-apply the CRD definition shipped with v1.0.0 . Update SnapshotMetadataService manifests to use apiVersion: cbt.storage.k8s.io/v1beta1 . Update any client or controller code that talks to the CRD. This is a one-time change. There is no automatic conversion between the two versions. Compatibility Minimum Kubernetes version: 1.33 CSI spec: 1.10 or newer Container image: registry.k8s.io/sig-storage/csi-snapshot-metadata:v1.0.0 Trying it out The Getting Started section in the Alpha blog still applies. In short: Make sure your CSI driver supports volume snapshots and ships the external-snapshot-metadata sidecar. Install the SnapshotMetadataService CRD (the v1beta1 definition from the v1.0.0 release). Create a SnapshotMetadataService resource for your driver. Use a client — snapshot-metadata-lister , or your own implementation — to call GetMetadataAllocated and GetMetadataDelta . If you want to see the full flow end-to-end, the hostpath driver example is a good starting point. What's next? The focus for the rest of the Beta cycle is wider CSI driver adoption and operational feedback before the feature moves towards GA. If you maintain a CSI driver, this is a good time to evaluate adding support. If you are building a backup application on top of the API, feedback on the streaming clients and the iterator package is very welcome. Where can I learn more? The CSI developer documentation for snapshot metadata. KEP-3314 . The external-snapshot-metadata repository. The gRPC schema . The snapshot-metadata-lister example client. How do I get involved? This work is the result of contributions from many people across SIG Storage. A big thank you to everyone who helped review, code, and test the feature through Alpha and into Beta: Ben Swartzlander ( bswartz ) Carl Braganza ( carlbraganza ) Daniil Fedotov ( hairyhum ) Ivan Sim ( ihcsim ) Nikhil Ladha ( Nikhil-Ladha ) Praveen M ( iPraveenParihar ) Rakshith R ( Rakshith-R ) Xing Yang ( xing-yang ) If you would like to get involved with CSI or storage in Kubernetes, SIG Storage is the place to start. The Data Protection Working Group also holds regular meetings, and new attendees are always welcome.

## 내 메모
