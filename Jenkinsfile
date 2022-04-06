pipeline {
  agent any

  stages {
    stage('Cloning the Spartan Project for GitHub'){
      steps {
        git branch: 'main',
        url: 'https://github.com/d-ungureanu/spartan_project_vagrant.git'
      }
    }

    stage('Build Docker image') {
      steps {
        script {
          DOCKER_IMAGE = docker.build 'leiungureanu/spartan_project_vagrant'
        }
      }
    }

    stage('Push to Docker Hub'){
      steps {
          script {
            docker.withRegistry('', 'docker_hub_cred'){
              DOCKER_IMAGE.push()
            }
          }
      }
    }
  }
}
