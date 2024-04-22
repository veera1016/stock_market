pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'veera1016/my-app-2.0'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}")
                }
            }
        }

       stage('push Docker Image') {
            steps {
                script {
                withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhubpwd')]) {
                sh 'docker login -u veera1016 -p ${dockerhubpwd}'
                sh 'docker push veera1016/my-app-2.0'
            }
        }
      }
    }
  }
}
