pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://your-repo-url.git'
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
                    python -m flask run --host=0.0.0.0 --port=5000
                '''
            }
        }
    }
}

