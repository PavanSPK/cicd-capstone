pipeline {
    agent any

    environment {
        BACKEND_IMAGE  = "spk487/cicd-backend:latest"
        FRONTEND_IMAGE = "spk487/cicd-frontend:latest"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                docker build -t $BACKEND_IMAGE ./backend
                docker build -t $FRONTEND_IMAGE ./frontend
                '''
            }
        }

        stage('Container Test (Health Check)') {
    steps {
        sh '''
        docker-compose down || true
        docker-compose up -d

        echo "Waiting for backend to become healthy..."

        for i in {1..10}; do
          if docker-compose exec -T backend curl -sf http://localhost:5000/health; then
            echo "Backend is healthy"
            exit 0
          fi
          echo "Retry $i..."
          sleep 3
        done

        echo "Backend health check failed"
        docker-compose logs backend
        exit 1
        '''
    }
}


        stage('Security Scan (Trivy)') {
            steps {
                sh '''
                trivy image --severity HIGH,CRITICAL --exit-code 0 $BACKEND_IMAGE
                trivy image --severity HIGH,CRITICAL --exit-code 0 $FRONTEND_IMAGE
                '''
            }
        }

        stage('Push Images to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker push $BACKEND_IMAGE
                    docker push $FRONTEND_IMAGE
                    '''
                }
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                docker-compose down
                docker-compose up -d
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed"
        }
        success {
            echo "CI/CD pipeline SUCCESSFUL"
        }
        failure {
            echo "CI/CD pipeline FAILED"
        }
    }
}
