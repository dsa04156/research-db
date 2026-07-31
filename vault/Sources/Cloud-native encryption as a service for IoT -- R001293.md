---
type: research-source
item_id: 1293
title: "Cloud-native encryption as a service for IoT"
source: "openalex"
published: "2026-07-15"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-52815-x"
url: "https://doi.org/10.1038/s41598-026-52815-x"
generated_by: codex-research-db
aliases:
  - "Cloud-native encryption as a service for IoT"
topics:
  - "kubernetes"
---

# Cloud-native encryption as a service for IoT

[원문 열기](https://doi.org/10.1038/s41598-026-52815-x)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`X2CCZX6T`)
- 발행일: 2026-07-15
- 저자: Amir Javadpour, Tarik Taleb, Chafika Benzaid, Khaled Zeraoulia, Abderezzak Djebrani, Mohamed Yacine Belhadi, Luis Cordeiro, Luís Rosa
- 식별자: `doi:10.1038/s41598-026-52815-x`

## 요약·초록

Encryption as a Service (EaaS) is a practical solution for resource-constrained Internet of Things (IoT) devices that cannot efficiently execute costly cryptographic tasks locally. This paper presents a cloud-native EaaS platform implemented on Kubernetes and designed to support scalable encryption, decryption, and key-management services for IoT environments. The paper describes the functional architecture of the platform, defines its main service workflow, and introduces two deployment modes, namely cloud-based and fog-based deployment. The proposed platform is evaluated in terms of processing time, deployment time, and end-to-end response time. The results show that the fog-based deployment reduces the response time by at least [Formula: see text] for small payloads and by up to [Formula: see text] for larger payloads compared with the cloud-based mode. The deployment analysis also shows that increasing the number of replicas from 1 to 5 leads to a deployment-time increase of more than [Formula: see text], while increasing the workload to 11 replicas results in an increase of about [Formula: see text]. In addition, the results indicate that the Key Manager is the most resource-intensive component and has the highest impact on pod readiness time. Overall, the findings show that the proposed Kubernetes-based EaaS platform can provide flexible and scalable cryptographic support for IoT systems, while fog-based placement offers clear latency advantages in the evaluated prototype setting.

## 내 메모


