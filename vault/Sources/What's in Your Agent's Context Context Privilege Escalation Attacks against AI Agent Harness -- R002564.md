---
type: research-source
item_id: 2564
title: "What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness"
source: "arxiv"
published: "2026-09-01T13:26:21Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.01222"
url: "https://arxiv.org/abs/2609.01222v2"
generated_by: codex-research-db
aliases:
  - "What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# What's in Your Agent's Context? Context Privilege Escalation Attacks against AI Agent Harness

[원문 열기](https://arxiv.org/abs/2609.01222v2)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-01T13:26:21Z
- 저자: Zichuan Li, Jian Cui, Ashley Chen, Xiaojing Liao, Luyi Xing
- 식별자: `arxiv:2609.01222`

## 요약·초록

Real-world, high-profile AI agent harnesses often rely on vendor-proprietary or opaque designs for context assembly, leaving the sources and underlying logic of assembled context poorly understood and the resulting security risks largely unexplored. In this paper, we present the first systematic analysis of context assembly designs in real-world AI agent harnesses. We study and uncover how an agent harness is designed to collect and assemble context from diverse sources, and identify a set of practical attack vectors arising from these designs. Our analysis brings to light two novel categories of attacks in the context assembly of real-world harnesses: (1) MessageRole Context Privilege Escalation (M-CPE), which occurs when attacker-controlled content originating from a low-privileged context is incorporated into a higher-privileged message role. (2) Cross-Scope Context Privilege Escalation (X-CPE), which occurs when attacker-controlled content persists beyond the context in which it was introduced. We performed a systemic security analysis of the CPE attacks against 12 real-world agent harnesses, including Claude Code and Codex. The resulting consequences include full agent compromise, remote code execution, denial of service, and manipulated tool or skill invocations, etc.

## 내 메모


