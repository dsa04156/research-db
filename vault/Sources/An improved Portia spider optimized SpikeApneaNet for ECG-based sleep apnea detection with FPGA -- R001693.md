---
type: research-source
item_id: 1693
title: "An improved Portia spider optimized SpikeApneaNet for ECG-based sleep apnea detection with FPGA implementation"
source: "openalex"
published: "2026-08-02"
first_seen: "2026-08-04"
review_status: "pending"
canonical_key: "doi:10.1038/s41598-026-65099-y"
url: "https://doi.org/10.1038/s41598-026-65099-y"
generated_by: codex-research-db
aliases:
  - "An improved Portia spider optimized SpikeApneaNet for ECG-based sleep apnea detection with FPGA implementation"
topics:
  - "edge-computing"
---

# An improved Portia spider optimized SpikeApneaNet for ECG-based sleep apnea detection with FPGA implementation

[원문 열기](https://doi.org/10.1038/s41598-026-65099-y)

## 연결

- 주제: [[vault/Topics/Edge computing]]
- 최초 수집: [[vault/Daily/2026-08-04|2026-08-04]]
- 수집 채널: `openalex`
- 검토 상태: `pending`
- Zotero: created (`DJWBVMME`)
- 발행일: 2026-08-02
- 저자: R. Chitra, E. Priya, C. N. Savithri, R. Geetha
- 식별자: `doi:10.1038/s41598-026-65099-y`

## 요약·초록

Sleep apnea (SA) is a serious sleep disorder that is characterized by recurrent episodes of breathing cessation, resulting in oxygen desaturation, interrupted sleep and increased risk of cardiovascular diseases, including hypertension, stroke, and arrhythmia. Early detection is critical because many cases go undiagnosed and can cause long-term serious health problems. Polysomnography (PSG) is the standard clinical approach, but is expensive, complex and used exclusively in sleep laboratories. Single-lead electrocardiogram (ECG) is a practical alternative because apnea events modulate HRV and autonomic control and allow for non-invasive, scalable detection. Currently, ECG-based apnea detection can be achieved using traditional machine learning (ML) and deep learning (DL) methods. They also have several drawbacks: Handcrafted features, poor generalization across subjects and datasets, high computational complexity, and restricted applicability in real-time and wearable devices. Furthermore, most studies do not report on the hardware implementation, leaving a gap between the algorithm and its implementation. To overcome these problems, a SpikeApneaNet framework is proposed, which is fine-tuned using improved Portia spider optimization (IPSO) and implemented on a field-programmable gate array (FPGA) for real-time SA detection. The proposed model removes the handcrafted feature dependency and introduces temporal spike encoding to transform ECG signals into sparse event-driven representations. To effectively capture the spatial and temporal dependencies of ECG signals, a spike-based deep learning framework is proposed based on a sparse spiking convolutional neural network (CNN), sparse self-attention, and spike-bidirectional gated recurrent unit (BiGRU). IPSO is used to optimize key hyperparameters, improving convergence and model performance. The model is deployed with INT8 quantization and a custom HLS hardware accelerator, synthesized in Vivado 2023.1, to enable low-latency edge inference on an Xilinx Zynq-7000 XC7Z035 FPGA. The experimental results demonstrate that the proposed IPSO-SpikeApneaNet achieved an accuracy of 95.83% under subject-independent 5-fold cross-validation, indicating robust generalization across unseen subjects. In addition, cross-dataset testing of the University College Dublin Sleep Apnea Database (UCDDB) demonstrates strong generalization ability with a mean accuracy of 94.53%. Furthermore, FPGA implementation demonstrates great efficiency improvements with 16 ms latency, 62.50 FPS throughput, 0.07 J energy consumption, and 14.53 FPS/W power efficiency with lower resource utilization than unoptimized and PSO (Portia spider optimization)-based models. In conclusion, the proposed framework is capable of providing accurate, efficient and hardware-friendly real-time ECG-based SA detection for clinical and wearable applications.

## 내 메모


