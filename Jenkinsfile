pipeline {
    agent any

    environment {
        BACKEND_IMAGE  = "cicd-backend"
        FRONTEND_IMAGE = "cicd-frontend"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                echo 'Building backend and frontend images...'
                sh '''
                  docker build -t $BACKEND_IMAGE ./backend
                  docker build -t $FRONTEND_IMAGE ./frontend
                '''
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                echo 'Deploying application using Docker Compose...'
                sh '''
                  docker-compose down || true
                  docker-compose up -d
                '''
            }
        }

        stage('Health Check') {
            steps {
                echo 'Performing backend health check...'
                sh '''
                  for i in {1..10}; do
                    if docker-compose exec -T backend curl -f http://localhost:5000/health; then
                      echo "Backend is healthy"
                      exit 0
                    fi
                    echo "Waiting for backend to be ready..."
                    sleep 3
                  done
                  echo "Backend health check failed"
                  exit 1
                '''
            }
        }
    }

    post {
        success {
            echo 'CI/CD Pipeline completed successfully!'
        }
        failure {
            echo 'CI/CD Pipeline failed!'
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
