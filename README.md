# 🏡 Melbourne Housing Price Prediction - MLOps Pipeline

> Predict Melbourne house prices using a production-grade MLOps pipeline.  
> End-to-end pipeline built with Prefect, MLflow, FastAPI, and GitHub Actions.

## 🔧 Features

- 📊 Data ingestion and preprocessing
- 🧠 Model training with XGBoost & MLflow tracking
- 🚀 Model deployment via FastAPI
- 🐳 Containerized with Docker
- ✅ CI/CD pipeline using GitHub Actions

## 💻 Tech Stack

- Python, Scikit-learn, XGBoost
- Prefect for pipeline orchestration
- MLflow for experiment tracking and model registry
- FastAPI for serving
- Docker, GitHub Actions for CI/CD

## ▶️ Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Launch FastAPI server
uvicorn api.main:app --reload
