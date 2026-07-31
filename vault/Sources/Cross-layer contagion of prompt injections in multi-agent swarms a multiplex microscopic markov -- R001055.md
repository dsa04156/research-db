---
type: research-source
item_id: 1055
title: "Cross-layer contagion of prompt injections in multi-agent swarms: a multiplex microscopic markov chain approach"
source: "openalex"
published: "2026-07-16"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1186/s42400-026-00628-w"
url: "https://doi.org/10.1186/s42400-026-00628-w"
generated_by: codex-research-db
aliases:
  - "Cross-layer contagion of prompt injections in multi-agent swarms: a multiplex microscopic markov chain approach"
topics:
  - "ai-agents"
---

# Cross-layer contagion of prompt injections in multi-agent swarms: a multiplex microscopic markov chain approach

[원문 열기](https://doi.org/10.1186/s42400-026-00628-w)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`Q64Q496B`)
- 발행일: 2026-07-16
- 저자: Tran Duc Le, Truong Duy Dinh, Thi Le Quyen Nguyen, Cong Danh Nguyen
- 식별자: `doi:10.1186/s42400-026-00628-w`

## 요약·초록

Abstract Large Language Models (LLMs) are increasingly deployed as interconnected agentic swarms that leverage the Model Context Protocol (MCP) to invoke shared external tools, APIs, and databases. In these settings, conventional security strategies based on agent-to-agent airgapping can be insufficient because agents that never directly communicate may still cross-infect one another through shared infrastructure tools, producing a “Confused Deputy” cascade. This paper develops a formal mathematical framework for modeling this cross-layer contagion in MCP-enabled multi-agent swarms. We construct a coupled multiplex Microscopic Markov Chain Approach (MMCA) that simultaneously tracks the node-level probability flow across two layers: an Agent cognitive layer (governed by Susceptible–Exposed–Infected–Quarantined (SEIQ) dynamics) and a Tool infrastructure layer (governed by Susceptible–Infected–Susceptible (SIS) dynamics). Our contributions are threefold: (i) we formulate a coupled multiplex MMCA with asymmetric SEIQ–SIS dynamics across agent and tool layers; (ii) we derive an analytical characterization of systemic risk, including an epidemic-threshold approximation via Next-Generation Matrix analysis and a closed-form budget-allocation rule under an exponential defense-efficiency model; and (iii) across eight experiment groups on synthetic and empirical agent-layer topologies, we show that shared-tool coupling consistently amplifies contagion and that tool-side controls can dominate agent-side hardening under the modeled regime. For cybersecurity practice, the framework identifies when shared tool infrastructure can transform localized prompt-injection events into system-level risk even under direct agent-to-agent isolation.

## 내 메모


