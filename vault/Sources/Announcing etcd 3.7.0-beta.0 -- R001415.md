---
type: research-source
item_id: 1415
title: "Announcing etcd 3.7.0-beta.0"
source: "rss:Kubernetes Blog"
published: "2026-05-20T00:00:00+00:00"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "url:f4f5eac60efab428e87e0c2996e8702fffefc25f19dabf328acd05c42653595a"
url: "https://kubernetes.io/blog/2026/05/20/etcd-370-beta/"
generated_by: codex-research-db
aliases:
  - "Announcing etcd 3.7.0-beta.0"
topics:
  - "kubernetes"
  - "cloud-infrastructure"
---

# Announcing etcd 3.7.0-beta.0

[원문 열기](https://kubernetes.io/blog/2026/05/20/etcd-370-beta/)

## 연결

- 주제: [[vault/Topics/Kubernetes]], [[vault/Topics/Cloud infrastructure]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `rss:Kubernetes Blog`
- 검토 상태: `pending`
- Zotero: created (`FJM2VMRS`)
- 발행일: 2026-05-20T00:00:00+00:00
- 식별자: `url:f4f5eac60efab428e87e0c2996e8702fffefc25f19dabf328acd05c42653595a`

## 요약·초록

SIG-Etcd announces the availability of the first beta release of etcd v3.7.0 . This new version of the popular distributed database and key Kubernetes component includes the long-requested RangeStream feature, as well as a refactoring and cleanup of multiple legacy components and interfaces. v3.7 will deliver improved security, better operational reliability, and an improved experience for working with large resultsets. First, however, the project needs users to test the beta. You can find v3.7.0-beta.0 here: Source code Binaries Official container images Please try it out and report issues in the etcd repo . This beta also determines the EOL of version 3.4. RangeStream In etcd v3.6 and earlier, it is challenging to work with requests that return large resultsets. The client or requesting application is forced to wait for the full result set, leading to unpredictable latency and memory usage. The RangeStream RPC lets calling applications accept result sets in chunks, reducing latency and making buffering memory usage more predictable. Much of the work on RangeStream was done by a relatively new contributor to etcd, Jeffrey Ying , a software engineer at Google. New contributors can have a substantial impact on etcd development. "I've always been fascinated by database internals, and building RangeStream was a great opportunity to solve a bottleneck we were hitting in production with Kubernetes. It was the perfect opportunity to collaborate across projects and improve the ecosystem as a whole. Jumping into etcd as a new contributor had a bit of a learning curve, but the community is incredibly welcoming. The leads were very receptive to my ideas and helped me iterate quickly, while maintaining the project's high bar for reliability and code quality," said Jeffrey. Instructions on how to use RangeStream in gRPC calls and in etcdctl can be found in the etcd documentation. Users should try it out for their own applications. Removal of v2store The last vestiges of etcd v2store have been removed in v3.7, making this the first release that is 100% on v3store. This includes discovery , bootstrap , v2 requests , and the v2 client . Our team has also removed multiple deprecated experimental flags . All of these changes may create some breakage for users, particularly those who have not already updated to v3.6.11. We are interested in hearing about blockers encountered by users and dependent applications; please report anything you find that can't be remedied or needs better upgrade documentation. etcd v3.7.0-beta.0 also includes bbolt v1.5.0 and raft v3.7.0 . 3.4 EOL According to our community support policy , we typically maintain only the latest two minor versions, currently v3.6 and v3.5. Etcd v3.5 will be supported for 1 year after v3.7.0 final release. As mentioned in extended support for v3.4 in the etcd v3.6.0 release announcement, etcd v3.4 has been EOL since May 15, 2026. SIG-etcd may release one more security patch for that version at the end of May, if warranted by patched vulnerabilities. In any case, it will cease being updated after the end of May. Users on v3.4 should be planning to upgrade their clusters . Feedback and Future Betas Reach the etcd contributors with your feedback about v3.7.0-beta.0 in any of the following places: Github issues #SIG-etcd slack channel in Kubernetes Slack etcd-dev mailing list SIG-etcd may release additional betas of version v3.7.0 with additional refactoring, particularly of our use of protobuf libraries. Release candidates and the final release will probably happen through June, possibly into early July.

## 내 메모


