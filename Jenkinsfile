pipeline {

    agent any

    environment {
        REACT_APP_BACKEND_URL = 'http://my-personal-backend-test:8000'
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

        stage('Build Backend Image') {
            steps {
                sh '''
                    echo "Building backend Docker image..."

                    docker build -t my-personal-backend:latest ./backend
                '''
            }
        }

        stage('Start Test Environment') {
            steps {
                sh '''
                    echo "Starting MongoDB..."

                    docker rm -f my-personal-mongodb-test 2>/dev/null || true

                    docker run -d \
                        --name my-personal-mongodb-test \
                        --network jenkins \
                        mongo:7

                    echo "Starting backend..."

                    docker rm -f my-personal-backend-test 2>/dev/null || true

                    docker run -d \
                        --name my-personal-backend-test \
                        --network jenkins \
                        -e MONGO_URL=mongodb://my-personal-mongodb-test:27017 \
                        -e DB_NAME=my_personal \
                        my-personal-backend:latest

                    echo "Waiting for backend to start..."

                    sleep 10

                    docker ps
                '''
            }
        }

        stage('Backend Tests') {
            steps {
                sh '''
                    echo "Running backend tests..."

                    python3 -m venv backend/venv

                    backend/venv/bin/pip install -r backend/requirements.txt

                    REACT_APP_BACKEND_URL=http://my-personal-backend-test:8000 \
                    backend/venv/bin/pytest backend/tests
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
                    echo "Building final backend image..."

                    docker build -t my-personal-backend:latest ./backend

                    echo "Building final frontend image..."

                    docker build -t my-personal-frontend:latest ./frontend
                '''
            }
        }
    }

    post {

        always {
            echo 'Cleaning up test containers...'

            sh '''
                docker rm -f my-personal-backend-test 2>/dev/null || true
                docker rm -f my-personal-mongodb-test 2>/dev/null || true
            '''

            echo 'Pipeline execution completed.'
        }

        success {
            echo '========================================'
            echo '      CI PIPELINE SUCCESSFUL!           '
            echo '========================================'
        }

        failure {
            echo '========================================'
            echo '         CI PIPELINE FAILED!            '
            echo '========================================'
        }
    }
}
