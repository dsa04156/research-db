---
type: research-source
item_id: 316
title: "Analyzing and Mitigating (with LLMs) the Security Misconfigurations of Helm Charts from Artifact Hub"
source: "arxiv"
published: "2024-03-14T16:26:40Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2403.09537"
url: "https://arxiv.org/abs/2403.09537v1"
generated_by: codex-research-db
aliases:
  - "Analyzing and Mitigating (with LLMs) the Security Misconfigurations of Helm Charts from Artifact Hub"
topics:
  - "kubernetes"
---

# Analyzing and Mitigating (with LLMs) the Security Misconfigurations of Helm Charts from Artifact Hub

[원문 열기](https://arxiv.org/abs/2403.09537v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`4T4QK45Q`)
- 발행일: 2024-03-14T16:26:40Z
- 저자: Francesco Minna, Fabio Massacci, Katja Tuma
- 식별자: `arxiv:2403.09537`

## 요약·초록

Background: Helm is a package manager that allows defining, installing, and upgrading applications with Kubernetes (K8s), a popular container orchestration platform. A Helm chart is a collection of files describing all dependencies, resources, and parameters required for deploying an application within a K8s cluster. Objective: The goal of this study is to mine and empirically evaluate the security of Helm charts, comparing the performance of existing tools in terms of misconfigurations reported by policies available by default, and measure to what extent LLMs could be used for removing misconfiguration. We also want to investigate whether there are false positives in both the LLM refactorings and the tool outputs. Method: We propose a pipeline to mine Helm charts from Artifact Hub, a popular centralized repository, and analyze them using state-of-the-art open-source tools, such as Checkov and KICS. First, such a pipeline will run several chart analyzers and identify the common and unique misconfigurations reported by each tool. Secondly, it will use LLMs to suggest mitigation for each misconfiguration. Finally, the chart refactoring previously generated will be analyzed again by the same tools to see whether it satisfies the tool's policies. At the same time, we will also perform a manual analysis on a subset of charts to evaluate whether there are false positive misconfigurations from the tool's reporting and in the LLM refactoring.

## 내 메모


