---
type: research-source
item_id: 2380
title: "KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference"
source: "arxiv"
published: "2026-08-27T06:55:24Z"
first_seen: "2026-08-28"
review_status: "pending"
canonical_key: "arxiv:2608.26699"
url: "https://arxiv.org/abs/2608.26699v1"
generated_by: codex-research-db
aliases:
  - "KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference"
topics:
  - "kubernetes"
---

# KubeCap: A Framework for Capability Minimization in Kubernetes via Static Analysis and LLM-Assisted Rule Inference

[원문 열기](https://arxiv.org/abs/2608.26699v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-08-28|2026-08-28]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`3PXQRMPC`)
- 발행일: 2026-08-27T06:55:24Z
- 저자: Yuhao Liu, Yingnan Zhou, Weijie Liu, Yan Jia, Zheli Liu
- 식별자: `arxiv:2608.26699`

## 요약·초록

As the most widely used container orchestration platform, Kubernetes provides flexible privilege configuration by allowing developers to manage Linux capabilities via manifest files. However, developers rely on default settings or coarse-grained security contexts in practice, violating the principle of least privilege and enlarging the attack surface of containerized workloads. Existing studies either detect vulnerable patterns in Kubernetes manifests or infer required capabilities for standalone Linux programs, but they do not directly address capability minimization in Kubernetes. To bridge this gap, we first conduct an empirical study on three open-source datasets, revealing that 74.67% of projects lack capability configurations. Motivated by our observations, we propose KubeCap, a framework for Kubernetes capability minimization. KubeCap translates deployment specifications into deterministic manifests, locates container entrypoints, performs reachability-guided system call analysis, and leverages LLM-assisted rule specification to derive syscall--parameter--capability relations from Linux kernel code. Based on these results, KubeCap infers the minimal capability set required by each workload and automatically generates repaired manifests. Evaluation on 10 representative Go-based Kubernetes projects shows an average capability reduction rate of 54.97%, outperforming rapid type analysis and class hierarchy analysis baselines while maintaining practical analysis cost. These results demonstrate KubeCap's effectiveness in enforcing least privilege in Kubernetes.

## 내 메모


