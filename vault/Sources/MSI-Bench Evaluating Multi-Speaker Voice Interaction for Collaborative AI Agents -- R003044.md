---
type: research-source
item_id: 3044
title: "MSI-Bench: Evaluating Multi-Speaker Voice Interaction for Collaborative AI Agents"
source: "arxiv"
published: "2026-09-21T16:04:26Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.24812"
url: "https://arxiv.org/abs/2609.24812v1"
generated_by: codex-research-db
aliases:
  - "MSI-Bench: Evaluating Multi-Speaker Voice Interaction for Collaborative AI Agents"
topics:
  - "ai-agents"
---

# MSI-Bench: Evaluating Multi-Speaker Voice Interaction for Collaborative AI Agents

[원문 열기](https://arxiv.org/abs/2609.24812v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-21T16:04:26Z
- 저자: Chenxu Xiong, Dongming Shen, Yuzhi Tang, Wentao Ma, Mu Li, Alex Smola
- 식별자: `arxiv:2609.24812`

## 요약·초록

Voice provides a natural and immediate interface for AI agents. Many settings in which voice agents could be useful, including meetings, households, and collaborative work, are inherently multi-speaker. Supporting these settings introduces challenges that are largely absent from one-on-one interaction. We introduce the Multi-Speaker Interaction Benchmark (MSI-Bench) for evaluating multi-speaker voice interaction. Each test case is a short multi-party multi-turn audio scene with participant context, expected tool calls, and atomic rubrics. The benchmark targets three capability families: multi-speaker memory, multi-speaker instruction following, and multi-speaker reasoning. It comprises 1,152 test cases, evenly split between Mandarin Chinese and English (576 each). The strongest configuration on each split passes all rubrics on only 66.8% of English and 54.5% of Mandarin cases, and the strongest open-weight configuration on 34.0% and 19.3%. Failure analysis separates perception from reasoning: open-weight models are bottlenecked by the multi-speaker audio front-end, while frontier systems still fail speaker-scoped decision making on clean transcripts---and models across the board often respond when no one has addressed them. These results identify speaker-grounded perception, speaker-scoped decision making, and conversational restraint as concrete targets for future voice agents.

## 내 메모
