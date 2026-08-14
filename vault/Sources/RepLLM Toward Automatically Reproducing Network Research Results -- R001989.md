---
type: research-source
item_id: 1989
title: "RepLLM: Toward Automatically Reproducing Network Research Results"
source: "openalex"
published: "2026-08-11"
first_seen: "2026-08-14"
review_status: "pending"
canonical_key: "doi:10.1145/3789240.3829170"
url: "https://doi.org/10.1145/3789240.3829170"
generated_by: codex-research-db
aliases:
  - "RepLLM: Toward Automatically Reproducing Network Research Results"
topics:
  - "ai-agents"
---

# RepLLM: Toward Automatically Reproducing Network Research Results

[원문 열기](https://doi.org/10.1145/3789240.3829170)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-14|2026-08-14]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- 발행일: 2026-08-11
- 저자: Yining Jiang, Yunxin Xu, Wei Xu, Yufan Zhu, X. Shirley Liu, Tangtang He, Haiying Huang, Letian Zhu, Qingyu Song, Qiang Su, Lizhao You, Lu Tang, Wanjian Feng, Yuchao Zhang, Linghe Kong, Qiao Xiang, Jiwu Shu
- 식별자: `doi:10.1145/3789240.3829170`

## 요약·초록

Result reproduction of computer networking research is challenging as the scarcity of open-source implementations and the complexity of heterogeneous system architectures. Even though Large Language Models have demonstrated potential in code generation, existing code generation frameworks often fail to address the long-context constraints and intricate logical dependencies, which are vital in reproducing network systems from academic papers. Thus, we introduce RepLLM, an end-to-end multi-agent framework designed to automate code reproduction from paper content. RepLLM features a collaborative architecture comprising four specialized agents—Content Parsing, Architecture Design, Code Generation, and Audit & Repair, which are coordinated through Shared Memory mechanism to ensure global context consistency. With the enhancement of Structured Chain-of-Thought LLM reasoning and a sandbox-isolated static-dynamic debugging methodology, our framework effectively resolves semantic discrepancies and runtime errors, thereby improving reliable reproductions. Extensive evaluations on representative papers in top conferences demonstrate that RepLLM outperforms state-of-the-art system-level LLM frameworks in generating compile-ready and logically correct systems. Our results show that, with the aid of RepLLM, we can reproduce 95% of the original benchmarks within approximately two hours while reducing token consumption by up to 10% compared with state-of-the-art baselines.

## 내 메모


