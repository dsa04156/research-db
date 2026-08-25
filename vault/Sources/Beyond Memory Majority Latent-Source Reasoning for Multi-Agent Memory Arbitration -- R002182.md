---
type: research-source
item_id: 2182
title: "Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration"
source: "arxiv"
published: "2026-08-20T06:50:23Z"
first_seen: "2026-08-24"
review_status: "pending"
canonical_key: "arxiv:2608.19701"
url: "https://arxiv.org/abs/2608.19701v1"
generated_by: codex-research-db
aliases:
  - "Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration"
topics:
  - "ai-agents"
---

# Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration

[원문 열기](https://arxiv.org/abs/2608.19701v1)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-24|2026-08-24]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`6ZQ6CTKS`)
- 발행일: 2026-08-20T06:50:23Z
- 저자: Chenchen Lin, Wenhao Yuan, Xuehe Wang, Edith Cheuk Han Ngai
- 식별자: `arxiv:2608.19701`

## 요약·초록

Long-term multi-agent systems continuously accumulate the memories produced by different agents. Existing memory methods typically treat retrieved memories as independent evidence and combine them through voting or weighting. However, this independence assumption often fails in multi-agent settings: memories written by different agents may inherit the same upstream source or shared bias, causing correlated evidence to be repeatedly counted and creating a false majority. We term this failure mode \textit{Memory Correlation Bias}. To address the issue, we propose the \textbf{C}orrelation-\textbf{A}ware \textbf{M}emory \textbf{A}rbitration (CAMA) framework that jointly decouples retrieved memories and recovers missing independent evidence. We model the retrieved memories as query-conditioned evidence groups and combine neural dependency inference with provenance-based symbolic priors to estimate the effective number of independent evidence sources, thereby preventing correlated memories from forming a false majority. Since critical independent evidence may be absent from the initial retrieval set, \textsc{CAMA} further learns a sequential recovery policy that actively retrieves alternative evidence or traces upstream sources before making the final decision, aiming to recover sufficient independent evidence for reliable arbitration while minimizing retrieval cost. Experiments on multiple benchmarks demonstrate the superiority of our method over the state-of-the-art baseline methods, suppressing false majorities induced by correlated memories.

## 내 메모


