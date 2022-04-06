pipeline {
  agent any

  environment {
    IMAGE_NAME = 'leiungureanu/spartan_project_vagrant:1.' + "$BUILD_NUMBER"
    DOCKER_CREDENTIALS = 'docker_hub_cred'
  }

  stages {
    stage('Cloning the Spartan Project for GitHub'){
      steps {
        checkout([
          $class: 'GitSCM', branches: [[name: '*/main']],
          userRemoteConfigs: [[
            url: 'git@github.com:d-ungureanu/spartan_project_vagrant.git',
            credentialsId: 'ssh_git_cred'
          ]]
        ])
      }
    }

    stage('Build Docker image') {
      steps {
        script {
          DOCKER_IMAGE = docker.build IMAGE_NAME
        }
      }
    }

    stage('Push to Docker Hub'){
      steps {
          script {
            docker.withRegistry('', DOCKER_CREDENTIALS){
              DOCKER_IMAGE.push()
            }
          }
      }
    }

    stage('Removing the docker image') {
      steps {
        sh 'docker rmi $IMAGE_NAME'
      }
    }
  }
}
