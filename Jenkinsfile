pipeline {
    agent any

    stages {
        stage('Git repository cloning') {
            steps {
                git branch: 'main', url: 'https://github.com/bgdnchrkschnk/Hillel_200226.git'
            }
        }
        stage('Setting up environment dependencies') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y python3 python3-dev python3-pip python3-venv
                    rm -rf .venv
                '''
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Install playwright') {
            steps {
                sh '''
                    . .venv/bin/activate
                    playwright install --with-deps chromium
                '''
            }
        }
        stage('Run tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest -m regression --alluredir=allure-results
                '''
            }
        }
    }
    post {
        always {
            allure includeProperties: false, jdk: '', commandline: 'allure', results: [[path: 'allure-results']]
        }
    }
}