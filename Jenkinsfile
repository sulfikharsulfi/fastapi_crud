pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'new-fastapi-crud2'
        DOCKER_TAG = 'latest'
        REPO_URL = 'https://github.com/sulfikharsulfi/fastapi_crud.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    echo "Cloning repository from ${REPO_URL}"
                }
                git branch: 'master', url: "${REPO_URL}"
                script {
                    echo "Repository cloned successfully."
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    def customImage = docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                    echo "Docker image ${DOCKER_IMAGE}:${DOCKER_TAG} built successfully."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // echo "Stopping and removing any existing container named fastapi_crud"
                    // bat '''
                    // for /f "tokens=*" %i in ('docker ps -q --filter "name=fastapi_crud"') do @docker stop %i
                    // for /f "tokens=*" %i in ('docker ps -aq --filter "name=fastapi_crud"') do @docker rm %i
                    // '''
                    // echo "Existing container stopped and removed (if any)."
                    
                    echo "Running new Docker container ${DOCKER_IMAGE}:${DOCKER_TAG}"
                    bat """
                    docker run -d --name new-fastapi-crud2 -p 8000:8000 ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                    echo "Docker container ${DOCKER_IMAGE}:${DOCKER_TAG} is now running."
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning workspace..."
            cleanWs()
            echo "Workspace cleaned."
        }
    }
}