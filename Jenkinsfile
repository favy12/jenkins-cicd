pipeline { 
    agent any

    environment {
        VENV_PATH = 'venv'
        PYTHON_CMD = 'python3'
        PIP_CMD = './venv/bin/pip'
        FLAKE8_CMD = './venv/bin/flake8'
        PYTEST_CMD = './venv/bin/pytest'
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    sh """
                    ${PYTHON_CMD} -m venv ${VENV_PATH}
                    . ${VENV_PATH}/bin/activate
                    ${PIP_CMD} install --upgrade pip
                    """
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh """
                    . ${VENV_PATH}/bin/activate
                    ${PIP_CMD} install -r requirements.txt
                    """
                }
            }
        }

        stage('Linting') {
            steps {
                script {
                    sh """
                    . ${VENV_PATH}/bin/activate
                    ${FLAKE8_CMD} main.py test_main.py
                    """
                }
            }
        }

        stage('Testing') {
            steps {
                script {
                    sh """
                    . ${VENV_PATH}/bin/activate
                    ${PYTEST_CMD} --junitxml=report.xml
                    """
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    sh """
                    . ${VENV_PATH}/bin/activate
                    nohup ${PYTHON_CMD} main.py --host=0.0.0.0 --port=${APP_PORT} &
                    """
                }
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
    }
}
