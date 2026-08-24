---
type: research-source
item_id: 2141
title: "Introducing the Red Hat OpenShift Virtualization incident must-gather"
source: "rss:Red Hat Developer Blog"
published: "2026-08-14T03:01:17+00:00"
first_seen: "2026-08-20"
review_status: "pending"
canonical_key: "url:d1df38f93390e1d604576094096848aa82aa92a7e425ee932518dcfc3033dc0c"
url: "https://developers.redhat.com/articles/2026/08/14/introducing-openshift-virtualization-incident-must-gather"
generated_by: codex-research-db
aliases:
  - "Introducing the Red Hat OpenShift Virtualization incident must-gather"
topics:
  - "ai-agents"
---

# Introducing the Red Hat OpenShift Virtualization incident must-gather

[원문 열기](https://developers.redhat.com/articles/2026/08/14/introducing-openshift-virtualization-incident-must-gather)

## 연결

- 주제: [[vault/Topics/AI agents]]
- 최초 수집: [[vault/Daily/2026-08-20|2026-08-20]]
- 수집 채널: `rss:Red Hat Developer Blog`
- 검토 상태: `pending`
- Zotero: created (`F3H5JX46`)
- 발행일: 2026-08-14T03:01:17+00:00
- 식별자: `url:d1df38f93390e1d604576094096848aa82aa92a7e425ee932518dcfc3033dc0c`

## 요약·초록

Investigating virtual machine (VM) incidents, such as Microsoft Windows kernel panics ("Blue screen of death", or BSOD for short) or I/O hangs, traditionally required running a cluster-wide must-gather combined with sosreport , which could potentially take hours to run. This approach is resource-intensive, slow to collect, and produces a large dataset that's difficult to review efficiently To address this, we have introduced a new --vm-incident mode to the kubevirt/must-gather tool. Why better incident reporting is needed The goal is to provide a collection mechanism specifically for issues that impact one, or a small subset of VMs. When a VM is failing, investigators typically need data from a specific node at a specific time. Instead of gathering cluster-wide data, and --vm-incident allows you to isolate the scope to: The specific VM involved The node where the VM was running at the incident time A defined time window around the incident What it does When invoked, the tool uses PromQL to automatically identify the node running your VM at the specified incident time. It then sets a collection window of [Incident Time - 24h, Incident Time + 2h] to capture relevant context. This mode collects a complete view of the virtualized stack, including: Host data : dmesg , time-scoped system journal and kubelet logs, hardware inventory ( dmidecode , lspci , kernel boot parameters), storage diagnostics (mountstats, diskstats, I/O/memory/CPU pressure), networking state (interfaces, bridges, VLANs, firewall rules, NetworkManager logs), NFS deep diagnostics, SR-IOV/VFIO device state, kernel tunables ( sysctl ), tuned profiles, time synchronization (chrony), and a curated kernel red-flags log that surfaces OOM kills, QEMU crashes, NFS errors, and hung tasks. VM context: VM/VMI definitions, PVC/PV/StorageClass chains, VolumeAttachments, and namespace events Live VM state : If the VM has not restarted since the incident (for example, it is still stuck on a BSOD), the tool captures live hypervisor state: virsh domain XML, block device lists, domain stats, block errors, QEMU logs, the guest serial console (containing kernel panic or BSOD output), and cgroup memory/CPU statistics for the QEMU process. If the VM has already rebooted, this data is automatically skipped since it would only reflect the new instance, not the one that experienced the incident. Pod data: Time-scoped virt-launcher and virt-handler logs (including previous container logs). Metrics: Incident-specific Prometheus metrics exported in OpenMetrics format. The archive generated includes an incident-summary.yaml file, which catalogs exactly what was collected and notes any skipped items with reasons, ensuring you know exactly what is in your data package. No day without AI Beyond human investigation, this structured, time-scoped approach to data collection is also expected to support AI-assisted root cause analysis. By providing a richer, more focused dataset, these archives offer the necessary context for AI models to more effectively correlate events and identify patterns that might be obscured in larger, less relevant data collections. From here we go You can use the new mode with the standard must-gather command: oc adm must-gather --image=quay.io/kubevirt/must-gather \ -- NS=namespace VM=myvm \ /usr/bin/gather --vm-incident \ --incident-time=2026-07-16T10:00:00Z Replace the NS , VM , and --incident-time arguments with your specific details. The --incident-time should be provided in ISO-8601 format, representing the UTC time when the issue occurred. This feature is designed to reduce the time spent on incident investigation by minimizing noise. Please try it out in your environment and provide feedback or report issues directly in the kubevirt/must-gather repository . The post Introducing the Red Hat OpenShift Virtualization incident must-gather appeared first on Red Hat Developer .

## 내 메모


