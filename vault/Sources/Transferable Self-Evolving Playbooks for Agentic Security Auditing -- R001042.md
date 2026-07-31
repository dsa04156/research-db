---
type: research-source
item_id: 1042
title: "Transferable Self-Evolving Playbooks for Agentic Security Auditing"
source: "arxiv"
published: "2026-06-15T08:57:45Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.16420"
url: "https://arxiv.org/abs/2606.16420v1"
generated_by: codex-research-db
aliases:
  - "Transferable Self-Evolving Playbooks for Agentic Security Auditing"
topics:
  - "self-evolving-harness"
---

# Transferable Self-Evolving Playbooks for Agentic Security Auditing

[원문 열기](https://arxiv.org/abs/2606.16420v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`5BWV6C2Z`)
- 발행일: 2026-06-15T08:57:45Z
- 저자: Ziyue Wang, Cheuk Wang Maurice Ng, Chenchen Yu, Strick Sheng, Kaihua Qin, Liyi Zhou
- 식별자: `arxiv:2606.16420`

## 요약·초록

An LLM agent for vulnerability discovery and validation is more than a model. It combines three components: an LLM for code analysis, an agent harness such as Codex or OpenCode for navigation, tool use, and execution, and an audit playbook, domain-specific procedural knowledge that guides the LLM and harness toward vulnerability discovery. Prior work relies on human-supplied playbooks, including prompt engineering, manual workflows, knowledge bases, and heuristics. This raises two research questions: Acquisition - is human curation necessary, and can playbook creation be automated? Transfer - can an evolved playbook transfer the audit procedure to weaker agents, improving their capability? We present EvoHunt, a playbook evolution environment over open-source repositories for security auditing. Three agents drive the evolution loop: an audit agent rolls out the current playbook and produces findings; an evaluator scores outcomes against ground truth; and a reviser commits updates to the playbook based on failure analysis. The playbook format is unconstrained: starting empty, EvoHunt adds or removes workflows, heuristics, vulnerability knowledge, or domain-specific content. The evolved playbook requires only minor adaptation to run under a different LLM or harness. We evaluate EvoHunt on open-source security advisories. For acquisition, playbook evolution raises end-to-end exploits for Codex/GPT5.4-xhigh 6x, from 1.1% to 6.2%, and the evolved OpenCode/GLM5.1 playbook surpasses OpenAI Codex Security on every metric, with 11.3% vs. 9.2% target-match rate, showing open-source evolution can outperform a dedicated commercial product. For transfer, the GLM-evolved playbook gives the strongest student lift: Qwen3.6-27B improves from 2.4% to 6.5%, Qwen3.6-35B-A3B from 1.1% to 4.6%, and A3B obtains 2.4x more matches than GPT transfer.

## 내 메모


