pipeline {
    agent any
    environment {
        PYTHON_PATH = "C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        PIP_PATH = '"C:\\Users\\Alaa Oda\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\pip.exe"'
        TEST_REPORTS = 'test-reports'
        IMAGE_NAME = 'tests'
        TAG = 'latest'
    }
    stages {
        stage('Setup Environment') {
            steps {
                bat 'call "%PYTHON_PATH%" -m venv venv'
                bat 'call venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'call venv\\Scripts\\pip.exe install -r requirements.txt'
                bat 'call venv\\Scripts\\pip.exe install pytest pytest-html selenium'
            }
        }
        stage('Setup Selenium Server HUB') {
            steps {
                echo 'Setting up Selenium server HUB...'
                bat "start /B java -jar selenium-server.jar hub"
                // Delay for 10 seconds
                bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
            }
        }
        stage('Setup Selenium Server nodes') {
            steps {
                echo 'Setting up Selenium server nodes...'
                bat "start /B java -jar selenium-server.jar node --port 5555 --selenium-manager true"
                // Delay for 10 seconds
                bat 'ping 127.0.0.1 -n 11 > nul' // Windows command to sleep for 10 seconds
            }
        }
        stage('Check Directory and File') {
    steps {
        script {
                // For Windows Batch Command
                bat """
                echo Checking directory...
                dir
                echo Checking if tests_runner.py exists...
                if exist tests/tests_runner.py (
                    echo tests_runner.py exists
                ) else (
                    echo tests_runner.py does not exist
                )
                """
            }
        }
    }


        stage('Run Tests with Pytest') {
            steps {
                script {
                    try {
                        bat 'call venv\\Scripts\\python.exe -m pytest -v tests/tests_runner --html=${TEST_REPORTS}\\report.html --self-contained-html'
                    } catch (Exception e) {
                        echo "Tests failed, but the build continues."
                    }
                }
            }
        }
    }
    post {
        success {
                slackSend(channel: 'C06Q6FRSFKJ',color: "good", message: "Build succeeded")
            }
        failure {
            slackSend(channel: 'C06Q6FRSFKJ',color: "danger", message: "Build failed")
        }
        always {
            archiveArtifacts artifacts: "${TEST_REPORTS}/*.html", allowEmptyArchive: true
            echo 'Cleaning up...'
            // Stop and remove any stray containers that might be using the image
            // Use the correct container names as per the tests run
            bat "docker stop api_test_container || true"
            bat "docker rm api_test_container || true"
            bat "docker stop web_test_container || true"
            bat "docker rm web_test_container || true"
            // Force remove the Docker image, if necessary, to clean up
            bat "docker rmi -f ${IMAGE_NAME}:${TAG}"
        }
    }
}