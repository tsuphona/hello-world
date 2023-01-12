pipeline {
  agent any
  stages {
    stage('Checkout Code') {
      steps {
        git(url: 'https://github.com/tsuphona/hello-world.git', branch: 'develop')
      }
    }

    stage('') {
      steps {
        sh 'ls -la'
      }
    }

  }
}