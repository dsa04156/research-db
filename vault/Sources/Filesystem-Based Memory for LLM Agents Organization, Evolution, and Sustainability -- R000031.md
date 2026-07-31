---
type: research-source
item_id: 31
title: "Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability"
source: "arxiv"
published: "2026-07-29T08:59:43Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.26637"
url: "https://arxiv.org/abs/2607.26637v1"
generated_by: codex-research-db
aliases:
  - "Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability"
topics:
  - "ai-agents"
---

# Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability

[원문 열기](https://arxiv.org/abs/2607.26637v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`XAJP9VZH`)
- 발행일: 2026-07-29T08:59:43Z
- 저자: Sizhe Zhou, Sheldon Yu, Hui Wei, Junda Wu, Siru Ouyang, Yizhu Jiao, Shijia Pan, Julian McAuley, Yu Zhang, Tong Yu, Jiawei Han
- 식별자: `arxiv:2607.26637`

## 요약·초록

Deployed LLM agents increasingly keep their long-term memory as a filesystem: a directory tree of markdown files that the agent itself reads, writes, and reorganizes through generic file tools. Yet research has largely passed over this medium: prior systems design bespoke memory representations and study retrieval over them, leaving the default's two working assumptions untested: that an agent can keep a growing store organized as memories accumulate, conflict, and go stale, and that this organization pays. We present the first systematic exploration of filesystem-based memory for LLM agents. We formalize the setting as three roles around one memory filesystem: a management agent integrates and organizes incoming content, a search agent answers queries with cited sources, and an execution agent supplies task trajectories that are distilled into skills, unifying declarative memory and skills in a single store. Across long-conversation benchmarks and embodied tasks, we vary memory shape (agent-organized hierarchy, verbatim dump, chunk retrieval), stream scale, tool harness (sandboxed shell, memory-tool-style functions, varied search tooling), and the strengths of the management and search agents, tracking answer quality, cost, and store health as memory grows. What organization reliably buys is search economy: organized stores roughly halve retrieval cost where material is large. Today's agents, however, fall short of the default's promise: in our growth study, organization erodes for all but the strongest management agent, and no agent we measure converts organization itself into better answers. And the model is not the only lever over a store's shape: changing the tool set alone reshapes the store as strongly as swapping the model. The study turns the filesystem default from an assumption into a design space for agent memory.

## 내 메모


