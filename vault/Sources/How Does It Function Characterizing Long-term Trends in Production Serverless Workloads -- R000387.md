---
type: research-source
item_id: 387
title: "How Does It Function? Characterizing Long-term Trends in Production Serverless Workloads"
source: "arxiv"
published: "2023-12-15T14:43:14Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1145/3620678.3624783"
url: "https://arxiv.org/abs/2312.10127v1"
generated_by: codex-research-db
aliases:
  - "How Does It Function? Characterizing Long-term Trends in Production Serverless Workloads"
topics:
  - "cloud-infrastructure"
---

# How Does It Function? Characterizing Long-term Trends in Production Serverless Workloads

[원문 열기](https://arxiv.org/abs/2312.10127v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KDZZ3G2X`)
- 발행일: 2023-12-15T14:43:14Z
- 저자: Artjom Joosen, Ahmed Hassan, Martin Asenov, Rajkarn Singh, Luke Darlow, Jianfeng Wang, Adam Barker
- 식별자: `doi:10.1145/3620678.3624783`

## 요약·초록

This paper releases and analyzes two new Huawei cloud serverless traces. The traces span a period of over 7 months with over 1.4 trillion function invocations combined. The first trace is derived from Huawei's internal workloads and contains detailed per-second statistics for 200 functions running across multiple Huawei cloud data centers. The second trace is a representative workload from Huawei's public FaaS platform. This trace contains per-minute arrival rates for over 5000 functions running in a single Huawei data center. We present the internals of a production FaaS platform by characterizing resource consumption, cold-start times, programming languages used, periodicity, per-second versus per-minute burstiness, correlations, and popularity. Our findings show that there is considerable diversity in how serverless functions behave: requests vary by up to 9 orders of magnitude across functions, with some functions executed over 1 billion times per day; scheduling time, execution time and cold-start distributions vary across 2 to 4 orders of magnitude and have very long tails; and function invocation counts demonstrate strong periodicity for many individual functions and on an aggregate level. Our analysis also highlights the need for further research in estimating resource reservations and time-series prediction to account for the huge diversity in how serverless functions behave. Datasets and code available at https://github.com/sir-lab/data-release

## 내 메모


