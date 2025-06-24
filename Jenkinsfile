pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/IshitaSwami/DemoBlaze_Playwright.git'
            }
        }

        stage('Set up Python & Install Dependencies') {
            steps {
                bat '''
                    python -m venv $VENV_DIR
                    source $VENV_DIR/Scripts/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    source $VENV_DIR/Scripts/activate
                    pytest tests/ --maxfail=1 --disable-warnings --tb=short
                '''
            }
        }
    }

    post {
        always {
            junit '**/test-results/*.xml' // Optional: only if you produce JUnit-style XML reports
        }
    }
}
