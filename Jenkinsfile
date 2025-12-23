pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Code checked out from GitHub'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                docker build -t cicd-backend ./backend
                docker build -t cicd-frontend ./frontend
                '''
            }
        }

      stage('Run Application (Docker Compose)') {
    steps {
        sh '''
        docker-compose down || true
        docker-compose up -d
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
    }
}
