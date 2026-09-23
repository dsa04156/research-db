---
type: research-source
item_id: 3058
title: "An Autonomous Agentic Query Framework with MCP Tools and Modernized NIST SRD-46 for Accelerating Aqueous Speciation Analysis"
source: "openalex"
published: "2026-09-21"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "doi:10.5281/zenodo.21226515"
url: "https://doi.org/10.5281/zenodo.21226515"
generated_by: codex-research-db
aliases:
  - "An Autonomous Agentic Query Framework with MCP Tools and Modernized NIST SRD-46 for Accelerating Aqueous Speciation Analysis"
topics:
  - "ai-agents"
---

# An Autonomous Agentic Query Framework with MCP Tools and Modernized NIST SRD-46 for Accelerating Aqueous Speciation Analysis

[원문 열기](https://doi.org/10.5281/zenodo.21226515)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-09-21
- 저자: Yunkai0825, Adwaith Ravichandran, Hassan Harb, Rajeev S. Assary, Ingram Brian, Zhenzhen Yang
- 식별자: `doi:10.5281/zenodo.21226515`

## 요약·초록

Large language models (LLMs) could automate reasoning over structured scientific databases in chemistry and materials science, but this requires purpose-built agentic architectures, not simply better models. We present an agentic workflow for systematically querying and extracting data from the NIST Standard Reference Database 46 (SRD-46) to perform autonomous speciation and thermodynamic analysis, with three contributions: (1) a hierarchical toolset, served by Model Context Protocol (MCP) framework, which converts natural-language scientific questions into validated SQL over a database enriched with canonical chemical identifiers, equilibrium-reaction maps, and fingerprint-similarity matrices; (2) an induction-deduction-validation reasoning loop with compactors that preserve key chemical context across multi-turn sessions under dynamic memory limits within the same session; and (3) a soft time/turn-budget hook that maintains coherent reasoning within resource constraints. The resulting framework is LLM-agnostic and spans queries from direct lookups to cross-species comparisons to open-ended tasks like estimating unknown Fe complexation constants and selecting ligands for acidic Fe electrodeposition. We benchmark four frontier models (Claude Opus 4.6, Claude Sonnet 4.6, GPT-5, and GPT-5.4) on 49 prompts across four complexity levels, repeated five times (~1,000 answers), using automated claim-level validation and regex-based tool-result matching. All models retrieve reliably on direct-lookup tasks, confirming the architecture bridges natural-language reasoning and structured database access. Beyond lookups, behaviors of models diverge: GPT-5.4 converges rapidly with high per-claim verifiability but limited exploratory depth, whereas Opus 4.6 pursues broader, cross-examined reasoning at the cost of slower convergence and more unsupported claims. This reveals a fundamental tradeoff between convergent efficiency and exploratory breadth on fuzzy scientific queries that scalar benchmarks cannot resolve. It also suggests that fuzzy scientific queries require expert-stewarded reasoning, not faster convergence criteria or higher benchmark metrics alone. Our results demonstrate that domain-expert-designed agentic architectures and evaluation frameworks are essential infrastructure for AI-driven scientific discovery, and that mixed-model deployment strategies may be needed to balance efficiency and explanatory depth for different classes of scientific questions. Revision v1.0.0(R) documents a newly validated Python environment, packages the supplied large databases in lossless ordinary ZIPs with automatic verified local restoration, and updates installation and database documentation. The dependency lock was prepared on 21 September 2026; it does not reconstruct the historical experiment environment, and no benchmark results were regenerated.

## 내 메모
