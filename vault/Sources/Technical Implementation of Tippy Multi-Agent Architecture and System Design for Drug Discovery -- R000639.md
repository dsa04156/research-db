---
type: research-source
item_id: 639
title: "Technical Implementation of Tippy: Multi-Agent Architecture and System Design for Drug Discovery Laboratory Automation"
source: "arxiv"
published: "2025-07-18T17:57:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.17852"
url: "https://arxiv.org/abs/2507.17852v1"
generated_by: codex-research-db
aliases:
  - "Technical Implementation of Tippy: Multi-Agent Architecture and System Design for Drug Discovery Laboratory Automation"
topics:
  - "ai-agents"
  - "kubernetes"
---

# Technical Implementation of Tippy: Multi-Agent Architecture and System Design for Drug Discovery Laboratory Automation

[원문 열기](https://arxiv.org/abs/2507.17852v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MEJHRKVQ`)
- 발행일: 2025-07-18T17:57:40Z
- 저자: Yao Fehlis, Charles Crain, Aidan Jensen, Michael Watson, James Juhasz, Paul Mandel, Betty Liu, Shawn Mahon, Daren Wilson, Nick Lynch-Jonely, Ben Leedom, David Fuller
- 식별자: `arxiv:2507.17852`

## 요약·초록

Building on the conceptual framework presented in our previous work on agentic AI for pharmaceutical research, this paper provides a comprehensive technical analysis of Tippy's multi-agent system implementation for drug discovery laboratory automation. We present a distributed microservices architecture featuring five specialized agents (Supervisor, Molecule, Lab, Analysis, and Report) that coordinate through OpenAI Agents SDK orchestration and access laboratory tools via the Model Context Protocol (MCP). The system architecture encompasses agent-specific tool integration, asynchronous communication patterns, and comprehensive configuration management through Git-based tracking. Our production deployment strategy utilizes Kubernetes container orchestration with Helm charts, Docker containerization, and CI/CD pipelines for automated testing and deployment. The implementation integrates vector databases for RAG functionality and employs an Envoy reverse proxy for secure external access. This work demonstrates how specialized AI agents can effectively coordinate complex laboratory workflows while maintaining security, scalability, reliability, and integration with existing laboratory infrastructure through standardized protocols.

## 내 메모


