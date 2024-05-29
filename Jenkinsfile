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
                        '''
                    }                    
                }
            }
        }
        stage ('deploy'){
            steps{
                script {
                    echo ('deploy')
                    withCredentials([file(credentialsId: 'flask_app_cred', variable: 'secretFile')]){
                        sh """
                            cp Deployment/application.yml Deployment/application.yml.temp
                            cat Deployment/application.yml.temp | envsubst > Deployment/application.yml 
                            rm Deployment/application.yml.temp 
                            kubectl apply -f Deployment --kubeconfig=${secretFile}
                        """
                    }
                }                
            }
        }
    }
}
