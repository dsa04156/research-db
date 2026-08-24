---
type: research-source
item_id: 2173
title: "Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents"
source: "arxiv"
published: "2026-08-21T00:14:38Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.20631"
url: "https://arxiv.org/abs/2608.20631v1"
generated_by: codex-research-db
aliases:
  - "Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents"
topics:
  - "ai-agents"
---

# Weighted Memory Tree: Remembering What Matters for Long-Horizon LLM Agents

[원문 열기](https://arxiv.org/abs/2608.20631v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-21T00:14:38Z
- 저자: Quang Dao, Purvi Kathalkar, Kenneth Eaton
- 식별자: `arxiv:2608.20631`

## 요약·초록

Large language model (LLM) agents have demonstrated the ability to solve multi-step tasks requiring planning, tool use, and external information access, yet growing execution histories increase inference cost and expose reasoning to outdated, irrelevant, or misleading information, potentially degrading reasoning quality. Existing memory approaches organize or compress execution histories but provide limited mechanisms for deciding which memories remain active. We introduce the, a hierarchical memory system that organizes execution into tasks, subtasks, and actions while assigning each memory a dynamic retention score. Event-based updates and selection-based decay revise these scores, allowing WMT to preserve useful information, fold completed trajectories, suppress low-utility content, and retain access to folded context. We evaluate WMT on GAIA-Text using Qwen3-8B, Gemma 4 E4B, and Llama-3.1-8B, with ablations and memory-poisoning experiments. Relative to linear memory, WMT improves accuracy by an average of 9.97 percentage points while reducing prompt-token usage by 32.8%. Memory-poisoning experiments show that WMT limits the persistence and propagation of unreliable information. Our results suggest that effective long-horizon agent memory depends less on storing more information than on deciding which information should remain active.

## 내 메모


