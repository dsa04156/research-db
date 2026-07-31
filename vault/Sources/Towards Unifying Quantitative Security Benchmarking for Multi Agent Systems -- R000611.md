---
type: research-source
item_id: 611
title: "Towards Unifying Quantitative Security Benchmarking for Multi Agent Systems"
source: "arxiv"
published: "2025-07-23T13:51:28Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.21146"
url: "https://arxiv.org/abs/2507.21146v1"
generated_by: codex-research-db
aliases:
  - "Towards Unifying Quantitative Security Benchmarking for Multi Agent Systems"
topics:
  - "ai-agents"
---

# Towards Unifying Quantitative Security Benchmarking for Multi Agent Systems

[원문 열기](https://arxiv.org/abs/2507.21146v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`FCZ7R83X`)
- 발행일: 2025-07-23T13:51:28Z
- 저자: Gauri Sharma, Vidhi Kulkarni, Miles King, Ken Huang
- 식별자: `arxiv:2507.21146`

## 요약·초록

Evolving AI systems increasingly deploy multi-agent architectures where autonomous agents collaborate, share information, and delegate tasks through developing protocols. This connectivity, while powerful, introduces novel security risks. One such risk is a cascading risk: a breach in one agent can cascade through the system, compromising others by exploiting inter-agent trust. In tandem with OWASP's initiative for an Agentic AI Vulnerability Scoring System we define an attack vector, Agent Cascading Injection, analogous to Agent Impact Chain and Blast Radius, operating across networks of agents. In an ACI attack, a malicious input or tool exploit injected at one agent leads to cascading compromises and amplified downstream effects across agents that trust its outputs. We formalize this attack with an adversarial goal equation and key variables (compromised agent, injected exploit, polluted observations, etc.), capturing how a localized vulnerability can escalate into system-wide failure. We then analyze ACI's properties -- propagation chains, amplification factors, and inter-agent compound effects -- and map these to OWASP's emerging Agentic AI risk categories (e.g. Impact Chain and Orchestration Exploits). Finally, we argue that ACI highlights a critical need for quantitative benchmarking frameworks to evaluate the security of agent-to-agent communication protocols. We outline a methodology for stress-testing multi-agent systems (using architectures such as Google's A2A and Anthropic's MCP) against cascading trust failures, developing upon groundwork for measurable, standardized agent-to-agent security evaluation. Our work provides the necessary apparatus for engineers to benchmark system resilience, make data-driven architectural trade-offs, and develop robust defenses against a new generation of agentic threats.

## 내 메모


