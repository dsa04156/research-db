---
type: research-source
item_id: 749
title: "Universal Data Engineering Frameworks for Cross-Platform Fraud Detection"
source: "openalex"
published: "2025-06-30"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.47363/jaicc/2025(4)468"
url: "https://doi.org/10.47363/jaicc/2025(4)468"
generated_by: codex-research-db
aliases:
  - "Universal Data Engineering Frameworks for Cross-Platform Fraud Detection"
topics:
  - "kubernetes"
---

# Universal Data Engineering Frameworks for Cross-Platform Fraud Detection

[원문 열기](https://doi.org/10.47363/jaicc/2025(4)468)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`KP2KKV7T`)
- 발행일: 2025-06-30
- 저자: USA, Ravi Kiran Alluri
- 식별자: `doi:10.47363/jaicc/2025(4)468`

## 요약·초록

Developing, deploying, and operating on various platforms, including mobile banking apps and enterprise payment gateways, fraud detection systems must rise to meet the escalating threats presented by advanced fraud vectors. As a result, building a unified fraud detection system is challenging and necessary due to the heterogeneity of data sources, infrastructure ecosystems, and compliance standards. To address these challenges, this paper presents a generalized data engineering framework that enables scalable, platform-neutral, and real-time dynamic fraud detection through modular design, metadata-driven processing, and cross-platform interoperability. The framework brings together the structure, semi-structured, and unstructured data across a variety of systems through a common ingestion layer, standardized transformation pipelines, and abstracted machine learning integration points.In this paper, we assess modern technologies and patterns used in data engineering – e.g., schema-on-read ingestion, federated data access, event-driven processing, and cloud-native orchestration – to establish a common base that enables fraud analytics across diverse stacks. It promotes the use of DataOps practices toward automated pipeline deployment, lineage tracing, and incident tracing. Furthermore, this framework not only combines real-time streaming processing (using Apache Kafka, Spark Streaming, or Flink) with historical batch processing (using Delta Lake or Apache Iceberg) for real-time fraud response, but also long-term fraud patterns. It adds interoperability through data abstraction layers, RESTful APIs, and GraphQL endpoints, making the system's backend agnostic and allowing for custom interfaces to the analytical layers.Furthermore, the proposed framework utilizes adaptive learning methods to customize fraud detection rules and adapt to localized platform activities. This flexibility enables the architecture to be adopted in various domains, including fintech, insurance, healthcare, and e-commerce, where the sharing of knowledge through federated learning is made possible. This paper also discusses cross-jurisdictional data privacy, compliance (GDPR, HIPAA, PCI DSS), and regulatory reporting concerns by incorporating metadata-based policy enforcement and secure data masking techniques into the pipeline.A prototype for the framework was deployed in three domains-banking, ridesharing, and retail-to provide proof of concept. The findings indicated gains in accuracy, the elimination of latency, and cost reduction resulting from the reuse of a pipeline and orchestration efficiency. Metrics such as fraud recall, false favourable rates, and execution throughput were calculated and compared to those of their pre-existing, siloed systems. It also reflects on some potential bottlenecks, including schema drift management, microservices dependency management, and integration overheads with vendor platforms.This paper provides a comprehensive view on establishing universal data engineering frameworks applicable for fraud detection tasks, offering insights into modular pipeline design, cloud deployment architectures, and domain-specific customizations. Through the lens of data interoperability, pipeline observability, and real-time reaction responses, the research provides an architecture roadmap for constructing enterprise-grade fraud detection environments that can adapt to modern digital infrastructures.

## 내 메모


