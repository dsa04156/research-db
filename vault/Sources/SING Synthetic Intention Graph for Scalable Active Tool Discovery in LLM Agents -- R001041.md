---
type: research-source
item_id: 1041
title: "SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents"
source: "arxiv"
published: "2026-06-15T11:37:37Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.16591"
url: "https://arxiv.org/abs/2606.16591v2"
generated_by: codex-research-db
aliases:
  - "SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents"
topics:
  - "self-evolving-harness"
---

# SING: Synthetic Intention Graph for Scalable Active Tool Discovery in LLM Agents

[원문 열기](https://arxiv.org/abs/2606.16591v2)

## 연결

- 주제: [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GAVMGKPK`)
- 발행일: 2026-06-15T11:37:37Z
- 저자: Qiao Xiao, Haochen Shi, Yisen Gao, Wenbin Hu, Huihao Jing, Tianshi Zheng, Baixuan Xu, Ziheng Zhang, Weiqi Wang, Haoran Li, Jiaxin Bai, Yangqiu Song
- 식별자: `arxiv:2606.16591`

## 요약·초록

Large language model (LLM) agents increasingly rely on agent harnesses that manage context, tools, and multi-turn execution, making tools a central interface for acting in realistic digital environments. As harness-connected tool ecosystems expand to hundreds or thousands of APIs, services, and task-specific skills, exhaustive tool schema injection becomes costly and imposes a closed-world assumption that limits agents to a predefined static inventory. Retrieval-augmented tool selection offers a natural alternative, but existing one-shot retrieval methods often fail to align isolated tool descriptions with the agent's true task intention, especially in long-horizon tasks where required capabilities emerge through decomposition, observations, and newly induced subgoals. We propose SING, an intention-aware active tool discovery framework that builds an intention-tool graph linking user intentions, tool capabilities, and tool collaboration patterns, and dynamically retrieves tools according to evolving task states. Using a unified corpus of 7,471 tools, we evaluate SING on three real-world tool-use benchmarks. SING improves Global Recall@5 by up to 59.8% and downstream success rate by up to 28.9% over baselines, while reducing full-corpus tool-schema exposure by 99.8%, demonstrating that intention-aware graph structure enables more accurate and context-efficient tool discovery in large-scale agentic ecosystems.

## 내 메모


