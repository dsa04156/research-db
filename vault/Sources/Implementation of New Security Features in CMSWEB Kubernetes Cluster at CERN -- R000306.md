---
type: research-source
item_id: 306
title: "Implementation of New Security Features in CMSWEB Kubernetes Cluster at CERN"
source: "arxiv"
published: "2024-05-24T08:22:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "doi:10.1051/epjconf/202429507026"
url: "https://arxiv.org/abs/2405.15342v1"
generated_by: codex-research-db
aliases:
  - "Implementation of New Security Features in CMSWEB Kubernetes Cluster at CERN"
topics:
  - "kubernetes"
---

# Implementation of New Security Features in CMSWEB Kubernetes Cluster at CERN

[원문 열기](https://arxiv.org/abs/2405.15342v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`KFCF3S54`)
- 발행일: 2024-05-24T08:22:22Z
- 저자: Aamir Ali, Muhammad Imran, Valentin Kuznetsov, Spyridon Trigazis, Aroosha Pervaiz, Andreas Pfeiffer, Marco Mascheroni
- 식별자: `doi:10.1051/epjconf/202429507026`

## 요약·초록

The CMSWEB cluster is pivotal to the activities of the Compact Muon Solenoid (CMS) experiment, as it hosts critical services required for the operational needs of the CMS experiment. The security of these services and the corresponding data is crucial to CMS. Any malicious attack can compromise the availability of our services. Therefore, it is important to construct a robust security infrastructure. In this work, we discuss new security features introduced to the CMSWEB Kubernetes ("k8s") cluster. The new features include the implementation of network policies, deployment of Open Policy Agent (OPA), enforcement of OPA policies, and the integration of Vault. The network policies act as an inside-the-cluster firewall to limit the network communication between the pods to the minimum necessary, and its dynamic nature allows us to work with microservices. The OPA validates the objects against some custom-defined policies during create, update, and delete operations to further enhance security. Without recompiling or changing the configuration of the Kubernetes API server, it can apply customized policies on Kubernetes objects and their audit functionality enabling us to detect pre-existing conflicts and issues. Although Kubernetes incorporates the concepts of secrets, they are only base64 encoded and are not dynamically configured. This is where Vault comes into play: Vault dynamically secures, stores, and tightly controls access to sensitive data. This way, the secret information is encrypted, secured, and centralized, making it more scalable and easier to manage. Thus, the implementation of these three security features corroborate the enhanced security and reliability of the CMSWEB Kubernetes infrastructure.

## 내 메모


