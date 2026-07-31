---
type: research-source
item_id: 1191
title: "Semi-Automated Threat Modeling of Cloud-Based Systems Through Extracting Software Architecture from Configuration and Network Flow"
source: "arxiv"
published: "2026-03-23T21:57:53Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.22603"
url: "https://arxiv.org/abs/2603.22603v1"
generated_by: codex-research-db
aliases:
  - "Semi-Automated Threat Modeling of Cloud-Based Systems Through Extracting Software Architecture from Configuration and Network Flow"
topics:
  - "kubernetes"
---

# Semi-Automated Threat Modeling of Cloud-Based Systems Through Extracting Software Architecture from Configuration and Network Flow

[원문 열기](https://arxiv.org/abs/2603.22603v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`T3E3Z5RM`)
- 발행일: 2026-03-23T21:57:53Z
- 저자: Nicholas Pecka, Lotfi Ben Othmane, Bharat Bhargava, Renee Bryce
- 식별자: `arxiv:2603.22603`

## 요약·초록

Traditional threat modeling occurs during design, but cloud deployments introduce unanticipated threats, especially multi-stage attacks chaining vulnerabilities across trust boundaries. Existing security tools analyze components in isolation, cannot detect architectural threats from system composition, and cannot validate runtime behavior against configured policies. This gap leaves organizations vulnerable to attacks exploiting architectural weaknesses. This paper addresses this gap through a key innovation: automatically inferring system architecture from runtime observations to enable continuous threat modeling. Our methodology combines static configuration analysis with observed network flows to construct architecture graphs reflecting actual operational behavior, then applies systematic threat detection using platform-agnostic abstractions (components, domains, interfaces, access policies, flows). This enables consistent threat identification across bare metal, Kubernetes, and cloud infrastructure without manual diagram maintenance. We validate the methodology using a supply-chain system with ML components deployed on all three platforms, injecting 17 infrastructure and ML threats. Results show detection of all 17 threat types across all platforms, while existing security tools detected only 6-47% with zero ML threat coverage, confirming the necessity of runtime aware, architecture-level threat analysis.

## 내 메모


