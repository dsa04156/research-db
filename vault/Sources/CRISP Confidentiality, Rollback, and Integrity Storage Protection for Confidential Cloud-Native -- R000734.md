---
type: research-source
item_id: 734
title: "CRISP: Confidentiality, Rollback, and Integrity Storage Protection for Confidential Cloud-Native Computing"
source: "arxiv"
published: "2024-08-13T11:29:30Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1109/cloud62652.2024.00026"
url: "https://arxiv.org/abs/2408.06822v2"
generated_by: codex-research-db
aliases:
  - "CRISP: Confidentiality, Rollback, and Integrity Storage Protection for Confidential Cloud-Native Computing"
topics:
  - "kubernetes"
---

# CRISP: Confidentiality, Rollback, and Integrity Storage Protection for Confidential Cloud-Native Computing

[원문 열기](https://arxiv.org/abs/2408.06822v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`ZIMECBDR`)
- 발행일: 2024-08-13T11:29:30Z
- 저자: Ardhi Putra Pratama Hartono, Andrey Brito, Christof Fetzer
- 식별자: `doi:10.1109/cloud62652.2024.00026`

## 요약·초록

Trusted execution environments (TEEs) protect the integrity and confidentiality of running code and its associated data. Nevertheless, TEEs' integrity protection does not extend to the state saved on disk. Furthermore, modern cloud-native applications heavily rely on orchestration (e.g., through systems such as Kubernetes) and, thus, have their services frequently restarted. During restarts, attackers can revert the state of confidential services to a previous version that may aid their malicious intent. This paper presents CRISP, a rollback protection mechanism that uses an existing runtime for Intel SGX and transparently prevents rollback. Our approach can constrain the attack window to a fixed and short period or give developers the tools to avoid the vulnerability window altogether. Finally, experiments show that applying CRISP in a critical stateful cloud-native application may incur a resource increase but only a minor performance penalty.

## 내 메모


