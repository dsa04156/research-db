---
type: research-source
item_id: 2572
title: "Speculative Macro Commit for Faster Tool-Using Agents"
source: "arxiv"
published: "2026-09-03T00:31:43Z"
first_seen: "2026-09-04"
review_status: "pending"
canonical_key: "arxiv:2609.03236"
url: "https://arxiv.org/abs/2609.03236v1"
generated_by: codex-research-db
aliases:
  - "Speculative Macro Commit for Faster Tool-Using Agents"
topics:
  - "ai-agents"
---

# Speculative Macro Commit for Faster Tool-Using Agents

[원문 열기](https://arxiv.org/abs/2609.03236v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-04|2026-09-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-03T00:31:43Z
- 저자: Zeyu Liu, Souvik Kundu, Peter A. Beerel
- 식별자: `arxiv:2609.03236`

## 요약·초록

Tool-using LLM agents spend wall-clock time not only on model inference but also in serial action--observation turns, where each tool call, environment transition, and observation can delay subsequent decisions. We introduce \textbf{Speculative Macro Commit} (SMC), a runtime mechanism for a two-tier agent system: a large authoritative actor model produces the official trajectory, while a faster speculative drafter model continuously predicts and executes future action chains on an isolated environment snapshot. SMC mines recurring multi-action skeletons from training traces and stores them in a macro library used to match against action chains predicted by the drafter at runtime. When the actor's next tool call matches the first drafted action, SMC commits the remaining pre-executed draft steps, together with their observations, to the official trajectory. Using Qwen3.5-27B INT4 as the authoritative actor model and Qwen3.5-4B as the speculative drafter model, SMC matches the sequential agent's overall accuracy while reducing latency by 10.23\% over the Speculative Actions (SA) baseline and 18.59\% over sequential execution on the $τ^2$-Bench Telecom subset. On AppWorld, SMC reduces wall time by 7.7\% over SA baseline and 44.9\% over sequential execution, with a small reduction in task completion. Overall, SMC provides a practical way to reuse multi-step speculative execution and reduce agent latency beyond single-step speculative actions. Our code is publicly available \href{https://github.com/zeyuliu1037/speculative-macro-commit}{\textcolor{magenta}{here}}.

## 내 메모


