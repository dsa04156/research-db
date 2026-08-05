---
type: research-source
item_id: 1688
title: "Cross-Model Behavioral Fingerprinting for Backdoor Detection in Enterprise AI Agent Supply Chains"
source: "openalex"
published: "2026-08-02"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "doi:10.5281/zenodo.21758195"
url: "https://doi.org/10.5281/zenodo.21758195"
generated_by: codex-research-db
aliases:
  - "Cross-Model Behavioral Fingerprinting for Backdoor Detection in Enterprise AI Agent Supply Chains"
topics:
  - "ai-agents"
---

# Cross-Model Behavioral Fingerprinting for Backdoor Detection in Enterprise AI Agent Supply Chains

[원문 열기](https://doi.org/10.5281/zenodo.21758195)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`RIPMKRCW`)
- 발행일: 2026-08-02
- 저자: Chang Lyu, Qiang Fu
- 식별자: `doi:10.5281/zenodo.21758195`

## 요약·초록

This work presents CloudGuard, a model-agnostic security framework for detecting backdoors and persistent state manipulation in enterprise AI agent supply chains. The framework extends behavioral fingerprinting beyond stateless tool execution by integrating software provenance, capability-normalized execution traces, data-flow and privilege transitions, conversational context, persistent memory, retrieval events, claim–evidence relationships, and downstream external effects into a Stateful Behavior-Provenance Graph. CloudGuard addresses heterogeneous enterprise environments in which AI agents may use different large language models, tool frameworks, Model Context Protocol servers, skills, plugins, retrieval systems, and long-term memory components. Its security controls include supply-chain provenance verification, write-time memory admission, read-time state re-evaluation, taint propagation, counterfactual influence analysis, open-set risk calibration, three-way ALLOW–STEP-UP–BLOCK enforcement, and signed behavioral attestation for runtime drift detection. The accompanying controlled evidence package contains two reproducible synthetic mechanism benchmarks. CMBF-Sim evaluates cross-model-style behavioral invariance under tool aliases, timing differences, retry behavior, telemetry loss, provenance manipulation, and previously unseen attack families. CMBF-State evaluates distributed conversational triggers, persistent memory poisoning, context-compaction poisoning, false-precedent insertion, procedure-memory manipulation, and trigger-conditioned semantic steering across linked write, persistence, retrieval, influence, and consequence stages. All reported experimental results are explicitly limited to controlled synthetic settings. They demonstrate internal mechanism behavior and failure boundaries, but do not establish production detection accuracy or effectiveness on real enterprise deployments. The manuscript therefore separates reproducible mechanism evidence from future validation requirements involving real multi-LLM executions, public agent-security benchmarks, independently governed enterprise data, adaptive red-team testing, and analyst-centered evaluations. Authors: Leo Lv(Lyu Chang) and Felix Fu(Fu Qiang)Affiliations: FLYINGNETS PTE. LTD., Singapore; Flyingnets株式会社, Tokyo, Japan.

## 내 메모


