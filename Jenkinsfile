pipeline {
    agent any

    stages {
        stage('Hello') {
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
