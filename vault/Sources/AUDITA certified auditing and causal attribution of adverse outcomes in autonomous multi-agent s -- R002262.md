---
type: research-source
item_id: 2262
title: "AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems"
source: "arxiv"
published: "2026-08-23T01:22:09Z"
first_seen: "2026-08-25"
review_status: "pending"
canonical_key: "arxiv:2608.22160"
url: "https://arxiv.org/abs/2608.22160v1"
generated_by: codex-research-db
aliases:
  - "AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems"
topics:
  - "ai-agents"
---

# AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems

[원문 열기](https://arxiv.org/abs/2608.22160v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-25|2026-08-25]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`8GTQBNQ7`)
- 발행일: 2026-08-23T01:22:09Z
- 저자: Zhixu Du, Yiran Chen
- 식별자: `arxiv:2608.22160`

## 요약·초록

Physical automation is scaling toward fleets of embodied machines commanded by an AI brain. Early deployments already run factories and warehouses at production rates beyond any human line, and their adoption is accelerating. But when their joint decisions cause harm, everyone involved has reason to blame everyone else, the machine vendor, the algorithm provider, the factory operator, the insurer, and the regulator, and no method can divide the responsibility between them. Existing methods read logs whose origin they cannot verify and name a single culprit, misrepresenting outcomes that are overdetermined, preempted, or caused by an omission. We present \audita{}, an audit layer pairing a tamper-evident record of every inter-agent command with a certified, graded causal-attribution engine. We prove its verdict cannot be gamed: a rule-following agent can never be made to look guilty, an attempt to shift blame is itself caught and graded, and we establish the exact limit of what an evidence-based auditor can certify. On live language-model pipelines it reduces the standard judge baseline's responsibility error roughly threefold; on a benchmark of accident-grounded structures it recovers responsibility where single-culprit baselines fail, and stays invariant under forgery. \audita{} turns the question of who is to blame from an argument about logs into a calculation over evidence.

## 내 메모


