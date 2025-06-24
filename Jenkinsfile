pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/IshitaSwami/DemoBlaze_Playwright.git'
            }
        }

        stage('Set up Python & Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    pytest tests/ --maxfail=1 --disable-warnings --tb=short
                '''
            }
        }
    }

    post {
        always {
            junit '**/test-results/*.xml' // If using JUnit XML output
        }
    }
}
