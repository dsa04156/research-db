---
type: research-source
item_id: 2354
title: "SPECMINE: A Large-Scale Corpus of Spec-Driven Development Artifacts"
source: "arxiv"
published: "2026-08-25T22:43:30Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.25202"
url: "https://arxiv.org/abs/2608.25202v1"
generated_by: codex-research-db
aliases:
  - "SPECMINE: A Large-Scale Corpus of Spec-Driven Development Artifacts"
topics:
  - "ai-agents"
---

# SPECMINE: A Large-Scale Corpus of Spec-Driven Development Artifacts

[원문 열기](https://arxiv.org/abs/2608.25202v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-25T22:43:30Z
- 저자: Shyam Agarwal, Bogdan Vasilescu
- 식별자: `arxiv:2608.25202`

## 요약·초록

Spec-Driven Development (SDD) is a fast-emerging practice in which a structured natural-language specification, written by a developer, or (more often) drafted by an AI tool and then curated by the developer, drives an AI coding agent's implementation. A wave of tooling (GitHub Spec Kit [3], OpenSpec [4], AWS Kiro [5], and dozens of others) has appeared since 2025, yet the artifacts these tools produce have never been studied at scale. We present SPECMINE, a corpus that captures SDD in public GitHub repositories through two censuses: a broad census of spec.md/specs.md files covering most tools (470,795 files across 73,030 repositories, attributed to 17 named tools), and a Kiro census of its distinct requirements/design/tasks layout (98,574 files across 12,910 repositories). Each spec is enriched with full repository metadata, complete commit history, and parsed document structure. How a spec becomes code is itself an open question, so for 11 tools we sweep every pull request that touches a spec in their repositories with at least ten stars, capturing 5,992 such PRs across 581 repositories with their changesets. That makes the simplest workflow, spec and implementation changing together in one PR, directly observable, and a census-wide index of 2,421,323 typed references (1.28M to code files, 863k to sibling documents, 152k to PRs, 62k refs, 43k branches, 22k issues) gives a second, independent link from spec to code. SPECMINE lets the community study, for the first time, how software is specified in the age of AI agents.

## 내 메모
