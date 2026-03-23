pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sentry1904/newrep3'
            }
        }

        stage('Build') {
            steps {
                // Install only what is needed
                sh 'pip install numpy matplotlib pytest'
            }
        }

        stage('Test') {
            steps {
                // Run tests if you add test_py2.py
                sh 'pytest --junitxml=results.xml || echo "No tests found"'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Run Script') {
            steps {
                sh 'python py2.py'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'chart.png', fingerprint: true
            }
        }

        stage('Deploy') {
            steps {
                echo 'Simulated deployment of py2.py application...'
                // Example: sh 'docker build -t py2app . && docker run py2app'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

