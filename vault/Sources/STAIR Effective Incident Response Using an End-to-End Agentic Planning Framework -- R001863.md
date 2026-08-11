---
type: research-source
item_id: 1863
title: "STAIR: Effective Incident Response Using an End-to-End Agentic Planning Framework"
source: "arxiv"
published: "2026-08-10T12:25:12Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.09524"
url: "https://arxiv.org/abs/2608.09524v1"
generated_by: codex-research-db
aliases:
  - "STAIR: Effective Incident Response Using an End-to-End Agentic Planning Framework"
topics:
  - "ai-agents"
---

# STAIR: Effective Incident Response Using an End-to-End Agentic Planning Framework

[원문 열기](https://arxiv.org/abs/2608.09524v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-08-10T12:25:12Z
- 저자: Hanlin Jiang, Jionghao Huang, Shaofei Li, Bojia Yu, Peng Jiang, Yuxin Ren, Ning Jia, Yao Guo, Ding Li
- 식별자: `arxiv:2608.09524`

## 요약·초록

Incident response planning is critical for restoring compromised software systems after cyberattacks. Common practice relies on expert-driven playbooks that encode fixed response procedures, but these static workflows struggle to adapt to evolving incident states, changing recovery objectives, and execution feedback. Recent LLM-based planners and tool-using agents improve automation, yet they remain unstable in long-horizon response because they lack a unified basis for maintaining incident state, aligning actions with the current recovery stage, and reusing historical experience. We present STAIR, an end-to-end agentic planning framework for incident response. The framework maintains the current incident as Graph-as-State, uses a Stage Router to dispatch planning to stage-specialized agents, and retrieves historical experiences to guide action selection. An Execution Harness executes actions, returns feedback to update the incident state, and validates action effects for future experience reuse. Across 100 Docker-based cyber ranges, our framework achieves a normalized defense score of 0.94 and improves over the strongest baseline by 9.5%.

## 내 메모


