pipeline {
    agent { label 'radwan-jenkins-pipeline' }

    stages {
        stage('build') {
            steps {
                script {
                    echo "Build"
                    withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]){
                        sh '''
                            docker build -t grocery_flask_app -f App_dockerfile .
                            docker login -u $dockerHubUser -p $dockerHubPassword
                            docker tag grocery_flask_app:latest radwanmaazon/grocery_flask_app:${BUILD_NUMBER}
                            docker push radwanmaazon/grocery_flask_app:${BUILD_NUMBER}
                        '''
                    }                    
                }
            }
        }
    }
}
