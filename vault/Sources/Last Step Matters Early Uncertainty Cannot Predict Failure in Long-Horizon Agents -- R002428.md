---
type: research-source
item_id: 2428
title: "Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents"
source: "arxiv"
published: "2026-08-30T09:43:08Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.29685"
url: "https://arxiv.org/abs/2608.29685v1"
generated_by: codex-research-db
aliases:
  - "Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents"
topics:
  - "ai-agents"
  - "self-evolving-harness"
---

# Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents

[원문 열기](https://arxiv.org/abs/2608.29685v1)

## 연결

- 주제: [[vault/Topics/AI agents]], [[vault/Topics/Self-evolving harness]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`JUANDJPE`)
- 발행일: 2026-08-30T09:43:08Z
- 저자: Zongyue Li, Chengyue Yu, Lei Zang, Chenyi Zhuang, Linjian Mo, Leilei Gan
- 식별자: `arxiv:2608.29685`

## 요약·초록

Early failure prediction is important for long-horizon agents, as it enables timely intervention and can reduce inference and tool-use costs. Uncertainty quantification, such as verbal confidence and perplexity, offers a promising approach to detecting agent failures; however, it has not been explored whether these signals retain their discriminative power during the intermediate stages of long-horizon execution. We evaluate mainstream uncertainty signals on deep-research tasks and find that verbal confidence reliably distinguishes failures at trajectory completion, achieving a mean AUROC of 0.85, whereas all evaluated signals offer limited predictive value earlier in execution, with none exceeding a mean AUROC of 0.60 at 50% trajectory progress. We identify an underlying mechanism explaining this gap: path switching, where agents frequently abandon their current search direction in-trajectory, breaking the link between early signal and final outcome. These findings challenge the assumption that intermediate uncertainty can reliably guide early intervention. They also motivate a practical recommendation for agent harnesses in deep-research settings: use final-step confidence to decide whether to restart, an approach that our experiments find more effective than in-trajectory intervention.

## 내 메모


