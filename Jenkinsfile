pipeline {
    agent any

    environment {
        // Docker Hub credentials (store these in Jenkins credentials)
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
        DOCKER_IMAGE = "naman1301/scientific-calculator:latest"
        SUDO_PASSWORD = credentials('sudo-password')
    }

    stages {
        // Stage 1: Pull code from GitHub
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/davenaman13/scientific-calculator.git'
            }
        }

        // Stage 2: Run unit tests
        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        // Stage 3: Build Docker image
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        // Stage 4: Push Docker image to Docker Hub
        stage('Push Docker Image') {
            steps {
                script {
                    // Log in to Docker Hub
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        // Push the Docker image
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }

        // Stage 5: Deploy using Ansible
        stage('Deploy with Ansible') {
            steps {
                // Run the Ansible playbook
                ansiblePlaybook(
                    playbook: 'ansible/deploy.yml',
                    inventory: 'ansible/inventory',
                    extraVars: [
                        sudo_password: "${SUDO_PASSWORD}"
                    ]
                )
            }
        }
    }

    post {
        // Actions to perform after the pipeline completes
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
