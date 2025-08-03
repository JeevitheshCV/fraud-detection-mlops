import os

# Define the folder and file structure
structure = {
    ".github": [],
    ".devtools": [
        ".pre-commit-config.yaml",
        ".pylintrc",
        ".gitattributes"
    ],
    "docker": [
        "Dockerfile.data",
        "Dockerfile.api",
        "docker-compose.yaml"
    ],
    "notebooks": [
        "feature_eng.ipynb",
        "experiment_tracking.ipynb"
    ],
    "src/data": [
        "preprocess_data.py"
    ],
    "src/model": [
        "batch_model_predict.py"
    ],
    "src/api": [
        "server.py",
        "model.pkl"
    ],
    "orchestration": [
        "make_monitoring_ui_artifacts.py"
    ],
    "monitoring": [
        "monitoring_ui.py"
    ],
    "monitoring/evidently_reports": [
        "data_stability.html",
        "evidently_dashboard.html"
    ],
    "monitoring/shap_lime_info": [
        "all_shap_values.png",
        "beeswarm.png",
        "fraud_shap_values.png",
        "mean_shap_values.png",
        "not_fraud_shap_values.png"
    ],
    "mlflow": [
        "command.md"
    ],
    "postgres": [
        "data_schemas.sql",
        "commands.md"
    ],
    "config": [
        "sample.env"
    ],
    "": [
        "Makefile",
        "README.md",
        "requirements.txt",
        ".gitignore"
    ]
}

# Create folders and placeholder files
for folder, files in structure.items():
    if folder:
        os.makedirs(folder, exist_ok=True)
    for file in files:
        file_path = os.path.join(folder, file)
        with open(file_path, 'w') as f:
            f.write(f"# {file}" if file.endswith(".py") else "")

print("✅ Project structure created.")
