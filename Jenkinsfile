pipeline {
    agent any

    stages {
        stage('Serve UI') {
            steps {
                // Run Flask in background
                sh 'nohup python3 app.py > flask.log 2>&1 &'
                echo 'Flask UI is now available at http://192.168.156.31:5000'
            }
        }

        stage('Monitor Flask Exit') {
            steps {
                script {
                    // Wait for Flask to exit (SIGTERM when input == 100)
                    def status = sh(script: "ps -ef | grep 'python3 app.py' | grep -v grep || true", returnStdout: true).trim()
                    if (status == "") {
                        echo "Flask stopped — performing cleanup"
                        cleanWs()
                        error("Pipeline stopped due to user input 100")
                    } else {
                        echo "Flask still running"
                    }
                }
            }
        }

        stage('Archive Logs') {
            steps {
                archiveArtifacts artifacts: 'flask.log', fingerprint: true
            }
        }
    }

    post {
        always {
            echo "Pipeline finished (success or failure)."
        }
    }
}

