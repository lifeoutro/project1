pipeline{
    agent none
    environment{
        PROJECT_NAME = 'my project'
        OWNER = 'VS'
    }
    stages{
        stage('build'){
            agent { dockerfile true}
            steps{
                sh "ls -la /opt/project2"
                sh "python --version"
            }
        }
        stage('deploy'){
            steps{
                echo "projectname is $PROJECT_NAME"
                echo "owner is $OWNER"
                sleep 3
            }
        }
        stage('End'){
            steps{
            echo "complete"
            }
        }
    }
}