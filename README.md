# CI/CD Capstone Project – Docker & Jenkins

## 1.Project Overview

In this project, I designed and implemented an end-to-end CI/CD pipeline using Docker, Docker Compose, and Jenkins for a simple 2-tier web application.
The objective was to automate the complete application lifecycle — from code commit to deployment — while following practical DevOps and containerization best practices.

The pipeline is triggered automatically on every code push and performs build, runtime validation, security scanning, image publishing, and deployment without manual intervention.

-----------------------------------------------------------------------------------

## 2.Problem Statement

Build a complete CI/CD system that automatically tests, builds, and deploys a simple web application through development, staging, and production environments using Docker and Jenkins.

-----------------------------------------------------------------------------------

## 3.Technology Stack

| Layer            | Technology                  |
| ---------------- | --------------------------- |
| Frontend         | HTML + CSS served via Nginx |
| Backend          | Python Flask                |
| Database         | PostgreSQL                  |
| CI/CD            | Jenkins                     |
| Containerization | Docker                      |
| Orchestration    | Docker Compose              |
| Image Registry   | Docker Hub                  |
| Security Scan    | Trivy                       |
| Webhook Exposure | ngrok                       |
| Version Control  | GitHub                      |

-----------------------------------------------------------------------------------

## 4.Project Architecture

The application follows a 2-tier architecture with CI/CD automation.

Architecture Flow:
- Developer pushes code to GitHub
- GitHub Webhook triggers Jenkins automatically
- Jenkins pipeline builds, tests, scans, and pushes images
- Jenkins deploys application to target environment
- Frontend communicates with backend
- Backend interacts with PostgreSQL database

