pipeline {
    agent any

    environment {
        IMAGE_NAME = "nikhilsonawane2jpg/devops-app"
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} app/
                '''
            }
        }

        stage('Push Docker Image') {
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
    
    post {
        success {
            echo "✅ Pipeline completed successfully"
        }
        failure {
            echo "❌ Pipeline failed"
        }
    }
}
