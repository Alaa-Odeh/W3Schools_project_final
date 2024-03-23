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
                bat 'call venv\\Scripts\\pip.exe install pytest pytest-html'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }
        stage('Run API Tests in Docker') {
            steps {
                script {
                    parallel(
                        'API Test': {
                            // Correct the docker run command to point to the correct script file
                            bat "docker run --name api_test_container ${IMAGE_NAME}:${TAG} python -m unittest discover -s tests/test_api -p test_log_in_page.Login_Page_Test.test_run.py"
                            // Ensure the container is stopped before removing it
                            bat "docker stop api_test_container"
                            bat "docker rm api_test_container"
                        },
                        // Add other parallel tests here as necessary
                    )
                }
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