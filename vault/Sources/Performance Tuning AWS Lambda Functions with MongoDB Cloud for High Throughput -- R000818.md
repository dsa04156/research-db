---
type: research-source
item_id: 818
title: "Performance Tuning AWS Lambda Functions with MongoDB Cloud for High Throughput"
source: "openalex"
published: "2025-07-22"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.47363/jaicc/2025(4)454"
url: "https://doi.org/10.47363/jaicc/2025(4)454"
generated_by: codex-research-db
aliases:
  - "Performance Tuning AWS Lambda Functions with MongoDB Cloud for High Throughput"
topics:
  - "cloud-infrastructure"
---

# Performance Tuning AWS Lambda Functions with MongoDB Cloud for High Throughput

[원문 열기](https://doi.org/10.47363/jaicc/2025(4)454)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`IZ4CNTMS`)
- 발행일: 2025-07-22
- 저자: Sasikanth Mamidi
- 식별자: `doi:10.47363/jaicc/2025(4)454`

## 요약·초록

Serverless computing has revolutionized modern software architectures by offering scalability, agility, and cost-efficiency. AWS Lambda, in particular, enables developers to execute code without provisioning or managing servers, while MongoDB Atlas offers a fully managed NoSQL database service in the cloud. However, realizing high throughput from such architectures requires deliberate tuning. This paper presents a comprehensive analysis of performance optimization strategies specifically tailored for AWS Lambda functions interfacing with MongoDB Cloud. By identifying typical performance bottlenecks such as cold starts, connection limitations, and VPC overheads, we demonstrate practical solutions including provisioned concurrency, persistent connections via Lambda layers, and usage of VPC endpoints. The methodology focuses on balancing execution time, latency, and cost-effectiveness, ensuring the infrastructure supports both burst and steady-state loads. Our real-world case study from the fuel retail industry validates the success of these tuning strategies through metrics such as request latency, transaction per second (TPS), and connection stability. Furthermore, we investigate the synergy between event-driven triggers like Amazon SQS and data-intensive operations in MongoDB to achieve sustained throughput at scale. The findings from this research can guide engineers and architects in building robust, responsive, and scalable serverless applications using AWS and MongoDB Cloud, ultimately aligning business outcomes with technical performance.

## 내 메모


