pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout using HTTPS and Jenkins credentials (PAT stored in Jenkins)
                git branch: 'main',
                    url: 'https://github.com/sentry1904/newrep3.git',
                    credentialsId: 'github-pat-creds'
            }
        }

        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    export FLASK_APP=app.py
                    export FLASK_ENV=development
                    nohup python -m flask run --host=0.0.0.0 --port=5000 &
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

