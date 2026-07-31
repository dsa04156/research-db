---
type: research-source
item_id: 1271
title: "Mono2Sls: Automated Monolith-to-Serverless Migration via Multi-Stage Pipeline with Static Analysis"
source: "arxiv"
published: "2026-04-27T14:44:07Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2604.24550"
url: "https://arxiv.org/abs/2604.24550v1"
generated_by: codex-research-db
aliases:
  - "Mono2Sls: Automated Monolith-to-Serverless Migration via Multi-Stage Pipeline with Static Analysis"
topics:
  - "cloud-infrastructure"
---

# Mono2Sls: Automated Monolith-to-Serverless Migration via Multi-Stage Pipeline with Static Analysis

[원문 열기](https://arxiv.org/abs/2604.24550v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MPIU7E2N`)
- 발행일: 2026-04-27T14:44:07Z
- 저자: Xingyan Chen, Yuxin Su, Zishan Su, Yang Yu, Zibin Zheng
- 식별자: `arxiv:2604.24550`

## 요약·초록

Cloud computing platforms offer elastic scaling, managed infrastructure, and pay-per-use pricing, but moving existing monolithic backends to them remains a difficult software engineering task. In practice, the migration requires coordinated changes to program structure, source code, infrastructure configuration, and cloud-specific design decisions, and these changes are still largely carried out by hand. In this paper, we present Mono2Sls, an automated pipeline that converts monolithic web backends into deployable AWS SAM applications. The pipeline combines lightweight static analysis of entry points, call graphs, and asynchronous behavior with four sequential tool-using LLM agents: Architect, Code Developer, SAM Engineer, and Consistency Validator. These agents communicate through explicit intermediate artifacts and consult a curated SAM knowledge base. Evaluated on six benchmark applications totaling more than 10K lines of code and 76 business endpoints, Mono2Sls achieves 100% deployment success without manual fixes. It also reaches 66.1% end-to-end correctness and 98.7% API-coverage F1, whereas the commercial baselines achieve 53.7--61.2% and 88.4%, respectively. The migrated systems show more consistent use of AWS-native authentication and asynchronous patterns, and an ablation study indicates that static-analysis-guided architecture planning contributes 23.4 percentage points to end-to-end correctness.

## 내 메모


