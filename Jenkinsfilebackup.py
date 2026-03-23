pipeline {
    agent any

    stages {
        stage('Serve UI') {
            steps {
                // Run Flask in background and capture logs
                sh 'python3 app.py'
                echo 'Flask UI is now available at http://192.168.156.31:5000'
            }
        }
        stage('Archive Logs') {
            steps {
                archiveArtifacts artifacts: 'flask.log', fingerprint: true
            }
        }
    }
}

