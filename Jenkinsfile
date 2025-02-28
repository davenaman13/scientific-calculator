pipeline {
    agent any

    environment {
        // Docker Hub credentials (store these in Jenkins credentials)
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
        DOCKER_IMAGE = "naman1301/scientific-calculator:latest"
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
                    sh 'docker build -t naman1301/scientific-calculator .'
                }
            }
        }

        // Stage 4: Push Docker image to Docker Hub
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
			docker.image("${DOCKER_IMAGE}").push()                     
                    }
                }
            }
        }

//Resolved Ansible playbook execution failure in Jenkins pipeline
// corrected the directory structure for stage:5

 
       // Stage 5: Deploy using Ansible
        stage('Deploy with Ansible') {
            steps {
                ansiblePlaybook(
                    playbook: 'ansible/deploy.yml',
                    inventory: 'ansible/inventory',
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
