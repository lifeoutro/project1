pipeline{
    agent any
    environment{
        PROJECT_NAME = 'my project'
        OWNER = 'VS'
    }
    stages{
        stage('build'){
            steps{
                echo "line 1"
                echo "line 2"
                echo "line 3"
            }
        }
        stage('deploy'){
            steps{
                echo "projectname is $(PROJECT_NAME)"
                echo "owner is $(OWNER)"
            }

        }
    }
}