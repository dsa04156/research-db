---
type: research-source
item_id: 2736
title: "OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows"
source: "arxiv"
published: "2026-09-05T12:16:47Z"
first_seen: "2026-09-10"
review_status: "pending"
canonical_key: "arxiv:2609.09203"
url: "https://arxiv.org/abs/2609.09203v1"
generated_by: codex-research-db
aliases:
  - "OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows"
topics:
  - "self-evolving-harness"
---

# OpenDiscoveryTrace: Process Traces for Evaluating AI Scientist Workflows

[원문 열기](https://arxiv.org/abs/2609.09203v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-10|2026-09-10]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-05T12:16:47Z
- 저자: Aayam Bansal, Keertan Balaji
- 식별자: `arxiv:2609.09203`

## 요약·초록

Existing benchmarks for autonomous AI scientists evaluate only final outputs---generated code, hypotheses, or papers---yet discard the reasoning process by which those outputs were obtained. This makes it impossible to audit scientific methodology, diagnose failure modes, or distinguish systematic reasoning from fortunate guessing. We present \textbf{OpenDiscoveryTrace}, a public dataset of 558 complete AI scientific agent trajectories that captures how models reason, not just what they produce. Each trajectory records a structured 9-field-per-step trace---including thoughts, tool calls, observations, errors, revision triggers, and self-reported confidence---as models execute 124 scientific tasks spanning drug discovery, materials science, genomics, and scientific literature analysis. The dataset covers seven models: three frontier models (GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro; 124 trajectories each, fully balanced across domains and difficulty levels) and four open-weight models (Qwen2.5-7B, Mistral-7B-v0.3, Phi-3.5-mini, and Qwen2.5-1.5B; 30 each), plus 60 live-retrieval variant trajectories. Pilot analysis on 363 LLM-judged trajectories reveals that process traces expose behavioral differences invisible to output-only evaluation: all three frontier models achieve comparable success rates (84--89%), yet Claude Opus 4.6 produces 30$\times$ more errors than GPT-5.4 (2.5 vs. 0.08 per trajectory, $p < 0.0001$, Cliff's $δ= 0.613$), with qualitatively different error profiles---66.7% tool misuse for Claude versus 83.6% reasoning errors for GPT-5.4. We define five benchmark tasks with baselines from logistic regression, random forests, LSTMs, and Transformer models. The dataset, trace schema, agent harness, and benchmark definitions are publicly available under CC BY 4.0 to support research on process-level evaluation, scientific agent auditing, and AI governance.

## 내 메모


