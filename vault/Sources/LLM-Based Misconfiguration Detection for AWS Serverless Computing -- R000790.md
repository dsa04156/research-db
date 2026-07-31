---
type: research-source
item_id: 790
title: "LLM-Based Misconfiguration Detection for AWS Serverless Computing"
source: "arxiv"
published: "2024-11-01T14:59:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2411.00642"
url: "https://arxiv.org/abs/2411.00642v1"
generated_by: codex-research-db
aliases:
  - "LLM-Based Misconfiguration Detection for AWS Serverless Computing"
topics:
  - "cloud-infrastructure"
---

# LLM-Based Misconfiguration Detection for AWS Serverless Computing

[원문 열기](https://arxiv.org/abs/2411.00642v1)

## 연결

- 주제: [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`IWD6EUEK`)
- 발행일: 2024-11-01T14:59:00Z
- 저자: Jinfeng Wen, Zhenpeng Chen, Federica Sarro, Zixi Zhu, Yi Liu, Haodi Ping, Shangguang Wang
- 식별자: `arxiv:2411.00642`

## 요약·초록

Serverless computing is an emerging cloud computing paradigm that enables developers to build applications at the function level, known as serverless applications. Amazon Web Services (AWS), the leading provider in this domain, provides the Serverless Application Model (AWS SAM), the most widely adopted configuration schema for configuring and managing serverless applications through a specified file. However, misconfigurations pose a significant challenge in serverless development. Traditional data-driven techniques may struggle with serverless applications because the complexity of serverless configurations hinders pattern recognition, and it is challenging to gather complete datasets that cover all possible configurations. Leveraging vast amounts of publicly available data during pre-training, LLMs can have the potential to assist in identifying and explaining misconfigurations in serverless applications. In this paper, we introduce SlsDetector, the first framework leveraging LLMs to detect misconfigurations in serverless applications. SlsDetector utilizes effective prompt engineering with zero-shot learning to identify configuration issues. It designs multi-dimensional constraints specifically tailored to the configuration characteristics of serverless applications and leverages the Chain of Thought technique to enhance LLMs inferences. We evaluate SlsDetector on a curated dataset of 110 configuration files. Our results show that SlsDetector, based on ChatGPT-4o, achieves a precision of 72.88%, recall of 88.18%, and F1-score of 79.75%, outperforming state-of-the-art data-driven approaches by 53.82, 17.40, and 49.72 percentage points, respectively. Furthermore, we investigate the generalization capability of SlsDetector by applying recent LLMs, including Llama 3.1 (405B) Instruct Turbo and Gemini 1.5 Pro, with results showing consistently high effectiveness across these models.

## 내 메모


