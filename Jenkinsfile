pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/dev1']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Apeksha-Math/Jenkins.git']])
            }
        }
        stage('Build'){
            steps{
                git branch: 'dev1', url: 'https://github.com/Apeksha-Math/Jenkins.git'
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
