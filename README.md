# Voyage Analytics: Integrating MLOps in Travel

Using MLOps practices to build, deploy, and monitor machine learning models that solve core problems in the travel and hospitality industry. This repository contains end-to-end pipelines for flight price prediction, hotel recommendations, and gender classification, fully integrated with modern MLOps tools.

---

## 🚀 Badges & Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CE2?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📂 Project Architecture & Directory Structure

```text
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
├── flight_price_api.py
├── flight-price-deployment.yml
├── best_flight_price_model.joblib
├── flight_api.log
├── DATA/                                 # Raw and processed datasets
├── Flight price prediction/              # Code, notebooks & research for Flight Price
├── Gender classification/                # Code, notebooks & research for Gender Profiling
├── Hotel Recommendation Model/           # Code, notebooks & research for Hotel Recs
└── airflow-docker/                       # Apache Airflow environment configs & DAGs

Here is a comprehensive, production-ready `README.md` file tailored for your project. It includes professional badges, clear architectural structure, and detailed sections for all three sub-projects and MLOps tools.

---

```markdown
# Voyage Analytics: Integrating MLOps in Travel

Using MLOps practices to build, deploy, and monitor machine learning models that solve core problems in the travel and hospitality industry. This repository contains end-to-end pipelines for flight price prediction, hotel recommendations, and gender classification, fully integrated with modern MLOps tools.

---

## 🚀 Badges & Tech Stack

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CE2?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📂 Project Architecture & Directory Structure

```text
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
├── flight_price_api.py
├── flight-price-deployment.yml
├── best_flight_price_model.joblib
├── flight_api.log
├── DATA/                                 # Raw and processed datasets
├── Flight price prediction/              # Code, notebooks & research for Flight Price
├── Gender classification/                # Code, notebooks & research for Gender Profiling
├── Hotel Recommendation Model/           # Code, notebooks & research for Hotel Recs
└── airflow-docker/                       # Apache Airflow environment configs & DAGs

```

---

## 🛠️ Core Projects Overview

### 1. Flight Price Prediction

* **Objective:** Predict flight ticket prices based on features like airline, source, destination, stopovers, and departure time.
* **Model:** Built using optimized regression techniques (e.g., Random Forest / XGBoost) and saved as `best_flight_price_model.joblib`.
* **Deployment:** Exposed via a Flask REST API (`flight_price_api.py`) accepting JSON payloads and returning instant price evaluations.

### 2. Hotel Recommendation Model

* **Objective:** Recommend customized hotel choices to users based on historical preferences, locations, reviews, and amenities.
* **Model:** Collaborative filtering or content-based recommendation system designed to match customer intent with hotel features.

### 3. Gender Classification

* **Objective:** Classify user demographics (gender profile) based on booking behavior, travel history, or search preferences.
* **Model:** Classification model used to power downstream targeted marketing and personalized flight/hotel landing pages.

---

## 🔄 MLOps & Infrastructure Integration

> **Note:** The core value of Voyage Analytics lies in its automated lifecycle management, ensuring models don't degrade over time.

### 📈 MLflow: Experiment Tracking & Model Registry

* Tracks hyperparameters, metrics (RMSE, Accuracy), and code versions for all experimental runs across the three models.
* Acts as the central model registry to transition models from *Staging* to *Production*.

### 🌬️ Apache Airflow: Data & Training Pipelines

* Orchestrated via the configuration found in `airflow-docker/`.
* DAGs automate daily/weekly data ingestion from the `DATA/` directory, trigger data preprocessing, run validation tests, and execute retraining loops.

### 👷 Jenkins: Continuous Integration & Deployment (CI/CD)

* Automates the build triggers whenever code updates are pushed to the repository.
* Runs unit and integration tests, evaluates model performance checks, builds the production-ready Docker image, and pushes it to a container registry.

### 🐳 Docker: Containerization

* The system includes a global `Dockerfile` encapsulating the runtime dependencies (`requirements.txt`), Python environment, and the API endpoints.
* Ensures consistent "it works on my machine" reproducibility across local environments, staging, and production.

### ☸️ Kubernetes (K8s): Orchestration & Scaling

* Managed via `flight-price-deployment.yml`.
* Deploys the Flask prediction engine dynamically in a Kubernetes cluster.
* Configured with rolling updates to avoid downtime during model redeployments and auto-scaling to handle high concurrent traffic during holiday booking seasons.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Docker and Docker Compose installed.

### 1. Clone the Repository

```bash
git clone [https://github.com/sanidhya1996/Voyage-Analytics-Integrating-MLOps-in-Travel.git](https://github.com/sanidhya1996/Voyage-Analytics-Integrating-MLOps-in-Travel.git)
cd Voyage-Analytics-Integrating-MLOps-in-Travel

```

### 2. Run Locally via Flask

```bash
pip install -r requirements.txt
python flight_price_api.py

```

### 3. Build and Run Containerized Service

```bash
docker build -t voyage-analytics-api .
docker run -p 5000:5000 voyage-analytics-api

```

### 4. Deploy to Kubernetes

```bash
kubectl apply -f flight-price-deployment.yml

```

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

```

```
