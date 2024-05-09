pipeline {
    environment {
        registryCredential = 'AbdullahDockerCredentials'
        IMAGE_NAME = 'mianabdullah/mlops-assignment1'
        TAG = 'latest' 
    }
    agent any
    stages {
        stage('Cloning Git Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ShahidHameed4/mlops-assignment-02-i200980-i202487'
            }
        }
        stage('Building our image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }
        stage('Deploy our image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        docker.image("${IMAGE_NAME}:${TAG}").push()
                    }
                }
            }
        }
    }
    post {
        success {
            emailext(
                to: 'i202487@nu.edu.pk',
                subject: 'Build Successful ',
                body: 'The docker image successfully pushed to Dockerhub! Well Done!'
            )
        }
    }
}
