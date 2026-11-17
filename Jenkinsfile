pipeline {
    agent any

    environment {
        // Замініть на свій логін на Docker Hub
        DOCKER_USER = 'ваш_dockerhub_username'
        IMAGE_NAME = 'my-test-app'
    }

    stages {
        stage('Check SCM') {
            steps {
                checkout scm
                echo "Код успішно завантажено з GitHub"
            }
        }

        stage('Build Application') {
            steps {
                echo "Збірка додатка номер: ${BUILD_NUMBER}"
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Збірка Docker-образу з використанням локального Dockerfile у репозиторії
                    dockerImage = docker.build("${DOCKER_USER}/${IMAGE_NAME}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Використання credentials, збережених у Jenkins
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        dockerImage.push("${BUILD_NUMBER}")
                        dockerImage.push("latest")
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Конвеєр завершив роботу."
        }
        success {
            echo "Образ успішно зібрано та відправлено на Docker Hub!"
        }
        failure {
            echo "Помилка при виконанні конвеєра."
        }
    }
}