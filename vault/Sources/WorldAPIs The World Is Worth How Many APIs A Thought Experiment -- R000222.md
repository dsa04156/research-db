---
type: research-source
item_id: 222
title: "WorldAPIs: The World Is Worth How Many APIs? A Thought Experiment"
source: "arxiv"
published: "2024-07-10T15:52:44Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2407.07778"
url: "https://arxiv.org/abs/2407.07778v2"
generated_by: codex-research-db
aliases:
  - "WorldAPIs: The World Is Worth How Many APIs? A Thought Experiment"
topics:
  - "ai-agents"
---

# WorldAPIs: The World Is Worth How Many APIs? A Thought Experiment

[원문 열기](https://arxiv.org/abs/2407.07778v2)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GWNG7K7N`)
- 발행일: 2024-07-10T15:52:44Z
- 저자: Jiefu Ou, Arda Uzunoglu, Benjamin Van Durme, Daniel Khashabi
- 식별자: `arxiv:2407.07778`

## 요약·초록

AI systems make decisions in physical environments through primitive actions or affordances that are accessed via API calls. While deploying AI agents in the real world involves numerous high-level actions, existing embodied simulators offer a limited set of domain-salient APIs. This naturally brings up the questions: how many primitive actions (APIs) are needed for a versatile embodied agent, and what should they look like? We explore this via a thought experiment: assuming that wikiHow tutorials cover a wide variety of human-written tasks, what is the space of APIs needed to cover these instructions? We propose a framework to iteratively induce new APIs by grounding wikiHow instruction to situated agent policies. Inspired by recent successes in large language models (LLMs) for embodied planning, we propose a few-shot prompting to steer GPT-4 to generate Pythonic programs as agent policies and bootstrap a universe of APIs by 1) reusing a seed set of APIs; and then 2) fabricate new API calls when necessary. The focus of this thought experiment is on defining these APIs rather than their executability. We apply the proposed pipeline on instructions from wikiHow tutorials. On a small fraction (0.5%) of tutorials, we induce an action space of 300+ APIs necessary for capturing the rich variety of tasks in the physical world. A detailed automatic and human analysis of the induction output reveals that the proposed pipeline enables effective reuse and creation of APIs. Moreover, a manual review revealed that existing simulators support only a small subset of the induced APIs (9 of the top 50 frequent APIs), motivating the development of action-rich embodied environments.

## 내 메모


