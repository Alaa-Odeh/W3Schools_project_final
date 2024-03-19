pipeline {
    agent any
    environment {
        PYTHON_PATH = "C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        PIP_PATH = '"C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe"'
        TEST_REPORTS = 'test-reports'
    }
    stages {
        stage('Setup Environment') {
            steps {
                bat 'call "%PYTHON_PATH%" -m venv venv'
                bat 'call venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'call venv\\Scripts\\pip.exe install -r requirements.txt'
                bat 'call venv\\Scripts\\pip.exe install pytest pytest-html'
            }
        }
        stage('Run API Tests with Pytest') {
            steps {
                script {
                    try {
                        bat 'call venv\\Scripts\\python.exe -m pytest tests/test_api/api_test_runner.py --html=${TEST_REPORTS}\\report.html --self-contained-html'
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: "${TEST_REPORTS}/*.html", allowEmptyArchive: true
        }
    }
}