---
type: research-source
item_id: 785
title: "Truffle: Efficient Data Passing for Data-Intensive Serverless Workflows in the Edge-Cloud Continuum"
source: "arxiv"
published: "2024-11-25T14:59:21Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/ucc63386.2024.00017"
url: "https://arxiv.org/abs/2411.16451v1"
generated_by: codex-research-db
aliases:
  - "Truffle: Efficient Data Passing for Data-Intensive Serverless Workflows in the Edge-Cloud Continuum"
topics:
  - "cloud-infrastructure"
---

# Truffle: Efficient Data Passing for Data-Intensive Serverless Workflows in the Edge-Cloud Continuum

[원문 열기](https://arxiv.org/abs/2411.16451v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`QT9J7N2Q`)
- 발행일: 2024-11-25T14:59:21Z
- 저자: Cynthia Marcelino, Stefan Nastic
- 식별자: `doi:10.1109/ucc63386.2024.00017`

## 요약·초록

Serverless computing promises a scalable, reliable, and cost-effective solution for running data-intensive applications and workflows in the heterogeneous and limited-resource environment of the Edge-Cloud Continuum. However, building and running data-intensive serverless workflows also brings new challenges that can significantly degrade the application performance. Cold start remains one of the main challenges that impact the total function execution time. Further, since the serverless functions are not directly addressable, Serverless workflows need to rely on external (storage) services to pass the input data to the downstream functions. Empirical evidence from our experiments shows that the cold start and the function data passing take up the most time in the function execution lifecycle. In this paper, we introduce Truffle - a novel model and architecture that enables efficient inter-function data passing in the Edge-Cloud Continuum by introducing mechanisms that separate computation and I/O, allowing serverless functions to leverage the cold starts to their advantage. Truffle introduces Smart Data Prefetch (SDP) mechanism that abstracts the retrieval of input data for the serverless functions by triggering the data retrieval from the external storage during the function's startup. Truffle's Cold Start Pass (CSP) mechanism optimizes inter-function data passing and data exchange within serverless workflows in the Edge-Cloud Continuum by hooking into the functions' scheduling lifecycle to trigger early data passing during the function's cold start. Experimental results show that by leveraging the data prefetching and cold-start data passing, Truffle reduces the IO latency impact on the total function execution time by up to 77%, improving the function execution time by up to 46% compared to the state-of-the-art data passing approaches.

## 내 메모


