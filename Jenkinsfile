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
                script {
                    try {
                        sh 'mkdir /var/tmp/'
                        sh 'cp ./* /var/tmp/'
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }
                }
            }
        }
        stage('Start web server') {
            steps {
                sh 'chmod 777 /var/tmp/web_init.sh'
                sh '/var/tmp/web_init.sh'
            }
        }
    }
}
