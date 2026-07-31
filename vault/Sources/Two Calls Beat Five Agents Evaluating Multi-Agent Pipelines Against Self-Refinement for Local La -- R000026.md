---
type: research-source
item_id: 26
title: "Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models"
source: "arxiv"
published: "2026-07-29T13:53:02Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26922"
url: "https://arxiv.org/abs/2607.26922v1"
generated_by: codex-research-db
aliases:
  - "Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models"
topics:
  - "ai-agents"
---

# Two Calls Beat Five Agents: Evaluating Multi-Agent Pipelines Against Self-Refinement for Local Language Models

[원문 열기](https://arxiv.org/abs/2607.26922v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`4M4BHGMV`)
- 발행일: 2026-07-29T13:53:02Z
- 저자: Ashish Prajapati, Om Mohite
- 식별자: `arxiv:2607.26922`

## 요약·초록

Multi-agent LLM pipeline systems break down the task among multiple roles for better reasoning, but are benchmarked mainly with large-scale commercial models. In this study, we investigate Parishad, a structured multi-agent system involving five roles, by deploying it on Qwen2.5-7B-Instruct, a local model, on two datasets: GSM8K (500 questions) and HumanEval (164 questions), compared with prompting directly and two-call self-refinement. The multi-agent system drops GSM8K accuracy from 75.0\% to 45.0\% with JSON data format due to the error accumulation problem. With plaintext format, the accuracy is restored to 82.0\%. A two-call self-refinement strategy (V1) can achieve 86.2\% accuracy on GSM8K, with 7.4$\times$ lower token usage. However, the same V1 implementation on HumanEval---where direct accuracy is already 96.3\%---actively destroys performance (66.5\%). A task-aware gated redesign (V2) applied to HumanEval preserves accuracy at 95.1\%. Our results demonstrate that communication format and implementation details determine outcomes more than architectural complexity, and that simpler approaches match or outperform multi-agent pipelines for local 7B model deployment. All code and data are released.

## 내 메모


