# 🚀 End-to-End MLOps Pipeline for Insurance Fraud Detection

This project demonstrates a production-ready **MLOps system** for detecting vehicle insurance fraud using real-world data, built with **scalable components**, **automation**, and **monitoring**.

> Developed and maintained by [Jeevithesh CV](https://github.com/JeevitheshCV)

---

## 🔍 Why This Project?

Insurance fraud costs billions globally each year. This project focuses on building a **machine learning solution** to detect fraudulent claims **and package it with robust MLOps infrastructure** that enables:

- Automated data pipelines  
- Scalable model training & deployment  
- Versioned experiments  
- Explainable & monitored predictions  

The goal: **build a system that a data science team could deploy and maintain in the real world.**

---

## 🧠 Key Highlights

- 📥 **Kaggle-based dataset** on vehicle fraud
- 🏗️ **Modular MLOps architecture** with Prefect orchestration
- 🧪 **MLflow tracking** of all experiments
- 🔍 **Model explainability** using SHAP & Evidently
- ⚙️ **Automated Dockerized setup** with `make`
- 📈 **Monitoring dashboards** via Grafana & Streamlit
- 🧵 **End-to-end reproducibility**

---

## 🗺️ Project Pipeline Overview

```mermaid
flowchart TD
    A[Raw Data (Kaggle)] --> B[GCS Bucket]
    B --> C[Prefect Flow: Preprocessing]
    C --> D[PostgreSQL Data Mart]
    D --> E[Model Training & Validation]
    E --> F[MLflow Tracking]
    F --> G[Batch Prediction]
    G --> H[Monitoring Reports (Evidently)]
    G --> I[FastAPI Deployment]
    D --> J[Grafana DB Monitoring]