![cicd](https://github.com/PavanSPK/cicd-capstone/blob/443ed22f47f3f8647e917bde653fea0c22d8ff54/screenshots/cicd.png)

### Jenkins Pipeline Architecture

![jenkins_pipeline](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/jenkins_pipeline.png)

-----------------------------------------------------------------------------------
## 5.Application Architecture
### 5.1 Frontend
- Static HTML/CSS application
- Served using Nginx
- Displays:
    - Application health status
    - Database connection status
    - Total record count
    - Employee data table

### 5.2 Backend
- Flask REST API
- Provides endpoints:
    - /health – application health
    - /db-status – database status and employee records
- Uses environment variables for database connection

### 5.3 Database
- PostgreSQL container
- Stores employee records
- Persistent volume for data durability

![application](https://github.com/PavanSPK/cicd-capstone/blob/2d41e469a2c54b668aaac5ab75b8c441aa139542/screenshots/application.png)

-----------------------------------------------------------------------------------

## 6. Project Structure

```
cicd-capstone/
│
├── backend/
│   ├── app.py                # Flask backend application
│   ├── requirements.txt      # Python dependencies
│   └── Dockerfile            # Multi-stage backend Dockerfile
│
├── frontend/
│   ├── index.html            # UI displaying app & database status
│   └── Dockerfile            # Nginx-based frontend Dockerfile
│
├── scripts/
│   └── deploy.sh             # Environment-based deployment script
│
├── .env.dev                  # Development environment variables
├── .env.staging              # Staging environment variables
├── .env.prod                 # Production environment variables
│
├── docker-compose.yml        # Multi-service orchestration
├── Jenkinsfile               # CI/CD pipeline definition
├── README.md                 # Project documentation

```
-----------------------------------------------------------------------------------

## 7. Tools & Technologies Used

List of all tools used in the project, along with their purpose and where they are implemented.

### 7.1 Docker
Purpose: Containerization platform.  
Usage in Project:
- Containerizes frontend, backend, database, and Jenkins
- Ensures consistency across environments
- Used in Jenkins pipeline for image build, push, and deployment

### 7.2 Docker Compose
Purpose: Multi-container orchestration.  
Usage in Project:
- Defines frontend, backend, and database services
- Creates shared networks and persistent volumes
- Used for local development, testing, and deployment

### 7.3 Jenkins
Purpose: CI/CD automation tool.  
Usage in Project:
- Runs as a Docker container
- Executes full CI/CD pipeline defined in Jenkinsfile
- Handles build, test, scan, push, and deployment stages
- Includes manual approval gate for production

### 7.4 GitHub
Purpose: Source code management.  
Usage in Project:
- Stores application source code
- Triggers Jenkins pipeline using GitHub Webhooks
- Acts as the CI trigger point

### 7.5 GitHub Webhook
Purpose: Automatic pipeline triggering.  
Usage in Project:
- Jenkins pipeline starts automatically on every git push
- Eliminates manual “Build Now”
- Enables true Continuous Integration

### 7.6 ngrok
Purpose: Public URL tunneling.  
Usage in Project:
- Exposes locally running Jenkins to the public internet
- Required because GitHub Webhooks need a public endpoint
- Used only for webhook communication

### 7.7 Flask
Purpose: Backend web framework.  
Usage in Project:
- Provides REST APIs
- Exposes /health and /db-status endpoints
- Connects to PostgreSQL database
- Returns JSON data consumed by frontend

### 7.8 Flask-CORS
Purpose: Cross-Origin Resource Sharing.  
Usage in Project:
- Allows frontend (port 80) to access backend APIs (port 5000)
- Prevents browser CORS blocking
- Required for frontend–backend communication

### 7.9 Nginx
Purpose: Web server.  
Usage in Project:
- Serves static frontend files
- Used with nginx:alpine image for minimal size
- Acts as production-grade frontend server

### 7.10 PostgreSQL
Purpose: Relational database.  
Usage in Project:
- Stores employee records
- Runs as a Docker container
- Connected to backend using environment variables
- Data displayed dynamically on frontend UI

### 7.11 Trivy
Purpose: Container security scanning.  
Usage in Project:
- Scans Docker images for vulnerabilities
- Integrated into Jenkins pipeline
- Ensures secure images before deployment

### 7.12 Bash / Shell Scripts
Purpose: Deployment automation.  
Usage in Project:
- deploy.sh handles environment-specific deployment
- Automates container restart and health verification
- Used by Jenkins during CD stages
-----------------------------------------------------------------------------------
## 8.Pulling and Running the Project on Any Computer

## 8.1.Prerequisites
- Docker
- Docker Compose
- Git
- Jenkins

### Step 1: Clone Repository

```
git clone https://github.com/PavanSPK/cicd-capstone.git
cd cicd-capstone
```

### Step 2: Pull Docker Images

```
docker pull spk487/cicd-backend:latest
docker pull spk487/cicd-frontend:latest
```

### Step 3: Run Application

```
docker-compose up -d
```

### Step 4: Verify Application

- Frontend UI: http://localhost
- Backend API: http://localhost:5000
- Health Endpoint: http://localhost:5000/health

### Backend Check

![backend_check](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/backend_check.png)

Backend API: http://localhost:5000

![backend](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/backend.png)

### Health check

![health_check](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/health_check.png)

Health Endpoint: http://localhost:5000/health

![health_status](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/health_status.png)

### Database check

![db_status](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/db_status.png)

-----------------------------------------------------------------------------------

## 9.Dockerization Strategy
### 9.1 Backend Dockerfile
The backend image follows container best practices:
- Multi-stage build to reduce image size
- Non-root user (appuser) for security
- Optimized layer caching
- Minimal final runtime image

### 9.2 Frontend Dockerfile
- Based on nginx:alpine
- Serves static content only
- Extremely small image footprint

### 9.3 Image Optimization
Docker images were optimized using best practices.
- Backend image uses multi-stage builds to exclude build-time dependencies.
- Frontend image uses Nginx Alpine for a minimal runtime footprint.

Image Content Size:
- Backend (multi-stage): ~56 MB
- Frontend (Nginx Alpine): ~23 MB

![image_optimize](https://github.com/PavanSPK/cicd-capstone/blob/36ad1ad1018615b6f743b5c002a6472a905ad900/screenshots/image_optimize.png)

-----------------------------------------------------------------------------------

## 10. Docker Compose Configuration
docker-compose.yml includes:
### Services
- backend
- frontend
- db (PostgreSQL)

### Features
- Isolated Docker network
- Named volume for database persistence
- Environment variables for database configuration
Docker Compose is used both locally and during deployment to ensure environment consistency.

![docker_compose](https://github.com/PavanSPK/cicd-capstone/blob/2d41e469a2c54b668aaac5ab75b8c441aa139542/screenshots/docker_compose.png)

-----------------------------------------------------------------------------------

## 11. CI/CD Pipeline Using Jenkins

The complete CI/CD workflow is defined in the Jenkinsfile

### Pipeline Stages

Pipeline Stages:

1. Checkout Code
2. Build Docker Images
3. Container Health Test
4. Security Scan (Trivy)
5. Push Images to Docker Hub
6. Deploy to Development
7. Deploy to Staging
8. Manual Approval
9. Deploy to Production

![cicd_pipeline](https://github.com/PavanSPK/cicd-capstone/blob/2d41e469a2c54b668aaac5ab75b8c441aa139542/screenshots/cicd_pipeline.png)

-----------------------------------------------------------------------------------

## 12. Runtime Health Check Enforcement
After building the images, Jenkins:
- Starts the containers using Docker Compose
- Polls the /health endpoint
- Retries automatically if needed
- Fails the pipeline if the service does not become healthy

-----------------------------------------------------------------------------------

## 13. Security Scanning with Trivy
Trivy is integrated into the pipeline as a mandatory gate.
- Scans backend image
- Checks for HIGH and CRITICAL vulnerabilities
- Pipeline fails immediately if issues are found
This step ensures that insecure images are never deployed.

![trivy_1](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/trivy_1.png)

![trivy_2](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/trivy_2.png)

![trivy_3](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/trivy_3.png)

-----------------------------------------------------------------------------------

## 14. Docker Hub Image Registry
- Backend and frontend images are pushed separately
- Docker Hub access token is used (no plaintext credentials)
- Images are versioned and reusable across environments

![dockerhub](https://github.com/PavanSPK/cicd-capstone/blob/2d41e469a2c54b668aaac5ab75b8c441aa139542/screenshots/dockerhub.png)

-----------------------------------------------------------------------------------

## 15. Environment Mapping Explanation
Although the same Docker Compose configuration is reused, logical environments are clearly defined through execution context and process separation.

### Development Environment
- Local machine execution
- Manual docker-compose up
- Used for development and local testing

### Staging Environment
- Jenkins pipeline execution
- Automated build, test, scan, and validation
- Acts as a controlled pre-production gate

### Production Environment
- Final Jenkins deployment stage
- Uses Docker Hub images
- Fully automated deployment via Docker Compose

-----------------------------------------------------------------------------------

## 16. Continuous Integration (Webhook)
- Every GitHub push triggers Jenkins automatically
- No manual intervention required
- ngrok provides public webhook access

![ngrok](https://github.com/PavanSPK/cicd-capstone/blob/2d41e469a2c54b668aaac5ab75b8c441aa139542/screenshots/ngrok.png)

-----------------------------------------------------------------------------------
## 17. Continuous Deployment
- Jenkins pulls latest images
- Stops old containers
- Starts new containers
- Verifies deployment using /health endpoint
- Production deployment requires manual approval

![approve](https://github.com/PavanSPK/cicd-capstone/blob/d0fd24f679cbc1c409805ce64b19c21eb26c0718/screenshots/approve.png)

-----------------------------------------------------------------------------------
## 18. Deployment Script
deploy.sh performs:
- Existing containers are stopped
- Latest images are pulled from Docker Hub
- New containers are started using Docker Compose
- No manual deployment steps are required

-----------------------------------------------------------------------------------
## 19.Troubleshooting Guide
This section lists common issues encountered during local execution or CI/CD pipeline runs, along with quick resolutions.

### Containers not starting:
Symptoms: Containers exit or application is unreachable.  
Fix:
```
docker-compose logs
```

### Frontend Loads but Backend Fails
Symptoms: UI loads, API endpoints fail.  
Fix:
```
docker-compose logs backend
docker-compose restart backend
```

### Health check failing:
Symptoms: Jenkins pipeline fails at /health check.  
Fix:
```
curl http://localhost:5000/health
```
Ensure Flask binds to 0.0.0.0 and backend container is running.

### Database Connection Errors
Symptoms: Backend crashes with DB errors.  
Fix:
```
docker-compose logs db
docker-compose restart db
```
Verify database environment variables.

### GitHub Webhook Not Triggering Build
Symptoms: Push does not start Jenkins job.  
Fix:
Verify webhook URL ends with /github-webhook/ and Jenkins is publicly reachable (ngrok if local).

### Trivy Scan Fails Pipeline
Symptoms: Pipeline stops at security scan.  
Fix:
Update base images or dependencies. Failure is expected for HIGH/CRITICAL vulnerabilities.

### Old image still running:
Symptoms: Latest changes not reflected.  
Fix:
```
docker-compose down
docker-compose pull
docker-compose up -d
```
### Jenkins Docker permission issue

Ensure Jenkins has access to Docker:
```
-v /var/run/docker.sock:/var/run/docker.sock
```

-----------------------------------------------------------------------------------

## 20.Conclusion

This capstone project successfully demonstrates the design and implementation of a complete CI/CD pipeline using Docker and Jenkins for a containerized web application. The solution automates the entire workflow from code commit to deployment, ensuring consistency, reliability, and repeatability across development, staging, and production environments.

By integrating real webhook-based Continuous Integration, multi-stage Docker image optimization, automated security scanning, and controlled production deployments with manual approval, the project reflects industry-standard DevOps practices. The working frontend–backend–database integration further validates the correctness of the deployment and the effectiveness of the pipeline.

Overall, the project shows end-to-end demonstration of modern CI/CD concepts suitable for real-world applications.

-----------------------------------------------------------------------------------

## Author
**Sandu Pavan Kumar**  
GitHub: [@PavanSPK](https://github.com/PavanSPK) 

