pipeline {
    agent any

    stages {
        stage('Serve UI') {
            steps {
                // Run Flask in background and capture logs
                sh 'nohup python3 app.py > flask.log 2>&1 &'
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

