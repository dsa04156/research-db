---
type: research-source
item_id: 1416
title: "Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager"
source: "rss:Kubernetes Blog"
published: "2026-05-15T18:35:00+00:00"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:558cd03a67c5610a9a3202355d270a35648d7e8e394cab5b974cb66cc1807454"
url: "https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/"
generated_by: codex-research-db
aliases:
  - "Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Kubernetes v1.36: New Metric for Route Sync in the Cloud Controller Manager

[원문 열기](https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- Zotero: created (`55PKWRSE`)
- 발행일: 2026-05-15T18:35:00+00:00
- 식별자: `url:558cd03a67c5610a9a3202355d270a35648d7e8e394cab5b974cb66cc1807454`

## 요약·초록

This article was originally published with the wrong date. It was later republished, dated the 15th of May 2026. Kubernetes v1.36 introduces a new alpha counter metric route_controller_route_sync_total to the Cloud Controller Manager (CCM) route controller implementation at k8s.io/cloud-provider . This metric increments each time routes are synced with the cloud provider. A/B testing watch-based route reconciliation This metric was added to help operators validate the CloudControllerManagerWatchBasedRoutesReconciliation feature gate introduced in Kubernetes v1.35 . That feature gate switches the route controller from a fixed-interval loop to a watch-based approach that only reconciles when nodes actually change. This reduces unnecessary API calls to the infrastructure provider, lowering pressure on rate-limited APIs and allowing operators to make more efficient use of their available quota. To A/B test this, compare route_controller_route_sync_total with the feature gate disabled (default) versus enabled. In clusters where node changes are infrequent, you should see a significant drop in the sync rate with the feature gate turned on. Example: expected behavior With the feature gate disabled (the default fixed-interval loop), the counter increments steadily regardless of whether any node changes occurred: # After 10 minutes with no node changes route_controller_route_sync_total 60 # After 20 minutes, still no node changes route_controller_route_sync_total 120 With the feature gate enabled (watch-based reconciliation), the counter only increments when nodes are actually added, removed, or updated: # After 10 minutes with no node changes route_controller_route_sync_total 1 # After 20 minutes, still no node changes — counter unchanged route_controller_route_sync_total 1 # A new node joins the cluster — counter increments route_controller_route_sync_total 2 The difference is especially visible in stable clusters where nodes rarely change. Where can I give feedback? If you have feedback, feel free to reach out through any of the following channels: The #sig-cloud-provider channel on Kubernetes Slack The KEP-5237 issue on GitHub The SIG Cloud Provider community page for other communication channels How can I learn more? For more details, refer to KEP-5237 .

## 내 메모


