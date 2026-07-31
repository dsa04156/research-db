---
type: research-source
item_id: 979
title: "Is Progressive Disclosure All You Need for Long-Context Agents?"
source: "arxiv"
published: "2026-07-20T06:35:32Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.17598"
url: "https://arxiv.org/abs/2607.17598v1"
generated_by: codex-research-db
aliases:
  - "Is Progressive Disclosure All You Need for Long-Context Agents?"
topics:
  - "self-evolving-harness"
---

# Is Progressive Disclosure All You Need for Long-Context Agents?

[원문 열기](https://arxiv.org/abs/2607.17598v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`P89T4GKP`)
- 발행일: 2026-07-20T06:35:32Z
- 저자: Yifeng He, Yinzhe Zhao, Jicheng Wang, Hao Chen
- 식별자: `arxiv:2607.17598`

## 요약·초록

Long-document question answering usually forces a choice between loading the whole document into the context window and bolting on a separate retriever. Agentic AI suggests a broader option, giving the agent the document path and letting it decide how and what to read. Agent Skills, a standard for packaging expertise into folders an agent loads on demand, supply a ready mechanism: progressive disclosure, which exposes only what a query needs, from a short description down to the specific passages. Practitioners rapidly adopted this pattern for book-length understanding tasks, but the evidence to support such choices has been anecdotal. We run the first controlled study of the pattern, comparing raw-document navigation and several designs of Agent Skills packs against a classical hybrid retriever across three agent harnesses and three model families on InfiniteBench. On a single book, the gain depends on the harness, running large when the agent navigates the raw document poorly but near zero when a strong agent harness already divides and retrieves on its own. When scaling up to tasks that span many books, raw-document navigation collapses while one-level progressive disclosure degrades more slowly and pulls ahead. A second, deeper routing level never helps and sometimes breaks accuracy outright, so one level is enough. Progressive disclosure buys context, not intelligence: it is redundant while a strong agent can locate the right passages itself, and decisive once the corpus grows too large to navigate by reading.

## 내 메모


