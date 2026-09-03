---
type: research-source
item_id: 2456
title: "Understanding Stage-Wise Utility-Risk Trade-offs in LLM Agent Memory"
source: "arxiv"
published: "2026-08-31T02:57:08Z"
first_seen: "2026-09-01"
review_status: "pending"
canonical_key: "arxiv:2608.30177"
url: "https://arxiv.org/abs/2608.30177v1"
generated_by: codex-research-db
aliases:
  - "Understanding Stage-Wise Utility-Risk Trade-offs in LLM Agent Memory"
topics:
  - "ai-agents"
---

# Understanding Stage-Wise Utility-Risk Trade-offs in LLM Agent Memory

[원문 열기](https://arxiv.org/abs/2608.30177v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-09-01|2026-09-01]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MU7JWTHW`)
- 발행일: 2026-08-31T02:57:08Z
- 저자: Chuanchao Zang, Zijian Cao, Xiangtao Meng, Jianing Wang, Wenyu Chen, Xinyu Gao, Li Wang, Zheng Li, Shanqing Guo
- 식별자: `arxiv:2608.30177`

## 요약·초록

Long-term memory is becoming a core capability of LLM agents, enabling personalization and long-horizon interaction. However, memory mechanisms that retain, transform, or expose more information can affect both benign utility and susceptibility to memory poisoning. Existing evaluations typically measure memory utility or attack risk in isolation under fixed configurations, providing limited insight into how stage-specific design choices reshape their trade-off. We present \textsc{MemGauge}, a controllable framework that separately varies writing admission, management policy, and retrieval exposure under matched clean and poisoned conditions. Across 11 LLMs and two long-term memory benchmarks, controlled evaluations reveal three distinct profiles: a threshold-like risk transition during writing, policy-dependent local decoupling during management, and coupled growth of utility and risk during retrieval. We further apply analogous stage-level measurements to four existing memory systems and observe diagnostic associations qualitatively consistent with these profiles. These results show that targeted poisoning risk varies across memory operations and motivate stage-aware evaluation and control of LLM-agent memory.

## 내 메모


