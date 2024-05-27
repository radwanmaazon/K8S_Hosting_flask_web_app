pipeline {
    agent { label 'radwan-jenkins-pipeline' }

    stages {
        stage('build') {
            steps {
                script {
                    sh '''
                        echo 'Hello World'
                        docker ps 
                    '''
                }
            }
        }
    }
}
