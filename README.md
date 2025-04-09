# DevOps for AI Capstone: Simple Sentiment Analysis API

[![Build Status](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/actions/workflows/ci-pipeline.yml/badge.svg)](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/actions/workflows/ci-pipeline.yml)

This project is a capstone demonstration focused on applying DevOps principles (specifically MLOps) to a simple Machine Learning application using open-source tools. It covers the lifecycle from model training to automated container building via a CI pipeline.

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
- [CI/CD Pipeline](#cicd-pipeline)
- [Future Work](#future-work)

## Project Goal

The primary goal of this project is to showcase a basic end-to-end workflow for developing, packaging, and setting up continuous integration for a machine learning model served via a REST API. It serves as an introduction to MLOps concepts like automation, containerization, and version control in an AI context.

## Features

*   **Simple Model Training:** Trains a basic Naive Bayes classifier for sentiment analysis using Scikit-learn.
*   **REST API:** Provides a Flask-based API endpoint (`/predict`) to get sentiment predictions for input text.
*   **Containerization:** Packages the Flask application and the trained model into a Docker container for consistent deployment.
*   **Continuous Integration (CI):** Implements a GitHub Actions workflow that automatically builds the Docker image upon pushes or pull requests to the `main` branch.
*   **Image Publishing:** Pushes the built Docker image to Docker Hub.

## Tech Stack

*   **Language:** Python 3.9
*   **ML Library:** Scikit-learn, Pandas
*   **Model Persistence:** Joblib
*   **Web Framework:** Flask
*   **Containerization:** Docker
*   **Version Control:** Git & GitHub
*   **CI/CD:** GitHub Actions
*   **Container Registry:** Docker Hub

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
## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

*   [Python 3.8+](https://www.python.org/downloads/) & `pip`
*   [Git](https://git-scm.com/downloads/)
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
*   A [GitHub](https://github.com/) account (for cloning and potential contributions)
*   A [Docker Hub](https://hub.docker.com/) account (if you want to push images yourself)

### Cloning

Clone the repository to your local machine:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
Use code with caution.
(Replace YOUR_GITHUB_USERNAME and YOUR_REPOSITORY_NAME with your actual details)
Installation
Create and activate a virtual environment: (Recommended)
# For Linux/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows (Command Prompt/PowerShell)
python -m venv venv
.\venv\Scripts\activate
Use code with caution.
Bash
Install Python dependencies:
pip install -r requirements.txt
Use code with caution.
Bash
Usage
There are multiple ways to run this application:
1. Training the Model (Optional)
The repository includes a pre-trained model (sentiment_model.joblib). However, if you want to retrain it (e.g., after modifying data.csv):
python train.py
Use code with caution.
Bash
This will overwrite the existing sentiment_model.joblib file.
2. Running the API Locally
This runs the Flask development server directly using your local Python environment.
python app.py
Use code with caution.
Bash
The API will be accessible at http://127.0.0.1:5000. Press Ctrl+C to stop the server.
3. Building and Running with Docker
This method uses the containerized version of the application.
Build the Docker image: (Make sure Docker Desktop is running)
docker build -t sentiment-api .
Use code with caution.
Bash
(You can use a different tag like <Your Docker Hub Username>/sentiment-api:latest if preferred)
Run the Docker container:
docker run -p 5001:5000 sentiment-api
Use code with caution.
Bash
This maps port 5001 on your host machine to port 5000 inside the container.
The API will now be accessible at http://127.0.0.1:5001. Press Ctrl+C in the terminal running the container to stop it.
Testing the API Endpoint
Once the API is running (either locally or via Docker), you can send POST requests to the /predict endpoint. Use a tool like curl, Postman, or Insomnia.
Example using curl:
If running locally (python app.py) use port 5000:
curl -X POST -H "Content-Type: application/json" \
     -d '{"text": "this movie was fantastic and wonderful"}' \
     http://127.0.0.1:5000/predict
Use code with caution.
Bash
If running via Docker (docker run -p 5001:5000 ...) use port 5001:
curl -X POST -H "Content-Type: application/json" \
     -d '{"text": "the experience was truly terrible"}' \
     http://127.0.0.1:5001/predict
Use code with caution.
Bash
Expected JSON Response:
{
  "input_text": "this movie was fantastic and wonderful",
  "prediction": "positive",
  "probability_negative": 0.0XXXX, // Actual probability value
  "probability_positive": 0.9YYYY  // Actual probability value
}
Use code with caution.
Json
CI/CD Pipeline
This project uses GitHub Actions for Continuous Integration. The workflow is defined in .github/workflows/ci-pipeline.yml.
Trigger: The workflow runs automatically on every push or pull_request targeting the main branch. It can also be triggered manually from the GitHub Actions tab.
Job: It performs the following steps:
Checks out the repository code.
Logs into Docker Hub using credentials stored as GitHub Secrets (DOCKERHUB_USERNAME, DOCKERHUB_TOKEN).
Builds the Docker image using the Dockerfile in the repository root.
Pushes the built image to Docker Hub, tagging it as <Your Docker Hub Username>/sentiment-api:latest.
Note: For the CI pipeline to push successfully to your Docker Hub, you must configure the DOCKERHUB_USERNAME and DOCKERHUB_TOKEN secrets in your GitHub repository settings (Settings -> Secrets and variables -> Actions). Replace <Your Docker Hub Username> in the workflow file and this README with your actual Docker Hub username.
Future Work
This project provides a foundational MLOps pipeline. Potential enhancements include:
Testing: Implement unit tests for the Flask API and potentially integration tests. Add a testing stage to the CI pipeline.
Experiment Tracking: Integrate MLflow to log parameters, metrics, and the model during training (train.py).
Model Versioning: Use MLflow Model Registry or DVC for more robust model versioning instead of committing the .joblib file directly.
Continuous Deployment (CD): Extend the pipeline to automatically deploy the built Docker container to a hosting platform (e.g., AWS ECS, Google Cloud Run, Heroku, Kubernetes).
Monitoring: Add logging and basic monitoring (e.g., request latency, error rates) to the Flask application.
Data/Model Drift: Implement basic checks for data drift or model performance degradation.