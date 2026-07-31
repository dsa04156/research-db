---
type: research-source
item_id: 703
title: "KubeFence: Security Hardening of the Kubernetes Attack Surface"
source: "arxiv"
published: "2025-04-15T12:15:34Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/dsn64029.2025.00054"
url: "https://arxiv.org/abs/2504.11126v1"
generated_by: codex-research-db
aliases:
  - "KubeFence: Security Hardening of the Kubernetes Attack Surface"
topics:
  - "kubernetes"
---

# KubeFence: Security Hardening of the Kubernetes Attack Surface

[원문 열기](https://arxiv.org/abs/2504.11126v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`98N9PNGH`)
- 발행일: 2025-04-15T12:15:34Z
- 저자: Carmine Cesarano, Roberto Natella
- 식별자: `doi:10.1109/dsn64029.2025.00054`

## 요약·초록

Kubernetes (K8s) is widely used to orchestrate containerized applications, including critical services in domains such as finance, healthcare, and government. However, its extensive and feature-rich API interface exposes a broad attack surface, making K8s vulnerable to exploits of software vulnerabilities and misconfigurations. Even if K8s adopts role-based access control (RBAC) to manage access to K8s APIs, this approach lacks the granularity needed to protect specification attributes within API requests. This paper proposes a novel solution, KubeFence, which implements finer-grain API filtering tailored to specific client workloads. KubeFence analyzes Kubernetes Operators from trusted repositories and leverages their configuration files to restrict unnecessary features of the K8s API, to mitigate misconfigurations and vulnerabilities exploitable through the K8s API. The experimental results show that KubeFence can significantly reduce the attack surface and prevent attacks compared to RBAC.

## 내 메모


