pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sentry1904/flask-app"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sentry1904/newrep3.git',
                    credentialsId: 'github-pat-creds'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
                '''
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                 usernameVariable: 'DOCKER_USER',
                                                 passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $DOCKER_IMAGE:$DOCKER_TAG
                    '''
                }
            }
        }

        stage('Pull and Run Container') {
            steps {
                sh '''
                    docker pull $DOCKER_IMAGE:$DOCKER_TAG
                    docker run --rm -p 5000:5000 $DOCKER_IMAGE:$DOCKER_TAG &
                    sleep 5
                    curl -s http://localhost:5000
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

