pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
        DOCKER_IMAGE = "naman1301/scientific-calculator:latest"
        SUDO_PASSWORD = credentials('sudo-password') // Store sudo password in Jenkins
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/davenaman13/scientific-calculator.git'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                   sh 'docker build -t naman1301/scientific-calculator:latest .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }

        stage('Deploy with Ansible') {
            steps {
                ansiblePlaybook(
                    playbook: 'ansible/deploy.yml',
                    inventory: 'ansible/inventory',
                    credentialsId: 'ansible-ssh-credentials',
                    extraVars: [
                        ansible_become_pass: "${SUDO_PASSWORD}",
                        ansible_verbosity: '-vvv'
                    ]
                )
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
