---
type: research-source
item_id: 798
title: "Object as a Service: Simplifying Cloud-Native Development through Serverless Object Abstraction"
source: "arxiv"
published: "2024-08-09T06:55:00Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2408.04898"
url: "https://arxiv.org/abs/2408.04898v2"
generated_by: codex-research-db
aliases:
  - "Object as a Service: Simplifying Cloud-Native Development through Serverless Object Abstraction"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Object as a Service: Simplifying Cloud-Native Development through Serverless Object Abstraction

[원문 열기](https://arxiv.org/abs/2408.04898v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`MKHGTVFD`)
- 발행일: 2024-08-09T06:55:00Z
- 저자: Pawissanutt Lertpongrujikorn, Mohsen Amini Salehi
- 식별자: `arxiv:2408.04898`

## 요약·초록

The function-as-a-service (FaaS) paradigm is envisioned as the next generation of cloud computing systems that mitigate the burden for cloud-native application developers by abstracting them from cloud resource management. However, it does not deal with the application data aspects. As such, developers have to intervene and undergo the burden of managing the application data, often via separate cloud storage services. To further streamline cloud-native application development, in this work, we propose a new paradigm, known as Object as a Service (OaaS) that encapsulates application data and functions into the cloud object abstraction. OaaS relieves developers from resource and data management burden while offering built-in optimization features. Inspired by OOP, OaaS incorporates access modifiers and inheritance into the serverless paradigm that: (a) prevents developers from compromising the system via accidentally accessing underlying data; and (b) enables software reuse in cloud-native application development. Furthermore, OaaS natively supports dataflow semantics. It enables developers to define function workflows while transparently handling data navigation, synchronization, and parallelism issues. To establish the OaaS paradigm, we develop a platform named Oparaca that offers state abstraction for structured and unstructured data with consistency and fault-tolerant guarantees. We evaluated Oparaca under real-world settings against state-of-the-art platforms with respect to the imposed overhead, scalability, and ease of use. The results demonstrate that the object abstraction provided by OaaS can streamline flexible and scalable cloud-native application development with an insignificant overhead on the underlying serverless system.

## 내 메모


