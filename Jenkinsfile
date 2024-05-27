pipeline {
    agent {'flask-slave'}

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
