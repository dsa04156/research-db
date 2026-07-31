---
type: research-source
item_id: 1033
title: "Code Isn't Memory: A Structural Codebase Index Inside a Coding Agent"
source: "arxiv"
published: "2026-06-21T10:10:51Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.22417"
url: "https://arxiv.org/abs/2606.22417v1"
generated_by: codex-research-db
aliases:
  - "Code Isn't Memory: A Structural Codebase Index Inside a Coding Agent"
topics:
  - "self-evolving-harness"
---

# Code Isn't Memory: A Structural Codebase Index Inside a Coding Agent

[원문 열기](https://arxiv.org/abs/2606.22417v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`9NE7AN3B`)
- 발행일: 2026-06-21T10:10:51Z
- 저자: Ishaan Bhola, Adithyan Krishnan, Sravanth Kurmala, Mukunda NS
- 식별자: `arxiv:2606.22417`

## 요약·초록

Coding agents now interleave LLMs with retrieval over the working repository, and retrieval implementations vary widely across deployed harnesses. Inside a fixed coding-agent harness on a fixed model, does adding a structural codebase index actually change cost or resolve? We ran three arms (the harness with the index, the same harness without it, and an agentic-grep comparator) on SWE-PolyBench Verified and SWE-bench Pro with Claude Opus 4.7 held fixed throughout, across three seeds, inside a leak-audited per-task sandbox. The within-harness ablation produces a large localization gain and a statistically separated resolve gain, with no cost penalty per cell and lower cost per solve. The cross-harness check shows that the index does not regress against an agentic-grep baseline on resolve or localization, again at no cost penalty. We release the per-cell exclusion ledger, the leak-audit script, the localization extractor, and the results database. The deployment question for a structural codebase index is thus not whether it is too expensive to run (across seeds, the index lands at a lower $/solved than agentic grep) but whether the workload includes multi-file changes where structural ranking pays off.

## 내 메모


