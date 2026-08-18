---
type: research-source
item_id: 1988
title: "CAPS: Compositional Attack Path Scoring for LLM Deployment Stacks"
source: "openalex"
published: "2026-08-12"
first_seen: "2026-08-14"
review_status: "pending"
canonical_key: "doi:10.47852/bonviewaia620210609"
url: "https://doi.org/10.47852/bonviewaia620210609"
generated_by: codex-research-db
aliases:
  - "CAPS: Compositional Attack Path Scoring for LLM Deployment Stacks"
topics:
  - "ai-agents"
---

# CAPS: Compositional Attack Path Scoring for LLM Deployment Stacks

[원문 열기](https://doi.org/10.47852/bonviewaia620210609)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-14|2026-08-14]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`NR77WUBI`)
- 발행일: 2026-08-12
- 저자: Quang-Vinh Dang, Hoang-Viet Vu, Ngoc-Son-An Nguyen, Minh Ngoc Dinh, Dat Le
- 식별자: `doi:10.47852/bonviewaia620210609`

## 요약·초록

Evaluating the security posture of large language model (LLM) deployment stacks is a critical challenge in modern AI security. Traditional vulnerability management frameworks—such as the Common Vulnerability Scoring System (CVSS) and component-level checklists—assume that software components can be evaluated in isolation. In real-world agentic and retrieval-augmented generation (RAG)-based LLM ecosystems, this assumption is systematically violated: attackers exploit complex topologies, chaining seemingly low–risk vulnerabilities (e.g., indirect prompt injection) with downstream tools (e.g., SQL execution) to achieve catastrophic compromises. Applying independent scoring methods to deeply integrated stacks therefore yields inflated risk assessments, misaligned mitigation priorities, and a failure to capture compositional attack paths. We propose Compositional Attack Path Scoring (CAPS), a framework engineered to quantify end-to-end multi-hop risks in LLM architectures. CAPS integrates three capabilities: (i) directed graph topological modeling, which maps the deployment stack from attacker entry points to high-value assets; (ii) dynamic mitigation attenuation, which calculates the “Effective Exploitability” of nodes based on deployed guardrails; and (iii) a compositional path engine that scores risk via an explicit exponential decay factor reflecting the friction of traversing trust boundaries. CAPS also provides an automated return on investment engine to rank mitigations by systemic risk reduction. Empirical evaluation on standardized architectures (RAG Chatbots, Autonomous Coding Agents, and Enterprise Model Routers) shows that CAPS improves risk calibration: against the Autonomous Agent benchmark, it computes a realistic critical path score of 51.3, correcting the naive 85.0 overestimation of component-level CVSS scoring. CAPS establishes a rigorous benchmark for quantitative vulnerability management in complex, agentic LLM environments. Received: 1 June 2026 | Revised: 15 July 2026 | Accepted: 31 July 2026 Conflicts of Interest The authors declare that they have no conflicts of interest to this work. Data Availability Statement The data that support the findings of this study are openly available in the CAPS repository [GitHub] at https://github.com/vinhqdang/CAPS-Compositional-Attack-Path-Scoring-for-LLM-Deployment-Stacks. Author Contribution Statement Quang-Vinh Dang: Conceptualization, Methodology, Software, Writing – original draft. Hoang-Viet Vu: Software, Validation, Visualization. Ngoc-Son-An Nguyen: Investigation, Data curation. Minh Ngoc Dinh: Formal analysis, Investigation. Dat Le: Writing – review &amp; editing, Supervision, Project administration.

## 내 메모


