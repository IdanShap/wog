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
        stage('Move files to /var/tmp/') {
            steps {
                sh 'mkdir /var/tmp/wog/'
                sh 'cp ./* /var/tmp/wog/'
            }
        }
        stage('Start web server') {
            steps {
                sh 'kill -2 $(pidof nohup)'
                sh 'nohup python3 /var/tmp/wog/MainScores.py &'
            }
        }
    }
}
