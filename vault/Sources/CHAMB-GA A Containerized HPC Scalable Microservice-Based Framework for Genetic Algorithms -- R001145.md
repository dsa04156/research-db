---
type: research-source
item_id: 1145
title: "CHAMB-GA: A Containerized HPC Scalable Microservice-Based Framework for Genetic Algorithms"
source: "arxiv"
published: "2026-06-25T16:07:22Z"
first_seen: "2026-07-30"
review_status: "pending"
canonical_key: "arxiv:2606.27217"
url: "https://arxiv.org/abs/2606.27217v2"
generated_by: codex-research-db
aliases:
  - "CHAMB-GA: A Containerized HPC Scalable Microservice-Based Framework for Genetic Algorithms"
topics:
  - "kubernetes"
---

# CHAMB-GA: A Containerized HPC Scalable Microservice-Based Framework for Genetic Algorithms

[원문 열기](https://arxiv.org/abs/2606.27217v2)

## 연결

- 주제: [[vault/Topics/Kubernetes]]
- 최초 수집: [[vault/Daily/2026-07-30|2026-07-30]]
- 수집 채널: `arxiv`
- 검토 상태: `pending`
- Zotero: created (`W6BDXKF8`)
- 발행일: 2026-06-25T16:07:22Z
- 저자: Felix Bonhoff, Thiemo Pesch, Andrea Benigni, Alexander Mitsos, Manuel Dahmen
- 식별자: `arxiv:2606.27217`

## 요약·초록

Metaheuristic-based global optimization with embedded, long-running simulations is a computationally expensive process. To support various stages of development and execution, a seamless transition from personal computers to distributed clusters is desired, enabling execution across all computational scales. However, existing tool chains are often characterized by rigidity and hardware-bound constraints, which impede scalability and the integration of complex simulations. Bridging this gap, we present a containerized HPC scalable microservice-based framework for genetic algorithms with embedded simulations (CHAMB-GA). The deployment of the framework scales consistently across cloud infrastructure via container orchestration and HPC clusters via batch-scheduled parallel execution. Users provide the GA operators and simulation backend separately. The framework is designed to run these components in a distributed and decoupled manner, mapped to separate hardware. This approach ensures that the fitness evaluation and genetic operations are not managed within the same process and are utilizing distinct parts of the compute infrastructure. A central message broker coordinates asynchronous manager-worker communication between microservices, thereby parallelizing evolutionary operations and fitness evaluations. We demonstrate CHAMB-GA's scalability, portability, and reproducibility, while facilitating the integration of external tools and complex simulations on benchmark and powerflow problems. The capabilities of CHAMB-GA are validated in a two-part approach: (i) a benchmark study demonstrating minimal overhead while scaling to over 3,500 CPU cores, and (ii) a dispatch optimization of High Voltage Direct Current (HVDC) lines in the German transmission grid, showing seamless migration from Kubernetes to SLURM, combined horizontal and vertical scaling, and integration of multi-stage workflows.

## 내 메모


