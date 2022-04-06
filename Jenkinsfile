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
          docker.build 'leiungureanu/spartan_project_vagrant:latest'
        }
      }
    }
  }
}
