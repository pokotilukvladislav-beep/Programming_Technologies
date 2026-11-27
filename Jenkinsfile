pipeline {
    agent any

    environment {
        IMAGE_NAME = "vladpokotyluk/my-test-app"
        IMAGE_TAG  = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Check SCM') {
            steps {
                checkout scm
                echo 'Код успішно завантажено з GitHub'
            }
        }

        stage('Build Application') {
            steps {
                echo "Збірка додатка номер: ${env.BUILD_NUMBER}"
            }
        }

        stage('Test') {
            steps {
                echo 'Запуск модульних тестів...'
                sh 'docker run --rm -v "${WORKSPACE}":/app -w /app python:3.11-alpine sh -c "pip install --no-cache-dir -r requirements.txt && python -m unittest discover -v"'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Конвеєр завершив роботу.'
        }
        success {
            echo 'Тести пройдено, образ успішно зібрано та завантажено на Docker Hub!'
        }
        failure {
            echo 'Помилка при виконанні конвеєра або провалені тести.'
        }
    }
}
