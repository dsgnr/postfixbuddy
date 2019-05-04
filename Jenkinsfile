pipeline {
    agent any
    stages {
        stage('Postfixbuddy Python 2.7') {
            parallel {
                stage('Pylint') {
                    agent {
                        docker {
                            image 'dsgnr/base-python2.7-alpine-docker'
                        }
                    }
                    stages {
                        stage('Setup') {
                            steps {
                                echo "Installing requirements..."
                                sh '''pip install -q -U pip
                                      pip install -r requirements.txt'''
                            }
                        }
                        stage('Pylint') {
                            steps {
                                echo "Running Pylint..."
                                sh 'pylint --rcfile=.pylintrc *.py > pylint.log'
                            }
                        }
                    }
                    post {
                        always {
                            recordIssues enabledForFailure: true, tool: pyLint(id: 'postfixbuddy-pylint', name: 'Postfixbuddy PyLint', pattern: 'pylint.log', reportEncoding: 'UTF-8')
                        }
                        failure {
                            sh 'cat pylint.log'
                        }
                    }
                }
                stage('Pycodestyle') {
                    agent {
                        docker {
                            image 'dsgnr/base-python2.7-alpine-docker'
                        }
                    }
                    stages {
                        stage('Setup') {
                            steps {
                                echo "Installing requirements..."
                                sh '''pip install -q -U pip
                                      pip install -r requirements.txt'''
                            }
                        }
                        stage('Pycodestyle') {
                            steps {
                                echo "Running Pycodestyle..."
                                sh 'pycodestyle --config=setup.cfg *.py > pycodestyle.log'
                            }
                        }
                    }
                    post {
                        always {
                            recordIssues enabledForFailure: true, tool: pep8(id: 'postfixbuddy-pycodestyle', name: 'Postfixbuddy Pycodestyle', pattern: 'pycodestyle.log', reportEncoding: 'UTF-8')
                        }
                        failure {
                            sh 'cat pycodestyle.log'
                        }
                    }
                }
            }
        }
        stage('Postfixbuddy Python 3.7') {
            parallel {
                stage('Pylint') {
                    agent {
                        docker {
                            image 'dsgnr/base-python3.7-alpine-docker'
                        }
                    }
                    stages {
                        stage('Setup') {
                            steps {
                                echo "Installing requirements..."
                                sh '''pip3 install -q -U pip
                                      pip3 install -r requirements.txt'''
                            }
                        }
                        stage('Pylint') {
                            steps {
                                echo "Running Pylint..."
                                sh 'pylint --rcfile=.pylintrc *.py > pylint-py3.log'
                            }
                        }
                    }
                    post {
                        always {
                            recordIssues enabledForFailure: true, tool: pyLint(id: 'postfixbuddy-pylint', name: 'Postfixbuddy PyLint Python3', pattern: 'pylint-py3.log', reportEncoding: 'UTF-8')
                        }
                        failure {
                            sh 'cat pylint-py3.log'
                        }
                    }
                }
                stage('Pycodestyle') {
                    agent {
                        docker {
                            image 'dsgnr/base-python3.7-alpine-docker'
                        }
                    }
                    stages {
                        stage('Setup') {
                            steps {
                                echo "Installing requirements..."
                                sh '''pip3 install -q -U pip
                                      pip3 install -r requirements.txt'''
                            }
                        }
                        stage('Pycodestyle') {
                            steps {
                                echo "Running Pycodestyle..."
                                sh 'pycodestyle --config=setup.cfg *.py > pycodestyle-py3.log'
                            }
                        }
                    }
                    post {
                        always {
                            recordIssues enabledForFailure: true, tool: pep8(id: 'postfixbuddy-pycodestyle', name: 'Postfixbuddy Pycodestyle Python3', pattern: 'pycodestyle-py3.log', reportEncoding: 'UTF-8')
                        }
                        failure {
                            sh 'cat pycodestyle-py3.log'
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            deleteDir()
        }
    }
}
