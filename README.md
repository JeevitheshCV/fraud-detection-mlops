# 🛡️ Insurance Fraud Detection – MLOps Pipeline

An end-to-end MLOps project built for detecting fraudulent insurance claims using a real-world dataset. This pipeline automates data ingestion, training, tracking, monitoring, and deployment using best practices in machine learning operations.

> Designed & implemented by [Jeevithesh CV](https://github.com/JeevitheshCV)

---

## 📸 Project Overview

![MLOps Canvas](/project_info/mlops_canvas.png)

---

## 🚀 Project Highlights

- ✅ Automated ML pipeline with **Prefect** orchestration
- ✅ Containerized deployment with **Docker & Compose**
- ✅ Model tracking using **MLflow**
- ✅ Real-time batch predictions via **FastAPI**
- ✅ Monitoring dashboards using **Evidently**, **Grafana**, and **SHAP**
- ✅ Cloud-native support for **GCP storage & VMs**

---

## 🎯 Motivation

Insurance fraud costs companies millions annually. Automating the detection process can improve scalability, reduce losses, and prioritize investigations.  
This project simulates a real-world MLOps pipeline with:

- Scheduled data flows
- Model experimentation & tracking
- Scalable inference
- Production monitoring

---

## 🧩 Pipeline Architecture

![Project Diagram](/project_info/project_diagram.png)

---

## 🧰 Tech Stack

| Component       | Tool / Service                          |
|----------------|------------------------------------------|
| Data Source     | [Kaggle Dataset](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection) |
| Data Lake       | Google Cloud Storage (GCS)              |
| Data Mart       | PostgreSQL + pgAdmin                    |
| Orchestration   | Prefect (Cloud)                         |
| Experimentation | MLflow (on GCP VM)                      |
| Serving         | FastAPI                                 |
| Monitoring      | Evidently · SHAP · Grafana              |
| Deployment      | Docker · Makefile · `.env`              |

---

## 📁 Folder Structure

<details>
<summary>Click to expand</summary>

```bash
fraud-detection-mlops/
├── src/                     # Source code
│   ├── data/                # Preprocessing scripts
│   ├── model/               # Batch inference logic
│   └── api/                 # FastAPI app
│
├── orchestration/          # Prefect flows
├── notebooks/              # EDA & feature analysis
├── monitoring/             # SHAP plots & Evidently HTMLs
├── mlflow/                 # Tracking configs
├── postgres/               # SQL schemas
├── docker/                 # Docker & Compose setup
├── config/                 # .env templates
├── .devtools/              # Linters, pre-commit
├── Makefile
├── requirements.txt
└── README.md
