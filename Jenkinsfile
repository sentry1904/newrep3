pipeline {
    agent { any }

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
                    docker tag $DOCKER_IMAGE:$DOCKER_TAG $DOCKER_IMAGE:$BUILD_NUMBER
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
                        docker push $DOCKER_IMAGE:$BUILD_NUMBER

                        # Enforce max 3 tags: keep latest + 2 most recent build numbers
                        TAGS=$(curl -s -u "$DOCKER_USER:$DOCKER_PASS" https://hub.docker.com/v2/repositories/$DOCKER_IMAGE/tags/?page_size=100 | grep -o '"name":"[^"]*"' | cut -d'"' -f4 | grep -v latest | sort -n)
                        COUNT=$(echo "$TAGS" | wc -l)
                        if [ $COUNT -gt 2 ]; then
                          DELETE=$(echo "$TAGS" | head -n1)
                          echo "Deleting oldest build tag: $DELETE"
                          curl -s -X DELETE -u "$DOCKER_USER:$DOCKER_PASS" https://hub.docker.com/v2/repositories/$DOCKER_IMAGE/tags/$DELETE/
                        fi
                    '''
                }
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                    docker run -d -p 5000:5000 --name flaskapp $DOCKER_IMAGE:$DOCKER_TAG || true
                    sleep 5
                    echo "Response from Flask app:"
                    curl -s http://localhost:5000
                    echo "Container logs:"
                    docker logs flaskapp
                '''
            }
        }
    }
}

