# DermTriage: End-to-End Clinical Skin Cancer Triage Pipeline

> **Executive Summary**
> An enterprise-ready, two-stage cascade machine learning system for dermatological triage. The pipeline utilizes a binary gating ensemble to detect malignancy, followed by an ordinal multiclass severity model (CORAL) to stage skin lesions (AKIEC, BCC, SCC, MEL), backed by Monte Carlo Dropout uncertainty quantification and Grad-CAM++ Explainable AI (XAI).

## Architecture & Methodology

The system is designed to mimic a clinical diagnostic workflow, prioritizing recall for severe cases and flagging uncertain predictions for human review.

- **Stage 1 (Binary Gate):** A 4-model stacking ensemble (ConvNeXt, DenseNet-121, EfficientNetV2-S, ResNet-200D) distinguishing Benign vs. Malignant lesions.
- **Stage 2 (Ordinal Severity):** For malignant predictions, a 3-model ensemble utilizes CORAL (Consistent Rank Logits) to rank the severity of the cancer.
- **XAI & Uncertainty Layer:** 
  - **Grad-CAM++:** Generates localized heatmaps indicating the morphological features driving the model's prediction.
  - **MC-Dropout:** Quantifies epistemic uncertainty. High-uncertainty predictions are automatically flagged as "Require Human Review."

## Dataset & Preprocessing

- **Source:** ISIC / HAM10000 dataset.
- **Data Leakage Prevention:** Rigorous **patient-level stratification** was utilized during the Train/Val/Test split to ensure no patient data overlapped between sets.
- **Class Imbalance:** Handled via weighted soft-voting and rank averaging across the ensemble models.

## Results & Metrics

*Evaluated on a strictly held-out patient test set.*

| Stage | Metric | Score | Notes |
| :--- | :--- | :--- | :--- |
| **Stage 1 (Malignant vs Benign)** | **ROC-AUC** | `0.965` | High sensitivity maintained to prevent False Negatives. |
| **Stage 1 (Malignant vs Benign)** | **F1-Score** | `0.921` | |
| **Stage 2 (Severity Staging)** | **Cohen's Kappa** | `0.884` | Evaluated using Quadratic Weighted Kappa for ordinal classes. |
| **System Wide** | **Calibration (Brier)** | `0.042` | Highly calibrated probabilities via ensemble rank averaging. |

*(Note: Replace example scores with your actual metrics)*

## How to Run the Inference Dashboard

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/DermTriage.git
cd DermTriage
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Generate a Clinical Report:**
Run the end-to-end evaluation script on a sample patient image. This will generate a PNG dashboard including the prediction, confidence bounds, and XAI heatmaps.
```bash
python scripts/generate_clinical_report.py --image_path data/sample/patient_01.jpg
```
