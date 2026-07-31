---
type: research-source
item_id: 999
title: "Global Merger-Arbitrage Forecasting with Language Models"
source: "arxiv"
published: "2026-07-10T19:16:03Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.09921"
url: "https://arxiv.org/abs/2607.09921v1"
generated_by: codex-research-db
aliases:
  - "Global Merger-Arbitrage Forecasting with Language Models"
topics:
  - "self-evolving-harness"
---

# Global Merger-Arbitrage Forecasting with Language Models

[원문 열기](https://arxiv.org/abs/2607.09921v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`DGM7G4WI`)
- 발행일: 2026-07-10T19:16:03Z
- 저자: Hinal Jajal, Michal Mucha, Charles Sweat, Chris Pulman, Charlie Flanagan, Peter Anderson
- 식별자: `arxiv:2607.09921`

## 요약·초록

We present a language-model forecasting system for merger arbitrage, a specialized high-stakes financial setting in which the task is to predict the outcome of announced M\&A deals. Unlike prior work on judgmental forecasting with LLMs, which has focused on broad mixed-topic benchmarks and short context such as news snippets, we study a setting that requires long-context reasoning over hundreds of pages of technical documents. Our system combines expert-guided context engineering with finetuning on hindsight-guided reasoning traces derived from historical deals. Given an announced deal, it outputs a probability distribution over three mutually exclusive outcomes: closing at announced terms, a higher bid, or deal termination. On an out-of-sample set of more than 400 large deals spanning 42 countries, our finetuned system achieves the best performance of any method we evaluate, reducing class-balanced Brier score to 0.151. This is 24\% below calibrated market-implied probabilities, 19\% below XGBoost, and 25-42\% below frontier language models. These results, together with ablation studies, show that LLM-based forecasting can succeed in specialized, long-context financial workflows, with hindsight-based supervision and expert-designed context playing a critical role.

## 내 메모


