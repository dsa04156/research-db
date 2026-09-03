---
type: research-source
item_id: 2504
title: "mimeo: Compiling Public Expert Corpora into Agent Skills and Testing What Transfers"
source: "arxiv"
published: "2026-08-31T22:46:48Z"
first_seen: "2026-09-02"
review_status: "pending"
canonical_key: "arxiv:2609.00453"
url: "https://arxiv.org/abs/2609.00453v1"
generated_by: codex-research-db
aliases:
  - "mimeo: Compiling Public Expert Corpora into Agent Skills and Testing What Transfers"
topics:
  - "self-evolving-harness"
---

# mimeo: Compiling Public Expert Corpora into Agent Skills and Testing What Transfers

[원문 열기](https://arxiv.org/abs/2609.00453v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-02|2026-09-02]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`U8DMXUTZ`)
- 발행일: 2026-08-31T22:46:48Z
- 저자: Timothy Kassis
- 식별자: `arxiv:2609.00453`

## 요약·초록

Giving an agent a file about a named expert can supply hard-to-find material, produce a recognizable persona, or change what the agent decides. These are different claims. We test each one. mimeo is an open-source tool that finds a person's public work, checks each extracted quotation against the cached source text, and writes a file an agent can load. Eight logged builds averaged 38 model calls; the check rejects 13.2% of extracted quotations. We tested four expert files with one coding-agent harness. Knowledge access was clearest: mimeo answered all 20 obscure, quotation-heavy questions; no closed-book condition answered more than 10. Keyword search (BM25) over the same pages answered 15-17, a gap this sample cannot resolve. Grounding showed one clear benefit: personas written from model memory misstated a documented position on 1-4 of 20 answers under every grader; the plain agent and mimeo never did. Every persona was easy to spot on short open prompts, and adding task material lowered identification by 18-23 points. mimeo was no more identifiable than a from-memory profile. Judgment transfer remained unresolved because both tests hit their ceiling: every condition found 94-97% of the problems planted in engineering tasks and scored 94-100% on 16 new application scenarios. An AI-judged "sounds like the expert" score changed with the judge: two of four preferred answers based on a model's stereotype, while two found no difference on the same text. That is a caution against relying on a single AI judge. The evidence supports mimeo as a compact, inspectable reference on a person, not as a demonstrated transfer of their judgment. Toolkit and expert profiles: https://github.com/K-Dense-AI/mimeo

## 내 메모


