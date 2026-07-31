---
type: research-source
item_id: 8
title: "Distributing Security Controls Through Harness Engineering"
source: "arxiv"
published: "2026-07-28T15:50:16Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.25890"
url: "https://arxiv.org/abs/2607.25890v1"
generated_by: codex-research-db
aliases:
  - "Distributing Security Controls Through Harness Engineering"
topics:
  - "self-evolving-harness"
---

# Distributing Security Controls Through Harness Engineering

[원문 열기](https://arxiv.org/abs/2607.25890v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`HE2U6EJS`)
- 발행일: 2026-07-28T15:50:16Z
- 저자: William Robert Gore
- 식별자: `arxiv:2607.25890`

## 요약·초록

AI coding agents are being adopted at historic speed, yet security and risk concerns remain the primary barrier to scaling agentic AI across organizations. Existing security controls for coding agents are not systematically distributed to engineering teams, and vendor-native solutions introduce ecosystem dependencies that may not suit every deployment context. This paper investigates whether off-the-shelf security controls can be implemented on commercial AI coding agents and scaled to a distributed user base via a custom agent harness. A phased testing methodology was applied across four agent configurations --- two commercial agents with and without controls, a baseline harness, and a security-hardened harness --- using a 23-test suite derived from the OWASP Top 10 for Agentic Applications. SHarD (Secure Harness Distribution), a distributable harness built on the Pi agent harness, demonstrated that three categories of security controls --- OS sandboxing, skill scanning, and tool restriction --- can be embedded and distributed via a single install command while retaining equivalent efficacy to direct installation on commercial agents. SHarD achieved an adjusted score of 100\%, matching the best securely configured commercial agent, with no regression across any test category. Notable observations include evidence that model non-determinism produces inconsistent security outcomes and that autonomous agent behavior can cross system boundaries in ways that OS sandboxing directly mitigates. Initial characteristics toward a control harness fitness framework are proposed, and a third research question is identified for future investigation.

## 내 메모


