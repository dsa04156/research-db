---
type: research-source
item_id: 3054
title: "XYEval: Agents say yes to bad advice"
source: "arxiv"
published: "2026-09-20T23:31:29Z"
first_seen: "2026-09-23"
review_status: "pending"
canonical_key: "arxiv:2609.23939"
url: "https://arxiv.org/abs/2609.23939v1"
generated_by: codex-research-db
aliases:
  - "XYEval: Agents say yes to bad advice"
topics:
  - "ai-agents"
---

# XYEval: Agents say yes to bad advice

[원문 열기](https://arxiv.org/abs/2609.23939v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-23|2026-09-23]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-20T23:31:29Z
- 저자: Zhengxuan Wu, Yuxuan Li, Oyvind Tafjord, Been Kim
- 식별자: `arxiv:2609.23939`

## 요약·초록

Effective communication between users and AI agents is essential for human-AI collaboration. The XY problem is a well-known communication pitfall where a person asks about their attempted solution rather than their actual problem. We extend prior sycophancy evaluation to the XY problem in agentic settings, evaluating whether agents can resist plausible but misleading suggestions from users and communicate their reasoning. We introduce XYEval, a meta-evaluation framework that can transform an existing benchmark into an XY problem evaluation. We evaluate five models across six diverse benchmark suites. Agents suffer large XY drops under XY mutation across benchmarks, with relative drops reaching up to 46.7%. With $τ^2$-bench, we further show that agent performance drops more when encountering a pedantic user who requires detailed explanations before approving a better solution. Our findings suggest that current agents lack the ability to effectively reason and communicate when facing misleading suggestions. A simple system instruction baseline that encourages awareness of XY problems only offers partial mitigation. Extensive trace analyses provide behavioral insights into how and why these XY drops occur across execution trajectories. Our results show that mitigating the XY problem remains challenging, requiring agents to both recognize user misdirection and clearly communicate the underlying problem.

## 내 메모
