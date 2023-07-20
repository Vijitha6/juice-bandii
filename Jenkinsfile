pipeline {
    agent any

    stages {
        stage('build image') {
            steps {
                sh "docker build -t juice-point:1.0 ."
            }
        }
        stage('docker push') {
            steps {
                sh "docker tag juice-point:1.0 bogevijitha/juice-bandii:1.0"
                sh "docker push bogevijitha/juice-bandii:1.0"
            }
        }
        stage('deploy') {
            steps {
                echo 'deploy to ec2...'
            }
        }
    }
}