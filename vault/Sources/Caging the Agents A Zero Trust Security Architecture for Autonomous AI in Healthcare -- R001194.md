---
type: research-source
item_id: 1194
title: "Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare"
source: "arxiv"
published: "2026-03-18T06:54:47Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2603.17419"
url: "https://arxiv.org/abs/2603.17419v1"
generated_by: codex-research-db
aliases:
  - "Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare"
topics:
  - "kubernetes"
---

# Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare

[원문 열기](https://arxiv.org/abs/2603.17419v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DFTDM7ZG`)
- 발행일: 2026-03-18T06:54:47Z
- 저자: Saikat Maiti
- 식별자: `arxiv:2603.17419`

## 요약·초록

Autonomous AI agents powered by large language models are being deployed in production with capabilities including shell execution, file system access, database queries, and multi-party communication. Recent red teaming research demonstrates that these agents exhibit critical vulnerabilities in realistic settings: unauthorized compliance with non-owner instructions, sensitive information disclosure, identity spoofing, cross-agent propagation of unsafe practices, and indirect prompt injection through external resources [7]. In healthcare environments processing Protected Health Information, every such vulnerability becomes a potential HIPAA violation. This paper presents a security architecture deployed for nine autonomous AI agents in production at a healthcare technology company. We develop a six-domain threat model for agentic AI in healthcare covering credential exposure, execution capability abuse, network egress exfiltration, prompt integrity failures, database access risks, and fleet configuration drift. We implement four-layer defense in depth: (1) kernel level workload isolation using gVisor on Kubernetes, (2) credential proxy sidecars preventing agent containers from accessing raw secrets, (3) network egress policies restricting each agent to allowlisted destinations, and (4) a prompt integrity framework with structured metadata envelopes and untrusted content labeling. We report results from 90 days of deployment including four HIGH severity findings discovered and remediated by an automated security audit agent, progressive fleet hardening across three VM image generations, and defense coverage mapped to all eleven attack patterns from recent literature. All configurations, audit tooling, and the prompt integrity framework are released as open source.

## 내 메모


