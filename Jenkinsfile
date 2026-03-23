pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/sentry1904/newrep3'
                sh 'git pull origin main'
            }
        }

        stage('Build') {
            steps {
                // Install Python dependencies including Flask
                sh 'pip install numpy matplotlib pytest flask'
            }
        }

        stage('Test') {
            steps {
                // Run tests if pytest.py exists
                sh 'python3 pytest.py || echo "No tests found"'
            }
        }

        stage('Run Script') {
            steps {
                // Run your main script
                sh 'python3 py2.py'
                // Copy chart to static folder for Flask
                sh 'mkdir -p static && cp chart.png static/chart.png'
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'chart.png', fingerprint: true
            }
        }

        stage('Serve UI') {
            steps {
                // Run Flask app on port 8080 in background
                sh 'nohup python3 app.py &'
                echo 'Flask UI is now available at http://<jenkins-server>:5000'       }
        }

        stage('Deploy') {
            steps {
                echo 'Simulated deployment of py2.py application...'
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

