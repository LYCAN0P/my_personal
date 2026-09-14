pipeline {

    agent any
    
    environment {
        REACT_APP_BACKEND_URL = 'http://localhost:8000'
    }

    
    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Tools') {
            steps {
                sh '''
                    echo "Checking installed tools..."

                    git --version
                    python3 --version
                    pip3 --version
                    node --version
                    npm --version
                    docker --version
                '''
            }
        }

        stage('Backend Tests') {
            steps {
                sh '''
                    cd backend

                    echo "Creating Python virtual environment..."
                    python3 -m venv venv

                    echo "Installing backend dependencies..."
                    ./venv/bin/pip install -r requirements.txt

                    echo "Running backend tests..."
                    ./venv/bin/pytest
                '''
            }
        }

        stage('Frontend Build') {
            steps {
                sh '''
                    cd frontend

                    echo "Installing frontend dependencies..."
                    npm install --legacy-peer-deps

                    echo "Building frontend..."
                    npm run build
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    echo "Building backend Docker image..."
                    docker build -t my-personal-backend:latest ./backend

                    echo "Building frontend Docker image..."
                    docker build -t my-personal-frontend:latest ./frontend
                '''
            }
        }

    }

    post {

        success {
            echo '========================================'
            echo '      CI PIPELINE SUCCESSFUL!           '
            echo '========================================'
        }

        failure {
            echo '========================================'
            echo '         CI PIPELINE FAILED!             '
            echo 'Check the stage above for the error.'
            echo '========================================'
        }

        always {
            echo 'Pipeline execution completed.'
        }
    }
}
