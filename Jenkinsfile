properties([pipelineTriggers([pollSCM('H * * * *')])])

pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'apt install python3 python3-pip -y'
                sh 'python3 -m pip install -r requirements.txt'
            }
        }
        stage('Start web server') {
            steps {
                sh 'python3 MainScores.py'
            }
        }
    }
}