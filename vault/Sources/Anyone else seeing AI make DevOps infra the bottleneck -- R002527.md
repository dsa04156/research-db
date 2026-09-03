---
type: research-source
item_id: 2527
title: "Anyone else seeing AI make DevOps/infra the bottleneck?"
source: "social:reddit"
published: "2026-09-01"
first_seen: "2026-09-02"
review_status: "pending"
canonical_key: "url:55fd4bce252eb443bf5c7cd650973dd6f0be526465a96bfee5ca8059208725d5"
url: "https://www.reddit.com/r/devops/comments/1w42bxs/anyone_else_seeing_ai_make_devopsinfra_the/"
generated_by: codex-research-db
aliases:
  - "Anyone else seeing AI make DevOps/infra the bottleneck?"
topics:
  - "kubernetes"
---

# Anyone else seeing AI make DevOps/infra the bottleneck?

> [!warning] SNS 탐색 신호
> 원문이나 1차 자료를 확인하기 전에는 근거로 인용하지 않습니다.

[원문 열기](https://www.reddit.com/r/devops/comments/1w42bxs/anyone_else_seeing_ai_make_devopsinfra_the/)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-09-02|2026-09-02]]
- 수집 채널: `social:reddit`
- 검토 상태: `pending`
- 발행일: 2026-09-01
- 식별자: `url:55fd4bce252eb443bf5c7cd650973dd6f0be526465a96bfee5ca8059208725d5`

## 요약·초록

We fortunately solved this before LLMs came into the equation where I work. We accomplished it through opinionated, self-service IaC. Everything our developers use to build infrastructure is wrapped up in a well defined interface that platform teams developed with very strict rules and design philos We're a fairly large environment, mostly EKS, and essentially 100% IaC/Terraform Seems ok. And we're already 100% Terraform/IaC I think there might be your problem. Over the past few years we've been massively shrinking our TF footprint. Our primary developer infrastructure interface is Kubernetes. Do their agents have access to accurate and sufficient context regarding your entire infrastructure? If not then the agents are likely making all the wrong assumptions for the PRs. edit:...

## 내 메모


