# MLOPS: Simple Sentiment Analysis API

[![Build Status](https://github.com/Ansh-Ghawri/MLOPS-API-Deployment/actions/workflows/ci-pipeline.yml/badge.svg)](https://github.com/Ansh-Ghawri/MLOPS-API-Deployment/actions/workflows/ci-pipeline.yml)

This project is a capstone demonstration focused on applying DevOps principles (specifically MLOps) to a Machine Learning application using open-source tools. 
It covers the lifecycle from model training to automated container building via a CI pipeline.

## Table of Contents

- [Project Goal](#project-goal)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Cloning](#cloning)
  - [Installation](#installation)
- [Usage](#usage)
  - [1. Training the Model (Optional)](#1-training-the-model-optional)
  - [2. Running the API Locally](#2-running-the-api-locally)
  - [3. Building and Running with Docker](#3-building-and-running-with-docker)
- [Testing the API Endpoint](#testing-the-api-endpoint)
- [CI/CD Pipeline (GitHub Actions)](#cicd-pipeline-github-actions)
- [Future Work](#future-work)
- [Contact](#contact)

## Project Goal

The primary goal of this project is to showcase a basic end-to-end workflow for developing, packaging, and setting up continuous integration for a machine learning model served via a REST API. It serves as an introduction to MLOps concepts like automation, containerization, and version control in an AI context.

## Features

* **Simple Model Training:** Trains a basic Naive Bayes classifier for sentiment analysis using Scikit-learn.
* **REST API:** Provides a Flask-based API endpoint (`/predict`) to get sentiment predictions for input text.
* **Containerization:** Packages the Flask application and the trained model into a Docker container for consistent deployment.
* **Continuous Integration (CI):** Implements a GitHub Actions workflow that automatically builds the Docker image upon pushes or pull requests to the `main` branch.
* **Image Publishing:** Pushes the built Docker image to Docker Hub.

## Tech Stack

* **Language:** Python 3.9
* **ML Library:** Scikit-learn, Pandas
* **Model Persistence:** Joblib
* **Web Framework:** Flask
* **Containerization:** Docker
* **Version Control:** Git & GitHub
* **CI/CD:** GitHub Actions
* **Container Registry:** Docker Hub

## Project Structure
Use code with caution.
Markdown
.
├── .github/workflows/ # GitHub Actions workflow definitions
│ └── ci-pipeline.yml # Workflow for building and pushing Docker image
├── .dockerignore # Specifies files/dirs to ignore during Docker build
├── .gitignore # Specifies intentionally untracked files for Git
├── Dockerfile # Instructions to build the Docker image
├── README.md # This documentation file
├── app.py # Flask application code for the API endpoint
├── data.csv # Simple dataset for training
├── requirements.txt # Python dependencies
├── sentiment_model.joblib # Saved (pre-trained) model file
└── train.py # Python script to train the model

## 📦 Cloning the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

---

## ⚙️ Installation

### Create and Activate a Virtual Environment (Recommended)

#### For Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows (Command Prompt/PowerShell):
```bash
python -m venv venv
.env\Scriptsctivate
```

### Install Python Dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Training the Model (Optional)

A pre-trained model `sentiment_model.joblib` is included. To retrain (e.g., after modifying `data.csv`):

```bash
python train.py
```

> This will overwrite the existing `sentiment_model.joblib` file.

---

### 2. Running the API Locally

This will start the Flask development server:

```bash
python app.py
```

Access the API at: [http://127.0.0.1:5000](http://127.0.0.1:5000)  
To stop the server: `Ctrl + C`

---

### 3. Building and Running with Docker

#### Build the Docker image:
(Make sure Docker Desktop is running)

```bash
docker build -t sentiment-api .
```

#### Run the Docker container:

```bash
docker run -p 5001:5000 sentiment-api
```

Access the API at: [http://127.0.0.1:5001](http://127.0.0.1:5001)

---

## Testing the API Endpoint

You can test the `/predict` endpoint using `curl`, Postman, or Insomnia.

### Example using `curl`:

#### If running locally (`python app.py`, port 5000):
```bash
curl -X POST -H "Content-Type: application/json"      -d '{"text": "this movie was fantastic and wonderful"}'      http://127.0.0.1:5000/predict
```

#### If running via Docker (`docker run`, port 5001):
```bash
curl -X POST -H "Content-Type: application/json"      -d '{"text": "the experience was truly terrible"}'      http://127.0.0.1:5001/predict
```

### Expected JSON Response:
```json
{
  "input_text": "this movie was fantastic and wonderful",
  "prediction": "positive",
  "probability_negative": 0.0XXXX,
  "probability_positive": 0.9YYYY
}
```

---

## CI/CD Pipeline (GitHub Actions)

### Workflow File: `.github/workflows/ci-pipeline.yml`

#### 🔁 Trigger:
- On every `push` or `pull_request` to the `main` branch
- Can be manually triggered from the **GitHub Actions** tab

#### ✅ Jobs:
- Checkout repository
- Log in to Docker Hub using `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` (stored in GitHub Secrets)
- Build the Docker image using the `Dockerfile`
- Push image to Docker Hub:  
  Tagged as:  
  ```
  <Your Docker Hub Username>/sentiment-api:latest
  ```

> **Note:** Set up GitHub Secrets:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Update the workflow and this README to replace `<Your Docker Hub Username>`.

---

## Future Work

- **Testing**: Add unit and integration tests, and a CI test stage.
- **Experiment Tracking**: Integrate MLflow for logging training metrics and models.
- **Model Versioning**: Use MLflow Model Registry or DVC instead of committing `.joblib`.
- **Continuous Deployment (CD)**: Deploy containers to AWS ECS, Google Cloud Run, Heroku, or Kubernetes.
- **Monitoring**: Add logging, latency tracking, and error monitoring.
- **Data/Model Drift Detection**: Implement basic drift checks.

---

## Contact

Have suggestions or improvements? Open an issue or PR!
Email:ghawri.ansh@gmail.com

---

