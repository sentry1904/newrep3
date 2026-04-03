pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // Jenkins credential ID
        IMAGE_NAME = "your-dockerhub-username/newrep3-app1"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                    sh "docker push ${IMAGE_NAME}:latest"
                }
            }
        }

        stage('Pull and Run') {
            steps {
                script {
                    sh "docker pull ${IMAGE_NAME}:latest"
                    // Run detached, map port 5000
                    sh "docker run -d -p 5000:5000 --name app1 ${IMAGE_NAME}:latest"
                }
            }
        }
    }
}

