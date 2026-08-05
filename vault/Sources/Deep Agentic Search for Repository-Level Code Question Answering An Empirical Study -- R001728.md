---
type: research-source
item_id: 1728
title: "Deep Agentic Search for Repository-Level Code Question Answering: An Empirical Study"
source: "arxiv"
published: "2026-08-02T21:36:59Z"
first_seen: "2026-08-05"
review_status: "pending"
canonical_key: "arxiv:2608.01507"
url: "https://arxiv.org/abs/2608.01507v1"
generated_by: codex-research-db
aliases:
  - "Deep Agentic Search for Repository-Level Code Question Answering: An Empirical Study"
topics:
  - "self-evolving-harness"
---

# Deep Agentic Search for Repository-Level Code Question Answering: An Empirical Study

[원문 열기](https://arxiv.org/abs/2608.01507v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-08-05|2026-08-05]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KKV2S8E8`)
- 발행일: 2026-08-02T21:36:59Z
- 저자: Amirkia Rafiei Oskooei, Bora Ilci, Alperen Kayim, Mehmet Egemen Uzun, Berat Can, Kaan Emre Kara, Ozan Orhan, Mehmet S. Aktas
- 식별자: `arxiv:2608.01507`

## 요약·초록

Code agents spend much of their effort simply locating the right code inside a repository. Two approaches dominate current practice. In Semantic Search, the agent retrieves code blocks from a vector index built from the repository in advance. In Deep Agentic Search (also known as grep-search by subagent), a planning agent delegates the exploration to a separate subagent that works in an isolated context window and returns only a condensed result. The second design, which is considered good context engineering practice, exists to protect the main agent from context pollution (also known as context rot), the loss of accuracy that occurs as unrelated material accumulates in the context window. Recent code agents (such as Claude Code, Codex, Antigravity, etc) have adopted it quickly, but there is little evidence on whether it produces better answers. We compare the two approaches on SWE-QA, a benchmark for repository-level code question answering. Semantic search answered 65.2% of questions correctly against 46.2% for deep agentic search, and it produced each correct answer at less than half the cost. To explain the gap, we then coded every failed run into a taxonomy of failure modes. The taxonomy shows that deep agentic search did not remove failures but introduced a new class of them: the single largest share of its failures, 41.8%, occurred at the hand-off between the planner and its sub-agent, and these were usually silent, ending in a fluent and confident answer that was wrong. Deep agentic search addresses a real problem and is now the preferred design in many code agents. However, our results show that the protection it offers may not be free, and that for read-only questions over a repository that can be indexed, retrieval was the stronger and cheaper option.

## 내 메모


