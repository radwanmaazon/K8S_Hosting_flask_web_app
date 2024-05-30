pipeline {
    agent { label 'radwan-jenkins-pipeline' }
    parameters {
        choise {name:'Env' ,choises [ 'dev', 'test', 'main', "rebase"]}
    }
    stages {
        stage('build') {
            steps {
                script {
                    echo "Build"
                    if (params.Env == "rebase"){
                        withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]){
                        sh '''
                            docker build -t grocery_flask_app -f App_dockerfile .
                            docker login -u $dockerHubUser -p $dockerHubPassword
                            docker tag grocery_flask_app:latest radwanmaazon/grocery_flask_app:${BUILD_NUMBER}.0
                            docker push radwanmaazon/grocery_flask_app:${BUILD_NUMBER}.0
                            echo ${BUILD_NUMBER}.0 > ../buildnumber.txt
                        '''
                        }
                    }                                        
                }
            }
        }
        stage ('deploy'){
            steps{
                script {
                    echo ('deploy')
                    if (params.Env == 'dev' || params.Env == 'test' || params.Env == 'test'){
                        withCredentials([file(credentialsId: 'flask_app_cred', variable: 'secretFile')]){
                        sh """
                            export BUILD_NUMBER=\$(cat ../buildnumber.txt)
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
}
