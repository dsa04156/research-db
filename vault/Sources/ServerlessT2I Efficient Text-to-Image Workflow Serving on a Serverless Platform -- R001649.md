---
type: research-source
item_id: 1649
title: "ServerlessT2I: Efficient Text-to-Image Workflow Serving on a Serverless Platform"
source: "openalex"
published: "2026-07-29"
first_seen: "2026-08-03"
review_status: "pending"
canonical_key: "arxiv:2607.26566"
url: "https://arxiv.org/abs/2607.26566"
generated_by: codex-research-db
aliases:
  - "ServerlessT2I: Efficient Text-to-Image Workflow Serving on a Serverless Platform"
topics:
  - "cloud-infrastructure"
---

# ServerlessT2I: Efficient Text-to-Image Workflow Serving on a Serverless Platform

[원문 열기](https://arxiv.org/abs/2607.26566)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-08-03|2026-08-03]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`8488AE63`)
- 발행일: 2026-07-29
- 저자: Xiaoxiao Jiang, Suyi Li, Sheng Yao, Tianyu Feng, Lingyun Yang, D.X. Nie, Haoran Yang, Wei Wang
- 식별자: `arxiv:2607.26566`

## 요약·초록

Text-to-image (T2I) workflows are increasingly deployed on serverless platforms because users often compose customized workflows and invoke them intermittently. Existing platforms typically deploy each workflow as an opaque GPU function, provisioning, placing, and scaling all constituent models in the workflow together. This monolithic design obscures workflow structure, inflates scaling overhead, forces users to manage low-level GPU coordination, and limits fine-grained fairness in multi-tenant clusters. In this paper, we present ServerlessT2I, a serverless-native system that decomposes a T2I workflow into loosely coupled model functions that can be independently managed and scheduled. By explicitly managing individual model execution, ServerlessT2I enables per-model scaling, declarative workflow composition, transparent GPU-resident communication, and fairness-aware scheduling. To make this decomposition efficient, ServerlessT2I harvests slack GPU memory left idle by compute-bound T2I inference to build a data plane that reduces model loading and data communication overheads. \sys{} further introduces a fair scheduler for multi-tenant serving. Using production traces, ServerlessT2I sustains up to 2$\times$ higher request rates than existing T2I workflow serving systems with the same GPU budget; for a fixed request rate, it saves up to 3$\times$ GPU resources while satisfying service level objectives (SLOs).

## 내 메모


