pipeline {
    agent any

    stages {
        stage('build image') {
            steps {
                sh "docker build -t juice-point:1.1 ."
            }
        }
        stage('docker push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-credentials', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                sh "docker tag juice-point:1.0 bogevijitha/juice-bandii:1.0"
                sh "echo $PASS | docker login -u $USER --password-stdin"
                sh "docker push bogevijitha/juice-bandii:1.0"
                }
            }
        }
        stage('deploy') {
            steps {
                echo 'deploy to ec2...'
            }
        }
    }
}