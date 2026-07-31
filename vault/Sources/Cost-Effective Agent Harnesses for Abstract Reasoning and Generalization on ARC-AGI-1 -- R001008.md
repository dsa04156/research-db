---
type: research-source
item_id: 1008
title: "Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1"
source: "arxiv"
published: "2026-07-07T19:49:35Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.06764"
url: "https://arxiv.org/abs/2607.06764v1"
generated_by: codex-research-db
aliases:
  - "Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1"
topics:
  - "self-evolving-harness"
---

# Cost-Effective Agent Harnesses for Abstract Reasoning and Generalization on ARC-AGI-1

[원문 열기](https://arxiv.org/abs/2607.06764v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`TTF4J9BN`)
- 발행일: 2026-07-07T19:49:35Z
- 저자: Kabir Moghe, Peter Chin
- 식별자: `arxiv:2607.06764`

## 요약·초록

Recent progress on ARC-AGI-1 from disclosed architectures has come broadly from two regimes: heavy test-time compute over frontier models (evolutionary search, exhaustive sampling, extended chain-of-thought), or benchmark-specific training in which small models are fine-tuned on ARC data, often with task-specialized architectures. We study a third regime: an open-weight model in non-thinking mode (DeepSeek V3.2) under a strict budget, with no ARC-specific fine-tuning. We study what is recoverable through architecture alone, building agentic harnesses that decompose pattern-discovery and program-synthesis stages explicitly. First, we introduce an Explorer-Definer Pipeline that separates pattern discovery from executable transformation synthesis, implemented as a two-stage agent pipeline. Next, we present the Reflective Orchestrator, which augments the pipeline with autonomous exploration of new transformations when previous hypotheses fail on training pairs. On the ARC-AGI-1 public 400-task evaluation set, the pipeline reaches 57.50% pass@2 at \$0.25 per task, and the orchestrator reaches 67.25% pass@2 at \$0.62 per task. Together these architectures lift a 15.50% one-shot baseline by ~52 points without benchmark-specific training or heavy test-time compute. Furthermore, the orchestrator-driven lift tests a falsifiable diagnostic the pipeline produces; unbiased pass@k analysis suggests the pipeline is generation-bound, not selection-bound (selection via training-pair accuracy captures ~95% of the candidate ceiling) and predicts that significant improvement requires broader generation, not better ranking. The orchestrator implements this prediction via adaptive re-exploration and confirms it (unbiased pass@1 lift +9.81 pp, matching selection-mediated pass@2 lift). An additional pipeline ablation identifies its think tool as a significant component, with removal reducing pass@2 by 5.75 pp.

## 내 메모


