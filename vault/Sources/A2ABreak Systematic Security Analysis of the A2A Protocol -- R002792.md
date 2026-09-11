---
type: research-source
item_id: 2792
title: "A2ABreak: Systematic Security Analysis of the A2A Protocol"
source: "arxiv"
published: "2026-09-09T22:18:36Z"
first_seen: "2026-09-11"
review_status: "pending"
canonical_key: "arxiv:2609.10871"
url: "https://arxiv.org/abs/2609.10871v1"
generated_by: codex-research-db
aliases:
  - "A2ABreak: Systematic Security Analysis of the A2A Protocol"
topics:
  - "ai-agents"
---

# A2ABreak: Systematic Security Analysis of the A2A Protocol

[원문 열기](https://arxiv.org/abs/2609.10871v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-11|2026-09-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-09T22:18:36Z
- 저자: Alireza Lotfi, Mirza Masfiqur Rahman, Imtiaz Karim, Elisa Bertino
- 식별자: `arxiv:2609.10871`

## 요약·초록

The Agent2Agent (A2A) protocol, now governed by the Linux Foundation, is an open standard that enables autonomous AI agents to discover, authenticate with, and delegate tasks to one another across organizational boundaries. Designed to complement the Model Context Protocol (MCP) for tool integration, A2A is rapidly emerging as the horizontal communication layer of the multi-agent ecosystem. Yet the protocol's security has received no systematic analysis. This paper presents A2ABreak, the first rigorous systematic security analysis of the A2A protocol. We introduce a novel framework that utilizes an LLM-assisted extraction of a verified finite-state machine directly from the natural-language specification, producing a unified model of 37 states and 76 transitions from 929 formalized statements, and then systematically reasons over this model to discover protocol-level vulnerabilities through adversarial verification, under a full-compliance assumption. Our analysis uncovers 11 new vulnerabilities, each exploitable by a specification-compliant adversary without requiring any implementation flaw. Among the findings are cross-client context injection through unprotected context identifiers, credential harvesting via multi-hop identity loss in delegation chains, and data exfiltration through rogue agents advertising unattested capability claims. A2ABreak achieves 73.3% precision and 84.6% F1 against independent expert review, while a zero-shot LLM baseline operating over the same specification produces zero confirmed findings, demonstrating that explicit formal grounding is essential for sound protocol security analysis.

## 내 메모


