---
type: research-source
item_id: 2330
title: "Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence"
source: "arxiv"
published: "2026-08-26T14:41:24Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.25869"
url: "https://arxiv.org/abs/2608.25869v1"
generated_by: codex-research-db
aliases:
  - "Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence"
topics:
  - "self-evolving-harness"
---

# Anchoring Bias in LLM-as-a-Judge Systems: Prior Scores Compromise Evaluation Independence

[원문 열기](https://arxiv.org/abs/2608.25869v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`29N9HPZZ`)
- 발행일: 2026-08-26T14:41:24Z
- 저자: Ante Kapetanovic, Kemal Altwlkany, Andro Mercep, Tomislav Duricic, Emanuel Lacic
- 식별자: `arxiv:2608.25869`

## 요약·초록

Large language models (LLMs) increasingly assess generated content, giving rise to the LLM-as-a-Judge paradigm. These systems now score outputs, filter content, and gate iterative refinement in production pipelines, where each judgment is often assumed to be independent of earlier evaluations. We test this assumption using three prompt conditions: no metadata, revision framing, and anchored metadata containing revision, attempt, and prior-score fields. We show that prior scores, even when included only as context metadata, anchor judgments and systematically shift ratings toward their values. Across 192,000 attempted evaluations (185,271 successful), seven out of the eight evaluated models have 95% task-stratified bootstrap intervals below zero for the total anchored-metadata effect on 20 fixed texts. Cohen's $d$, a standardized measure of the difference between score distributions, reaches an absolute value of 0.71. Token-level analysis of selected model-task probes suggests a threshold-like response pattern: introducing anchored metadata produces a marked redistribution of output-score probabilities, while changing the anchor value within the tested below-threshold range produces comparatively little additional variation. On categorical industry data with human-labeled ground truth, anchored metadata blocks 48% of error corrections and flips 10.18% of correct judgments toward an assigned wrong label, demonstrating the bias extends beyond numerical scoring to categorical decisions. Neither Chain-of-Thought nor a metadata-disregard warning reduces the total effect, although the warning improves the paired accuracy effect relative to baseline in the industry experiment. Reliable LLM evaluation demands careful context engineering rather than an assumption of impartiality. Effective mitigation must be validated for the intended model and task or domain.

## 내 메모


