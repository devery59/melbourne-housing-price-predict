# 🏡 Melbourne Housing Price Predict

An end-to-end MLOps project to train, track, and serve a machine learning model that predicts housing prices in Melbourne. This project includes model training, experiment tracking, model serving with FastAPI, containerization with Docker, and deployment automation using GitHub Actions.

---

## 📅 Project Overview

* Train a machine learning model to predict house prices using Melbourne housing dataset
* Track experiments using MLflow
* Serve the trained model as an API using FastAPI
* Use Docker for containerization
* Deploy using GitHub Actions and Docker Hub

---

## 🔧 Tech Stack

| Area                | Tools/Frameworks             |
| ------------------- | ---------------------------- |
| Language            | Python 3.9                   |
| ML Libraries        | scikit-learn, pandas, numpy  |
| Experiment Tracking | MLflow                       |
| Serving             | FastAPI, Uvicorn             |
| Containerization    | Docker                       |
| CI/CD               | GitHub Actions, Docker Hub   |
| Deployment          | Cloud VM or Render (example) |

---

## 📂 Project Structure

```
.
├── Dockerfile                  # Optional project-wide Dockerfile
├── README.md
├── api/
│   └── main.py                 # Placeholder for API routes
├── app/
│   ├── serve.py                # FastAPI application for prediction
│   ├── Dockerfile              # Dockerfile for the app
│   ├── requirements.txt        # Dependencies for serve.py
│   └── mlruns/                 # MLflow model artifacts
├── data/
│   └── melb_housing.csv        # Dataset
├── model/                      # Saved model files
├── mlflow.db                   # MLflow tracking DB
├── mlruns/                     # MLflow logging directory
├── notebooks/
│   └── eda.ipynb               # EDA notebook
├── pipeline/
│   ├── ingest.py
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── deploy.py               # Register model to MLflow
├── run.py                      # Orchestrates full pipeline
├── requirements.txt            # Project-wide requirements
└── .github/workflows/
    └── ci-cd.yaml              # GitHub Actions CI/CD
```

---

## 🚀 Quickstart

### 1. Train and Track the Model

```bash
python run.py
```

### 2. Serve the Model Locally

```bash
cd app
uvicorn serve:app --host 0.0.0.0 --port 8000
```

### 3. Build and Run Docker Image Locally

```bash
docker build -t melbourne-housing-predict ./app
docker run -p 8000:8000 melbourne-housing-predict
```

---

## 💪 CI/CD Pipeline (GitHub Actions)

### Trigger:

* Runs on `push` to `main` branch

### Steps:

1. Checkout repository
2. Set up Docker Buildx
3. Log in to Docker Hub using `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets
4. Build and push Docker image from `./app`

### Example Workflow (`.github/workflows/ci-cd.yaml`):

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [ "main" ]

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: ./app
          file: ./app/Dockerfile
          push: true
          tags: yourdockerhubusername/melbourne-housing-predict:latest
```

---

## 🔗 Example API Call

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"Rooms": 3, "Bathroom": 2, "Landsize": 400, "Car": 2}'
```

---

## 💡 Future Improvements

* [ ] Add `/health` endpoint
* [ ] Docker Compose for multi-service setup
* [ ] Monitoring with Prometheus + Grafana
* [ ] Model retraining pipeline
* [ ] Frontend integration (e.g. Streamlit UI)

---

## 👤 Author

**Kris**
GitHub: [@devery59](https://github.com/devery59)


