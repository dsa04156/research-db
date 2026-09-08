---
type: research-source
item_id: 2660
title: "Reference architecture for HA scanning with Red Hat Advanced Cluster Security for Kubernetes"
source: "rss:Red Hat Developer Blog"
published: "2026-09-07T03:00:55+00:00"
first_seen: "2026-09-08"
review_status: "pending"
canonical_key: "url:c58ee5ac824783248fe8c20f5cbb7654fdb1674ca199d50db508cc7e915e817d"
url: "https://developers.redhat.com/articles/2026/09/07/reference-architecture-for-ha-scanning-with-red-hat-advanced-cluster-security-for-kubernetes"
generated_by: codex-research-db
aliases:
  - "Reference architecture for HA scanning with Red Hat Advanced Cluster Security for Kubernetes"
topics:
  - "kubernetes"
---

# Reference architecture for HA scanning with Red Hat Advanced Cluster Security for Kubernetes

[원문 열기](https://developers.redhat.com/articles/2026/09/07/reference-architecture-for-ha-scanning-with-red-hat-advanced-cluster-security-for-kubernetes)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-08|2026-09-08]]
- 수집 채널: `rss:Red Hat Developer Blog`
- 검토 상태: `pending`
- 발행일: 2026-09-07T03:00:55+00:00
- 식별자: `url:c58ee5ac824783248fe8c20f5cbb7654fdb1674ca199d50db508cc7e915e817d`

## 요약·초록

Red Hat Advanced Cluster Security for Kubernetes provides an image scanning API through its Central component that CI/CD pipelines depend on for vulnerability assessment. Red Hat Advanced Cluster Security upgrades and restarts introduce downtime windows that can block critical build paths. This post describes a reference architecture that eliminates scan API downtime by running two Central service instances with a client-side failover mechanism. The post Reference architecture for HA scanning with Red Hat Advanced Cluster Security for Kubernetes appeared first on Red Hat Developer .

## 내 메모


