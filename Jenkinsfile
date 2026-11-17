pipeline {
    agent any

    environment {
        DOCKER_USER = 'vladpokotyluk'
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
                    dockerImage = docker.build("${DOCKER_USER}/${IMAGE_NAME}:${BUILD_NUMBER}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
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