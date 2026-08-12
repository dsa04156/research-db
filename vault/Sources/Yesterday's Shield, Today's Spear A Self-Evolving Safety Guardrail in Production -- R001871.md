---
type: research-source
item_id: 1871
title: "Yesterday's Shield, Today's Spear: A Self-Evolving Safety Guardrail in Production"
source: "arxiv"
published: "2026-08-09T04:31:05Z"
first_seen: "2026-08-11"
review_status: "pending"
canonical_key: "arxiv:2608.08471"
url: "https://arxiv.org/abs/2608.08471v1"
generated_by: codex-research-db
aliases:
  - "Yesterday's Shield, Today's Spear: A Self-Evolving Safety Guardrail in Production"
topics:
  - "ai-agents"
---

# Yesterday's Shield, Today's Spear: A Self-Evolving Safety Guardrail in Production

[원문 열기](https://arxiv.org/abs/2608.08471v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-11|2026-08-11]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`CHRD2SXT`)
- 발행일: 2026-08-09T04:31:05Z
- 저자: Cong Ming, Jingyi Chen, Bin Liu, Qi Chu, Tao Gong, Nenghai Yu, Yingfei Xiang
- 식별자: `arxiv:2608.08471`

## 요약·초록

Deployed LLM safety guardrails are predominantly static: trained once and frozen at release, while new jailbreak techniques and previously un-addressed harmful categories emerge within days, leaving the defense perpetually a step behind. We present SESG (Self-Evolving Safety Guardrails), a multi-agent system running in production. SESG monitors the live traffic behind a deployed guardrail and surfaces two classes of failure: jailbreaks novel in form and harmful categories novel in content. Once a failure is confirmed, a generation agent synthesizes paired training data targeted at it; a validation agent rebalances the batch toward the direction in which the deployed model errs, so that the model's own mistakes steer its training set; and a routing agent matches the training action to the diagnosed gap and returns the next version to production. Over six rounds of live evolution (V0 to V6), a 1.7B guardrail adapts to a new threat in 16-24 hours, with about 2 hours of human effort, versus the 40-90 hours of the manual process it replaces. On six emerging threats, it outperforms static guardrails from 0.6B to 9B and an adaptive baseline while preserving its general screening competence. Since April 2026, SESG has been the primary update pipeline of Sangfor's guardrail, autonomously closing 14 of 15 new threat scenarios in two months. We release 9 test sets for the 6 new threats at https://github.com/Trams1017/SESG. Warning: This paper contains examples that may be harmful or offensive.

## 내 메모


