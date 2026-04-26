pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/your-username/devops-project.git'
            }
        }

        stage('Build') {
            steps {
                bat 'docker build -t notes-app .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker run -d -p 5000:5000 notes-app'
            }
        }
    }
}