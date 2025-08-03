# 🛡️ Fraud Detection with MLOps: An End-to-End Pipeline for Insurance Claims

This project implements a production-grade machine learning pipeline to detect fraudulent vehicle insurance claims. It leverages modern MLOps tools and practices such as orchestration, experiment tracking, automated monitoring, and model deployment — all containerized using Docker.

> 🚀 Designed, structured, and implemented by [Jeevithesh CV](https://github.com/JeevitheshCV)

---

## 📌 Project Highlights

- End-to-end ML pipeline for insurance fraud detection
- Modular codebase with industry-standard structure
- Orchestrated workflows using **Prefect**
- Model training tracked via **MLflow**
- Live monitoring via **Evidently** and **Grafana**
- API-based prediction using **FastAPI**
- Complete Docker-based setup for reproducibility
- Environment-managed via `.env` and `Makefile`

---

## 🎯 Motivation

Fraudulent insurance claims can cause significant financial losses. Traditional fraud detection methods are often reactive and not scalable.  
This project was built to **simulate a real-world MLOps setup** that allows:
- Continuous ingestion of data
- Scalable and automated model retraining
- Transparent performance monitoring
- Real-time batch inference and visualization

This work helped me practice not just ML, but also **software engineering**, **DevOps**, and **cloud-first ML design**.

---

## Folder Structure

fraud-detection-mlops/
│
├── src/                     # Core source code
│   ├── data/                # Preprocessing scripts
│   ├── model/               # Batch prediction logic
│   └── api/                 # FastAPI service
│
├── notebooks/              # EDA and ML experimentation
├── orchestration/          # Prefect flow scripts
├── monitoring/             # SHAP, Evidently dashboards
├── mlflow/                 # MLflow commands & setup
├── postgres/               # DB schemas & commands
├── docker/                 # Docker & compose files
├── config/                 # Environment files
├── .devtools/              # Pre-commit, linting configs
├── Makefile                # Project commands
├── requirements.txt
├── README.md
└── .gitignore


---

## 🧩 End-to-End Pipeline Diagram

graph TD
    A[Kaggle Dataset] --> B[GCS Bucket]
    B --> C[Preprocessing with Prefect]
    C --> D[PostgreSQL Database]
    D --> E[Model Training]
    E --> F[MLflow Tracking]
    F --> G[Batch Prediction]
    G --> H[Monitoring (Evidently + SHAP)]
    G --> I[Serving with FastAPI]
    D --> J[Grafana Dashboard]
    H --> K[Streamlit Monitoring UI]

