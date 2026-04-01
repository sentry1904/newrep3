pipeline {
    agent any

    environment {
        SONARQUBE = 'SonarQubeServer'  // Replace with the name of your SonarQube server configured in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone your repository using your GitHub username
                git branch: 'main', url: 'https://github.com/sentry1904/newrep3.git'
            }
        }

        stage('Build') {
            steps {
                // Run Python file to verify execution
                sh 'python3 py1.py'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Run SonarQube scanner
                    withSonarQubeEnv("${SONARQUBE}") {
                        sh 'sonar-scanner \
                            -Dsonar.projectKey=newrep3 \
                            -Dsonar.projectName=newrep3 \
                            -Dsonar.sources=. \
                            -Dsonar.language=py \
                            -Dsonar.python.version=3'
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    // Wait for SonarQube quality gate result
                    timeout(time: 5, unit: 'MINUTES') {
                        waitForQualityGate abortPipeline: true
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build and analysis completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}

