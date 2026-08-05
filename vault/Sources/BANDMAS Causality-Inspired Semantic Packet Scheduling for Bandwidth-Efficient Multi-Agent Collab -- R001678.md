---
type: research-source
item_id: 1678
title: "BANDMAS: Causality-Inspired Semantic Packet Scheduling for Bandwidth-Efficient Multi-Agent Collaboration"
source: "arxiv"
published: "2026-08-01T05:51:51Z"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "arxiv:2608.00458"
url: "https://arxiv.org/abs/2608.00458v1"
generated_by: codex-research-db
aliases:
  - "BANDMAS: Causality-Inspired Semantic Packet Scheduling for Bandwidth-Efficient Multi-Agent Collaboration"
topics:
  - "ai-agents"
---

# BANDMAS: Causality-Inspired Semantic Packet Scheduling for Bandwidth-Efficient Multi-Agent Collaboration

[원문 열기](https://arxiv.org/abs/2608.00458v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`94TSGTSQ`)
- 발행일: 2026-08-01T05:51:51Z
- 저자: Jiangwen Dong, Wanyu Lin
- 식별자: `arxiv:2608.00458`

## 요약·초록

LLM-based multi-agent systems make decisions based on the aggregated information via exchanging messages across specialized agents. Forwarding every generated message among agents increases application-layer traffic. Yet, it introduces tremendous input tokens for agent processing, potentially raising inference latency and computational overhead. Existing approaches attempt to address the above issues by pruning agents or discarding redundant messages. Nevertheless, such agent-level or message-level optimization results in insufficient evidence supporting for final decisions or still containing redundant message transmissions. To address these challenges, we propose BANDMAS, a multi-agent collaboration framework that models inter-agent communications as task-oriented traffic, which enables efficient transmission via causality-inspired replay valuation. Specifically, we decompose messages into several data packets by analyzing their semantic features such as evidence and requests. The system only transmits these packets if their predicted replay-derived contribution exceeds their resource cost. Consequently, BANDMAS is able to adaptively schedule communication packets while adhering to bandwidth, latency, deadline, and receiver context constraints. On frozen Qwen3-4B traffic across SciFact, HotpotQA, and FanOutQA, our framework reduces application-layer bytes by 53.2\% to 77.3\% at selected caps and attains the highest mean task metric among constrained methods on all three workloads.

## 내 메모


