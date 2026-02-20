📦 DevOps CI/CD Pipeline using Jenkins, Docker & Kubernetes

This repository demonstrates a complete End-to-End CI/CD pipeline that automates building, containerizing, pushing, and deploying an application using:

✔️ Jenkins
✔ Docker
✔ Docker Hub
✔ Kubernetes (Minikube)
✔ ConfigMaps, Secrets, Ingress, HPA

🧠 Project Overview

This project showcases a production-style DevOps workflow starting from code commit all the way to deployment on a Kubernetes cluster.
The pipeline includes:

✔ Automated Docker image build
✔ Docker Hub image push
✔ Kubernetes deployment with rolling updates
✔ Configuration management using ConfigMap & Secret
✔ Automatic scaling via HPA
✔ Declarative pipeline using Jenkinsfile

📁 Repository Structure
Devops-project/
│
├── app/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── jenkins/
│   └── Jenkinsfile
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── ingress.yaml
│   └── hpa.yaml
│
├── Dockerfile.jenkins
├── README.md
└── .gitignore
🚀 Architecture Diagram
  GitHub Repo
        ↓
     Jenkins
        ↓
 Docker Build & Push (to Docker Hub)
        ↓
 Kubernetes Deployment (Minikube)
        ↓
     Application Live
🔧 Tools & Technologies Used
Component	Technology
CI/CD Server	Jenkins (Hosted locally)
Containerization	Docker
Container Registry	Docker Hub
Orchestration	Kubernetes (Minikube)
Configuration	ConfigMap, Secrets
Scaling	Horizontal Pod Autoscaler
Networking	Kubernetes Service + Ingress
📦 Prerequisites

Before you begin, make sure you have the following installed:

✔ Docker Desktop
✔ Minikube
✔ kubectl
✔ Jenkins (local or containerized)
✔ GitHub account
✔ Docker Hub account

Ensure kubectl is connected to your Minikube:

kubectl get nodes
📝 Kubernetes Manifest Files
🐣 Deployment

Defines your application deployment with rolling updates and probes:

# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: devops-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: devops-app
  template:
    metadata:
      labels:
        app: devops-app
    spec:
      containers:
      - name: devops-app
        image: nikhilsonawane2jpg/devops-app:IMAGE_TAG
        ports:
        - containerPort: 5000
        readinessProbe:
          httpGet:
            path: /
            port: 5000
        livenessProbe:
          httpGet:
            path: /
            port: 5000

…

(extend other files similarly)

📌 Setup Jenkins (Local macOS)
1️⃣ Install Jenkins
brew install jenkins-lts
brew services start jenkins-lts
2️⃣ Access Jenkins

Open:

http://localhost:8080

Unlock using:

cat ~/.jenkins/secrets/initialAdminPassword
3️⃣ Install Plugins

Install:
✔ Docker
✔ Kubernetes CLI (kubectl)
✔ Pipeline

📌 Configure Jenkins Credentials

✔ DockerHub Password

Kind: Secret text

ID: dockerhub-password

📌 Full Jenkinsfile

Save this in your repo under:

jenkins/Jenkinsfile
pipeline {
    agent any

    environment {
        IMAGE_NAME = "nikhilsonawane2jpg/devops-app"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} app/'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-password', variable: 'DOCKER_PASS')]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u nikhilsonawane2jpg --password-stdin
                      docker push ${IMAGE_NAME}:${BUILD_NUMBER}
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                  sed -i.bak "s|IMAGE_TAG|${BUILD_NUMBER}|g" k8s/deployment.yaml
                  kubectl apply -f k8s/
                '''
            }
        }
    }
}
🛠 Running the Pipeline

Commit & push code to GitHub

Jenkins poll or webhook triggers build

Pipeline builds image

Pushes to Docker Hub

Deploys to Kubernetes

You should see logs showing deployment rollout.

🔍 Verify Deployment
kubectl get pods
kubectl get svc
kubectl rollout status deployment/devops-app
📈 Scaling (HPA)

Horizontal Pod Autoscaler scales based on CPU:

kubectl get hpa
🧠 What You Learned

✔ Building Docker images in CI
✔ Managing Docker credentials securely
✔ Automating deployments with Jenkins pipelines
✔ Kubernetes deployment strategies
✔ Liveness & readiness probes
✔ Horizontal Pod Autoscaling

📌 Notes

Do not commit kubeconfig or sensitive files

.gitignore includes:

kubeconfig-jenkins.yaml
*.crt
*.key
🎯 Contact

📍 GitHub: https://github.com/nikhilsonawane-jpg

📥 nikhil@example.com
