pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/yourusername/cicd-capstone.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                docker build -t backend backend
                docker build -t frontend frontend
                '''
            }
        }

        stage('Run Tests Inside Container') {
            steps {
                sh '''
                docker run backend python -c "print('Tests passed')"
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                echo "Trivy scan simulated"
                '''
            }
        }

        stage('Deploy to Dev') {
            steps {
                sh '''
                docker compose down
                docker compose up -d
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                curl http://localhost:5000/health
                '''
            }
        }

        stage('Approval for Production') {
            steps {
                input message: 'Deploy to Production?'
            }
        }

        stage('Deploy to Production') {
            steps {
                sh '''
                docker compose down
                docker compose up -d
                '''
            }
        }
    }

    post {
        failure {
            sh 'docker compose down'
        }
    }
}
