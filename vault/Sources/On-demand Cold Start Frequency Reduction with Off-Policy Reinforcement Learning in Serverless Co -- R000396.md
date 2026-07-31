---
type: research-source
item_id: 396
title: "On-demand Cold Start Frequency Reduction with Off-Policy Reinforcement Learning in Serverless Computing"
source: "arxiv"
published: "2023-08-15T03:01:41Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2308.07541"
url: "https://arxiv.org/abs/2308.07541v2"
generated_by: codex-research-db
aliases:
  - "On-demand Cold Start Frequency Reduction with Off-Policy Reinforcement Learning in Serverless Computing"
topics:
  - "cloud-infrastructure"
---

# On-demand Cold Start Frequency Reduction with Off-Policy Reinforcement Learning in Serverless Computing

[원문 열기](https://arxiv.org/abs/2308.07541v2)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`WPT2K3J2`)
- 발행일: 2023-08-15T03:01:41Z
- 저자: Siddharth Agarwal, Maria A. Rodriguez, Rajkumar Buyya
- 식별자: `arxiv:2308.07541`

## 요약·초록

Function-as-a-Service (FaaS) is a cloud computing paradigm offering an event-driven execution model to applications. It features serverless attributes by eliminating resource management responsibilities from developers, and offers transparent and on-demand scalability of applications. To provide seamless on-demand scalability, new function instances are prepared to serve the incoming workload in the absence or unavailability of function instances. However, FaaS platforms are known to suffer from cold starts, where this function provisioning process introduces a non-negligible delay in function response and reduces the end-user experience. Therefore, the presented work focuses on reducing the frequent, on-demand cold starts on the platform by using Reinforcement Learning(RL). The proposed approach uses model-free Q-learning that consider function metrics such as CPU utilization, existing function instances, and response failure rate, to proactively initialize functions, in advance, based on the expected demand. The proposed solution is implemented on Kubeless and evaluated using an open-source function invocation trace applied to a matrix multiplication function. The evaluation results demonstrate a favourable performance of the RL-based agent when compared to Kubeless' default policy and a function keep-alive policy by improving throughput by up to 8.81% and reducing computation load and resource wastage by up to 55% and 37%, respectively, that is a direct outcome of reduced cold starts.

## 내 메모


