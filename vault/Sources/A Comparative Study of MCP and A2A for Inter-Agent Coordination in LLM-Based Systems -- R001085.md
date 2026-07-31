---
type: research-source
item_id: 1085
title: "A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems"
source: "arxiv"
published: "2026-07-26T23:05:08Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.23884"
url: "https://arxiv.org/abs/2607.23884v1"
generated_by: codex-research-db
aliases:
  - "A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems"
topics:
  - "ai-agents"
---

# A Comparative Study of MCP and A2A for Inter-Agent Coordination in LLM-Based Systems

[원문 열기](https://arxiv.org/abs/2607.23884v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FGZ4RAFP`)
- 발행일: 2026-07-26T23:05:08Z
- 저자: Ionut Predoaia, Tuong Manh Vu, Konstantinos Barmpis, Dimitris Kolovos, Antonio García-Domínguez
- 식별자: `arxiv:2607.23884`

## 요약·초록

Recent industry practice has seen the rapid emergence of agentic systems composed of heterogeneous, tool- and LLM-mediated agent components, raising practical questions about inter-agent coordination and protocol design. This paper presents an implementation-grounded comparison of the Model Context Protocol (MCP) and the Agent2Agent (A2A) protocol, from a multi-agent systems engineering perspective, using an inter-agent coordination scenario involving LLM-based agents. We evaluate an MCP-based and an A2A-based multi-agent implementation of the same software engineering task against a set of requirements derived from prior literature and discussions with industry partners, including agent discoverability, multi-part messaging, multi-turn conversations, asynchronous communication, observability, interoperability, and access control. The results evidence that MCP can support inter-agent coordination in constrained LLM-based systems through a comparatively lightweight implementation model with lower coordination complexity, although coordination concerns such as conversational state management and task lifecycle handling must be implemented explicitly at the application layer. In contrast, A2A provides richer native support for stateful, multi-turn coordination through protocol-level abstractions for tasks and lifecycle management, but this comes with substantially greater implementation and coordination complexity. Given the narrow scope of the evaluated coordination pattern, these findings are presented as design observations from an empirical experience report rather than general claims of protocol suitability or superiority across broader classes of MAS, highlighting trade-offs and how protocol abstractions shape the distribution of coordination responsibilities in contemporary agentic systems.

## 내 메모


