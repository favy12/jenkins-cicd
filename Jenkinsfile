pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Linting') {
            steps {
                sh '''
                source venv/bin/activate
                flake8 main.py test_main.py
                '''
            }
        }
        stage('Testing') {
            steps {
                sh '''
                source venv/bin/activate
                pytest --junitxml=report.xml
                '''
            }
        }
    }
    post {
        always {
            junit 'report.xml'
        }
    }
}
