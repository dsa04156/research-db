---
type: research-source
item_id: 989
title: "MemoHarness: Agent Harnesses That Learn from Experience"
source: "arxiv"
published: "2026-07-14T21:22:18Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.14159"
url: "https://arxiv.org/abs/2607.14159v1"
generated_by: codex-research-db
aliases:
  - "MemoHarness: Agent Harnesses That Learn from Experience"
topics:
  - "self-evolving-harness"
---

# MemoHarness: Agent Harnesses That Learn from Experience

[원문 열기](https://arxiv.org/abs/2607.14159v1)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MWI6DDBM`)
- 발행일: 2026-07-14T21:22:18Z
- 저자: Yue Huang, Wenjie Wang, Han Bao, Yuchen Ma, Xiaonan Luo, Yi Nian, Haomin Zhuang, Zheyuan Liu, Yue Zhao, Xiangliang Zhang
- 식별자: `arxiv:2607.14159`

## 요약·초록

An agent harness is the external control layer that turns a base LLM into an executable agent by managing context, tools, orchestration, memory, decoding, and output handling. While harness design strongly affects agent behavior, most automatic improvement methods optimize narrower artifacts such as prompts, pipelines, or workflows, and deployed agents usually reuse a single global harness for all cases. We introduce MemoHarness, an adaptive harness optimization framework that learns from its own executions. MemoHarness decomposes the harness into six editable control dimensions, stores per-case diagnoses and distilled global patterns in a dual-layer experience bank, and adapts the learned harness to each test case using retrieved experience without test-time labels, feedback, or additional search. In our evaluation across shell-agent, code-generation, and analytical-reasoning benchmarks, MemoHarness improves over the fixed harnesses we compare against and shows selective transfer to unseen suites and base models. Its additional context can also remain cost-competitive when much of the retrieved experience is cacheable. These results provide evidence that execution experience is a practical substrate for building agent harnesses that are more adaptive than a single static configuration, while leaving broader claims about statistical robustness and component attribution to future work.

## 내 메모


