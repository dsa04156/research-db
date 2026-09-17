---
type: research-source
item_id: 2832
title: "Decomposition Buys Integrity, Not Yield"
source: "arxiv"
published: "2026-09-15T17:04:09Z"
first_seen: "2026-09-17"
review_status: "pending"
canonical_key: "arxiv:2609.17464"
url: "https://arxiv.org/abs/2609.17464v1"
generated_by: codex-research-db
aliases:
  - "Decomposition Buys Integrity, Not Yield"
topics:
  - "ai-agents"
---

# Decomposition Buys Integrity, Not Yield

[원문 열기](https://arxiv.org/abs/2609.17464v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-17|2026-09-17]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- 발행일: 2026-09-15T17:04:09Z
- 저자: Rong He
- 식별자: `arxiv:2609.17464`

## 요약·초록

Multi-agent systems split a task across a tree of agents and justify the split with folklore: smaller contexts, cleaner separation, parallelism. We ask what the split does to how much of what the leaves discover reaches the root. Model a decomposition as a tree in which an agent handed $b$ items keeps any one with probability $r(b)$. If $r(b)=1/b$, every tree delivers exactly one finding, for every task size and every shape; we verify this to $2.4 \times 10^{-15}$ on 20,000 random irregular trees. If $r(b)=Cb^{-δ}$, a depth-$k$ tree over $N$ findings yields $C^k N^{1-δ}$: task size and architecture separate, and architecture contributes only $C \le 1$ per level, so flat is optimal for yield and no arrangement of agents escapes the exponent $δ$. On 600 production deep-research traces $δ= 0.34$ [0.30, 0.38], by three identifications that do not share a failure mode. At a hop where item boundaries come from the tool rather than a text heuristic, and where $b=1$ occurs 550 times, $C = 0.571$ [0.527, 0.615] is observed rather than extrapolated, over 16,082 hops. A tier also costs alignment: on 1,012 annotated multi-agent traces one brief in sixteen goes off-target, giving $μ= 0.939$ and a per-tier penalty $Cμ= 0.536$. Depth is bought on two other axes. The root context is the only state that persists and the only one that cannot cheaply forget, and depth cuts its exposure from $N$ items to $N^{1/k}$. Depth is also cheaper: production flat agents bill as $N^{1.39}$, not the $N^2$ an append-only context predicts, and at equal spend two tiers overtake flat at 403 findings. Across every parameter we measured the model says 0.7% to 11.3% of production sessions are worth delegating, against 7.8% that do. A hazard model on 743,819 production tool calls finds that delegation does not respond to a filling context and is instead an opening move.

## 내 메모
