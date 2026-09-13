pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Backend Tests') {
            steps {
                sh '''
                    cd backend
                    pip install -r requirements.txt
                    pytest
                '''
            }
        }

        stage('Frontend Build') {
            steps {
                sh '''
                    cd frontend
                    npm install --legacy-peer-deps
                    npm run build
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t my-personal-backend ./backend
                    docker build -t my-personal-frontend ./frontend
                '''
            }
        }
    }
}
