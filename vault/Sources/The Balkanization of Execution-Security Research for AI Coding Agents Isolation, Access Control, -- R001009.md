---
type: research-source
item_id: 1009
title: "The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities"
source: "arxiv"
published: "2026-07-07T01:56:18Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.05743"
url: "https://arxiv.org/abs/2607.05743v1"
generated_by: codex-research-db
aliases:
  - "The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities"
topics:
  - "self-evolving-harness"
---

# The Balkanization of Execution-Security Research for AI Coding Agents: Isolation, Access Control, and Time-of-Check-to-Time-of-Use Vulnerabilities

[원문 열기](https://arxiv.org/abs/2607.05743v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`EJ5S4GFP`)
- 발행일: 2026-07-07T01:56:18Z
- 저자: Mohammadreza Rashidi
- 식별자: `arxiv:2607.05743`

## 요약·초록

AI coding agents now read repositories, call tools, and execute shell commands with limited human oversight, and a fast-growing body of work studies whether the execution layer around them is actually safe. That literature is scattered. Papers on sandbox isolation, capability and access control, policy enforcement, time-of-check-to-time-of-use (TOCTOU) races, Model Context Protocol (MCP) threats, identity delegation, execution provenance, network egress control, and static analysis of agent-generated code are published independently and rarely cite one another. We systematize 39 papers published between 2023 and 2026 into 17 categories, each verified directly against its source. The same verification protocol also confirms four disclosed, patched CVEs directly affecting production agent harnesses. Reading across categories surfaces five cross-cutting gaps that no single paper addresses. (1) Isolation architectures and capability models are almost never evaluated against one another on a shared benchmark. (2) Policy-enforcement studies report failure rates from 69% to 98% of real denylists, yet no isolation paper re-evaluates its own defense under that adversarial setting. (3) TOCTOU and MCP threats are analyzed as separate literatures despite both being instances of the same state-validation problem. (4) Every enforcement mechanism assumes an honest policy author, leaving policy-authoring error itself unaddressed. (5) Benign but out-of-scope agent actions occurring at rates up to 17.1% under realistic prompting are addressed by no access-control or capability paper in the corpus. Existing broader surveys of agentic AI security discuss sandboxing only as one item among many defenses, leaving execution security without a dedicated systematization. This paper is written to fill that gap. We conclude with a research agenda directed at the five gaps.

## 내 메모


