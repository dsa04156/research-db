---
type: research-source
item_id: 330
title: "Modern Software Development for JUNO offline software"
source: "arxiv"
published: "2023-09-25T00:13:47Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2309.13780"
url: "https://arxiv.org/abs/2309.13780v1"
generated_by: codex-research-db
aliases:
  - "Modern Software Development for JUNO offline software"
topics:
  - "kubernetes"
---

# Modern Software Development for JUNO offline software

[원문 열기](https://arxiv.org/abs/2309.13780v1)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`7V3CTI3P`)
- 발행일: 2023-09-25T00:13:47Z
- 저자: Tao Lin
- 식별자: `arxiv:2309.13780`

## 요약·초록

The Jiangmen Underground Neutrino Observatory (JUNO), under construction in South China, primarily aims to determine the neutrino mass hierarchy and to precise measure the neutrino oscillation parameters. The data-taking is expected to start in 2024 and the detector plans to run for more than 20 years. The development of the JUNO offline software (JUNOSW) started in 2012, and it is quite challenging to maintain the JUNOSW for such a long time. In the last ten years, tools such as Subversion, Trac, and CMT had been adopted for software development. However, new stringent requirements came out, such as how to reduce the building time for the whole project, how to deploy offline algorithms to an online environment, and how to improve the code quality with code review and continuous integration. To meet the further requirements of software development, modern development tools are evaluated for JUNOSW, such as Git, GitLab, CMake, Docker, and Kubernetes. This contribution will present the software development system based on these modern tools for JUNOSW and the functionalities achieved: CMake macros are developed to simplify the build instructions for users; CMake generator expressions are used to control the build flags for the online and offline environments; a tool named git-junoenv is developed to help users partially checkout and build the software; a script is used to build and deploy the software on the CVMFS server; a Docker image with CVMFS client installed is created for continuous integration; a GitLab agent is set up to manage GitLab runners in Kubernetes with all the configurations in a GitLab repository.

## 내 메모


