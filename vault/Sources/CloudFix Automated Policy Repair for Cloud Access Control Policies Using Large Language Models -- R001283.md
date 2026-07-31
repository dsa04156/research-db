---
type: research-source
item_id: 1283
title: "CloudFix: Automated Policy Repair for Cloud Access Control Policies Using Large Language Models"
source: "arxiv"
published: "2025-12-09T21:22:16Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2512.09957"
url: "https://arxiv.org/abs/2512.09957v2"
generated_by: codex-research-db
aliases:
  - "CloudFix: Automated Policy Repair for Cloud Access Control Policies Using Large Language Models"
topics:
  - "cloud-infrastructure"
---

# CloudFix: Automated Policy Repair for Cloud Access Control Policies Using Large Language Models

[원문 열기](https://arxiv.org/abs/2512.09957v2)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`UP465CNR`)
- 발행일: 2025-12-09T21:22:16Z
- 저자: Bethel Hall, Owen Ungaro, William Eiers
- 식별자: `arxiv:2512.09957`

## 요약·초록

Access control policies are vital for securing modern cloud computing, where organizations must manage access to sensitive data across thousands of users in distributed system settings. Cloud administrators typically write and update policies manually, which can be an error-prone and time-consuming process and can potentially lead to security vulnerabilities. Existing approaches based on symbolic analysis have demonstrated success in automated debugging and repairing access control policies; however, their generalizability is limited in the context of cloud-based access control. Conversely, Large Language Models (LLMs) have been utilized for automated program repair; however, their applicability to repairing cloud access control policies remains unexplored. In this work, we introduce CloudFix, the first automated policy repair framework for cloud access control that combines formal methods with LLMs. Given an access control policy and a specification of allowed and denied access requests, CloudFix employs Formal Methods-based Fault Localization to identify faulty statements in the policy and leverages LLMs to generate potential repairs, which are then verified using SMT solvers. To evaluate CloudFix, we curated a dataset of 282 real-world AWS access control policies extracted from forum posts and augmented them with synthetically generated request sets based on real scenarios. Our experimental results show that CloudFix improves repair accuracy over a Baseline implementation across varying request sizes. Our work is the first to leverage LLMs for policy repair, showcasing the effectiveness of LLMs for access control and enabling efficient and automated repair of cloud access control policies. We make our tool Cloudfix and AWS dataset publicly available.

## 내 메모


