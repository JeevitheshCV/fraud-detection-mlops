# Insurance Fraud Detection – MLOps Pipeline

An end-to-end MLOps project built for detecting fraudulent vehicle insurance claims using a real-world dataset. This pipeline automates data ingestion, preprocessing, training, experiment tracking, monitoring, and deployment — following production-grade machine learning operational best practices.

> Designed & implemented by [Jeevithesh CV](https://github.com/JeevitheshCV)

---

## Project Overview

![MLOps Canvas](/project_info/mlops_canvas.png)

A complete view of the problem definition, value proposition, model strategy, and deployment lifecycle for detecting insurance fraud.

---

## Project Highlights

- Fully containerized ML system with **Docker & Compose**
- Automated batch predictions with **Prefect**
- Experiment tracking with **MLflow**
- Monitoring via **Evidently**, **SHAP**, and **Grafana**
- Live FastAPI service to expose model predictions
- Designed for **cloud compatibility** (GCS + GCP VM)

---

## Motivation

Fraudulent insurance claims cause significant financial losses and reputational damage. Manual fraud detection lacks scale and objectivity.

This project builds a realistic fraud detection workflow for insurance claims using:

- A real-world dataset
- Automated data pipelines
- Model lifecycle tracking
- Explainable monitoring
- Streamlined deployment & serving

---

## Pipeline Architecture

![Project Diagram](/project_info/project_diagram.png)

> **Stages**: Data ingestion → Preprocessing → Model training → Batch prediction → Monitoring & serving

---

## Tech Stack

| Category         | Tools & Services                                |
|------------------|--------------------------------------------------|
| **Data Source**   | [Kaggle Dataset](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection) |
| **Storage**       | Google Cloud Storage (GCS), PostgreSQL          |
| **Workflow Engine** | Prefect Cloud & CLI                          |
| **Model Tracking** | MLflow (hosted on GCP VM)                      |
| **Monitoring**    | Evidently, SHAP, Streamlit, Grafana             |
| **Serving**       | FastAPI (batch API)                             |
| **Infra/DevOps**  | Docker, Makefile, `.env`, Pre-commit Hooks      |

---

## Folder Structure

<details>
<summary>Click to expand</summary>

```bash
fraud-detection-mlops/
├── src/                     # Source code
│   ├── data/                # Preprocessing logic
│   ├── model/               # Batch prediction logic
│   └── api/                 # FastAPI service
│
├── orchestration/          # Prefect flows
├── notebooks/              # EDA, feature engineering
├── monitoring/             # SHAP images, Evidently HTMLs
├── mlflow/                 # Tracking configs & docs
├── postgres/               # SQL schema, commands
├── docker/                 # Dockerfiles, compose setup
├── config/                 # Environment variables
├── .devtools/              # Pre-commit, linting
├── project_info/           # Visuals & diagrams
├── Makefile
├── requirements.txt
└── README.md
