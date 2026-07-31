---
type: research-source
item_id: 52
title: "Cold-Start Model Delivery in Kubernetes Inference Serving: An Empirical Study of OCI-Based Distribution and Its Integrity"
source: "arxiv"
published: "2026-07-18T02:31:13Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2607.16596"
url: "https://arxiv.org/abs/2607.16596v1"
generated_by: codex-research-db
aliases:
  - "Cold-Start Model Delivery in Kubernetes Inference Serving: An Empirical Study of OCI-Based Distribution and Its Integrity"
topics:
  - "kubernetes"
---

# Cold-Start Model Delivery in Kubernetes Inference Serving: An Empirical Study of OCI-Based Distribution and Its Integrity

[원문 열기](https://arxiv.org/abs/2607.16596v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ENVPMZUA`)
- 발행일: 2026-07-18T02:31:13Z
- 저자: Georgii Kliukovkin
- 식별자: `arxiv:2607.16596`

## 요약·초록

The startup latency of a model-serving pod on Kubernetes is dominated by one step: delivering the model weights. As models reach the hundred-gigabyte weights of large language models, cold-start delivery time governs the economics of autoscaling and scale-to-zero, yet the dominant mechanisms remain ad-hoc downloads from object storage, with none of the pull caching, digest addressing, or verification Kubernetes provides for container images. We analyze the delivery paths available to a Kubernetes serving platform along two axes: which component pulls the artifact, and whether any admission-time verifier can bind the deployed reference to the arriving bytes. We validate the analysis upstream in KServe, a widely deployed CNCF model-serving platform, by implementing two new delivery paths: oci+native://, which mounts model images as Kubernetes image volumes (KEP-4639), merged upstream, and oci+fetch://, which pulls OCI artifacts inside the storage initializer, under review. We report, to our knowledge, the first controlled comparison of model delivery paths in a Kubernetes serving platform (modelcar sidecars, native image volumes, object-storage download) on artifacts sized to fp16 weights of 1B-, 7B-, and 70B-class models (2-140 GB). Node-cached OCI delivery makes warm replica addition size-independent: 11.7 s for a 70B-class artifact versus 40.7 minutes of re-download over object storage, a 208x difference, while the first cold pull costs up to 2x a plain download, localized to containerd's blob-write-then-unpack double pass. For models on s3://, gs://, or hf:// URIs, where no admission-time verifier observes the bytes, we present a serving-time integrity design proposed to the KServe community: digest pinning and OpenSSF model-signing enforcement in the storage initializer. Streaming hash verification during download adds under 0.1% to delivery time; a post-download pass adds up to 53%.

## 내 메모


