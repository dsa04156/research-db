---
type: research-source
item_id: 2356
title: "SimVerity: When Does Simulated Agent Success Survive Physical Deployment?"
source: "arxiv"
published: "2026-08-25T19:00:49Z"
first_seen: "2026-08-27"
review_status: "pending"
canonical_key: "arxiv:2608.25067"
url: "https://arxiv.org/abs/2608.25067v1"
generated_by: codex-research-db
aliases:
  - "SimVerity: When Does Simulated Agent Success Survive Physical Deployment?"
topics:
  - "ai-agents"
---

# SimVerity: When Does Simulated Agent Success Survive Physical Deployment?

[원문 열기](https://arxiv.org/abs/2608.25067v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-27|2026-08-27]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`68Z8ZEW7`)
- 발행일: 2026-08-25T19:00:49Z
- 저자: Zhonghao Zhan, Yefan Zhang, Krinos Li, Hamed Haddadi
- 식별자: `arxiv:2608.25067`

## 요약·초록

Simulated evaluation is widely used to benchmark AI agents, yet how much evidence a simulated pass provides about physical deployment has not been systematically quantified. We present SimVerity, a verdict-transfer assurance framework: it replays matched scenarios on target smart home deployments and cross-validates agent execution against independently qualified physical witnesses. Our evaluation highlights that deployment success is a real-world process, not a static property in simulation: completion, reported state, observable effect, and settled outcome diverged within the same execution. Although an advanced simulator cleared all 240 light trials, a camera caught 42 sub-second failures invisible to settled-state checks. False clearance was predictable: a risk profile learned from measured trials and locked before evaluation predicted failures on a path it never physically measured, beating a property-blind baseline in all eleven held-out sessions across two cohorts. Agent auditability was also measurable: switching one agent loop's model-client/serving configuration raised its scenario-matching share from 52-88% to 100%. Finally, a second qualified simulator added no independent cross-check: it never disagreed on any overlapping case, and only physical measurement exposed their shared blind spots. SimVerity turns verdict transfer into an explicit decision: clear, abstain, or escalate before deployment.

## 내 메모


