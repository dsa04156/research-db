---
type: research-source
item_id: 2520
title: "Kubernetes v1.37: etcd RangeStream Cuts Memory Use on Large List Reads"
source: "rss:Kubernetes Blog"
published: "2026-09-01T18:30:00+00:00"
first_seen: "2026-09-02"
review_status: "pending"
canonical_key: "url:d4361cc5b51334262577fcd478fcf0fcb41b5f55de75ac6e43dfb0e2a680136b"
url: "https://kubernetes.io/blog/2026/09/01/kubernetes-v1-37-etcd-range-stream/"
generated_by: codex-research-db
aliases:
  - "Kubernetes v1.37: etcd RangeStream Cuts Memory Use on Large List Reads"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Kubernetes v1.37: etcd RangeStream Cuts Memory Use on Large List Reads

[원문 열기](https://kubernetes.io/blog/2026/09/01/kubernetes-v1-37-etcd-range-stream/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-09-02|2026-09-02]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- Zotero: created (`NJIFHRSQ`)
- 발행일: 2026-09-01T18:30:00+00:00
- 식별자: `url:d4361cc5b51334262577fcd478fcf0fcb41b5f55de75ac6e43dfb0e2a680136b`

## 요약·초록

I am excited to announce that etcd RangeStream is graduating to beta in Kubernetes v1.37. Paired with etcd v3.7, it reduces the memory the API server and etcd need to read a large collection, and makes peak usage more predictable. The cost of large reads The API server serves most list and watch requests from its in-memory watch cache. Populating that cache requires reading a resource's full state from etcd, at startup and on every re-initialization. For a resource with many objects, or large ones, such as Pods, that read is expensive. The API server already paginated these reads, asking etcd for a fixed number of keys at a time rather than the whole collection at once. But a page bounded by key count has no awareness of object size, so a page of large objects can still be very large. That makes memory usage hard to predict, and a bad combination of object size and concurrent reads can be enough to trigger an OOM. etcd's unary Range assembles each page in full before sending it, and the API server holds it while decoding, so the same payload sits in memory on both sides at once. Most of that cost lands on etcd, which is also where streaming helps most. Streaming reads with RangeStream etcd v3.7 adds a streaming version of that read, the RangeStream RPC. It takes the same RangeRequest as Range and returns the same result set, but instead of building the whole response up front, etcd splits it into chunks and streams them. Chunk size is tuned adaptively to the values being returned, so a collection of large objects is bounded by bytes rather than by a key count, and memory is freed as the stream progresses instead of being held until a whole page is assembled. When the feature is enabled, the API server uses RangeStream wherever it reads a whole collection out of etcd. This includes watch cache initialization, and the fallback paths where a list request cannot be served from the cache and reads etcd directly. In either case the API server decodes each chunk as it arrives and releases it before pulling the next one, so neither side ever holds the whole collection. Requirements Kubernetes v1.37 or later etcd v3.7 or later RangeStream is used when the EtcdRangeStream feature gate is enabled on the kube-apiserver, which is beta and on by default in v1.37, and etcd is v3.7 or later. The API server resolves etcd's support at startup and also falls back at runtime if a call returns Unimplemented , so an API server paired with an older etcd keeps using the paginated Range path on its own. To turn it off, disable the gate: --feature-gates=EtcdRangeStream=false Confirming RangeStream is in use The API server records streamed reads under their own operation label on its etcd metrics. A non-zero count here means RangeStream is in use: etcd_request_duration_seconds_count{operation="listStream"} If it stays at zero, the API server is still using the paginated Range path, most likely because etcd is older than v3.7. Learn more KEP-5966: etcd RangeStream RangeStream in the etcd API guide Announcing etcd v3.7 SIG etcd If you have questions or feedback, join the #sig-etcd channel on Kubernetes Slack .

## 내 메모


