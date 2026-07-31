---
type: research-source
item_id: 633
title: "Byzantine-Robust Decentralized Coordination of LLM Agents"
source: "arxiv"
published: "2025-07-20T11:55:26Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2507.14928"
url: "https://arxiv.org/abs/2507.14928v1"
generated_by: codex-research-db
aliases:
  - "Byzantine-Robust Decentralized Coordination of LLM Agents"
topics:
  - "ai-agents"
---

# Byzantine-Robust Decentralized Coordination of LLM Agents

[원문 열기](https://arxiv.org/abs/2507.14928v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`RM6Q58UW`)
- 발행일: 2025-07-20T11:55:26Z
- 저자: Yongrae Jo, Chanik Park
- 식별자: `arxiv:2507.14928`

## 요약·초록

Collaboration among multiple large language model (LLM) agents is a promising approach to overcome inherent limitations of single-agent systems, such as hallucinations and single points of failure. As LLM agents are increasingly deployed on open blockchain platforms, multi-agent systems capable of tolerating malicious (Byzantine) agents have become essential. Recent Byzantine-robust multi-agent systems typically rely on leader-driven coordination, which suffers from two major drawbacks. First, they are inherently vulnerable to targeted attacks against the leader. If consecutive leaders behave maliciously, the system repeatedly fails to achieve consensus, forcing new consensus rounds, which is particularly costly given the high latency of LLM invocations. Second, an underperforming proposal from the leader can be accepted as the final answer even when higher-quality alternatives are available, as existing methods finalize the leader's proposal once it receives a quorum of votes. To address these issues, we propose DecentLLMs, a novel decentralized consensus approach for multi-agent LLM systems, where worker agents generate answers concurrently and evaluator agents independently score and rank these answers to select the best available one. This decentralized architecture enables faster consensus despite the presence of Byzantine agents and consistently selects higher-quality answers through Byzantine-robust aggregation techniques. Experimental results demonstrate that DecentLLMs effectively tolerates Byzantine agents and significantly improves the quality of selected answers.

## 내 메모


