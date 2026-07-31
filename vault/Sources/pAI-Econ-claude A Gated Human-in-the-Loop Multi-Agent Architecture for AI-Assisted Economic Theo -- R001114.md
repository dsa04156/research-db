---
type: research-source
item_id: 1114
title: "pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development"
source: "arxiv"
published: "2026-07-23T12:40:47Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.21268"
url: "https://arxiv.org/abs/2607.21268v1"
generated_by: codex-research-db
aliases:
  - "pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development"
topics:
  - "ai-agents"
---

# pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development

[원문 열기](https://arxiv.org/abs/2607.21268v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`GTNPGKZD`)
- 발행일: 2026-07-23T12:40:47Z
- 저자: Chen Zhu, Xiaolu Wang, Weilong Zhang
- 식별자: `arxiv:2607.21268`

## 요약·초록

In many social-science research tasks, such as economics, LLM-based agents must produce outputs for which no cheap, task-complete, machine-readable correctness signal exists. This creates a distinctive reliability problem for multi-agent systems: how should generation, critique, coordination, and human judgment be organized when no component can certify the final result? We address this problem through pAI-Econ-claude, a gated, human-in-the-loop multi-agent architecture for AI-assisted economic theory development. Agents coordinate through a shared workspace of inspectable intermediate records; specialized gates diagnose targeted failure modes and recommend loopbacks without certifying correctness; and human checkpoints retain authority over decisions that are costly to reverse. We evaluate the architecture on five matched economic-theory tasks against an ungated baseline. Two evaluators blinded to configuration agreed on all five pairwise rankings, preferring the gated architecture in four tasks and the baseline in one. Mean failure severity fell from 1.58 to 1.16, while overall usefulness rose from 2.60 to 3.10. The largest observed gain occurred when a reality check rejected a false market-structure premise and a proof review prompted revision of a false welfare claim. The negative case shows that scaffolding can also compress an economically important mechanism too aggressively. The results support a bounded claim: gated oversight improves the auditability of AI-assisted economic theory without substituting for formal verification, and the allocation of irreversible human judgment is a more informative design variable than pure agent autonomy. The workflow is publicly available at https://github.com/maxwell2732/pAI-Econ-claude.

## 내 메모


