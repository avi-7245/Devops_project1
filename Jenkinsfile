pipeline {
    agent any

    stages {
        stage('Clone from GitHub') {
            steps {
                    git branch: 'main', url: 'https://github.com/avi-7245/Devops_project1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-ci-app .'
            }
        }

        stage('Run Unit Test') {
            steps {
                sh 'python test_my_app.py'
            }
        }

        stage('Run App Container') {
            steps {
                sh 'docker run -d -p 5000:5000 devops-ci-app'
            }
        }
    }
}
