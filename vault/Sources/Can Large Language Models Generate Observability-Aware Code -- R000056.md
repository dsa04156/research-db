---
type: research-source
item_id: 56
title: "Can Large Language Models Generate Observability-Aware Code?"
source: "arxiv"
published: "2026-07-07T03:20:52Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.05785"
url: "https://arxiv.org/abs/2607.05785v1"
generated_by: codex-research-db
aliases:
  - "Can Large Language Models Generate Observability-Aware Code?"
topics:
  - "kubernetes"
---

# Can Large Language Models Generate Observability-Aware Code?

[원문 열기](https://arxiv.org/abs/2607.05785v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`77CIT7EB`)
- 발행일: 2026-07-07T03:20:52Z
- 저자: Yongliang Tao, Hongyu Zhang, Pengfei Gao, Minghua Ma, Zhiyu Fan, Yu Kang, Jue Zhang, Si Qin, Liqun Li, Qingwei Lin, Saravan Rajmohan
- 식별자: `arxiv:2607.05785`

## 요약·초록

Recent advances in coding agents have enabled the generation of increasingly complex software systems. While existing evaluations primarily focus on functional correctness, production systems must expose failure evidence to support observability. In this paper, we present a systematic study of observability in agent-generated systems. We examine whether agents can reconstruct source-level diagnostic semantics by restoring observability artifacts in 10 open-source and 8 industrial repositories. We also evaluate whether these artifacts translate into effective fault signals at runtime through 200 generated microservice systems deployed on Kubernetes with 13 injected faults. Our results reveal a consistent gap between diagnostic semantics at the source level and fault signals (i.e., explicit, fault-specific evidence) at runtime. At the source level, agents partially recover observability artifacts but struggle to capture key diagnostic semantics. At runtime, generated systems expose fault signals for only a small fraction of failures (up to 13.99\%), despite the presence of logging, suggesting that the generated observability artifacts may lack the failure-specific semantics needed to effectively expose faults. We further introduce an observability-oriented skill, which can serve as a guidance to improve both diagnostic semantics and fault-signal exposure, but the gains remain limited, indicating that the gap is not easily addressed. More broadly, our findings suggest that current evaluations focusing primarily on functional correctness may overlook observability as an important dimension of practical software quality.

## 내 메모


