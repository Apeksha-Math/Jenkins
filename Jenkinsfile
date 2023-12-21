pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Apeksha-Math/Jenkins.git']])
            }
        }
        stage('Build'){
            steps{
                git branch: 'main', url: 'https://github.com/Apeksha-Math/Jenkins.git'
                // bat 'python simplecode.py'
            }
        }
        stage('Test'){
            steps{
                echo 'the multibranch job has been tested'
            }
        }
    }
}
