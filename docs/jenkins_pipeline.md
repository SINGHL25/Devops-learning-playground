

**`jenkins_pipeline.md`**
```markdown
# Jenkins Pipeline Examples

Declarative pipeline:
```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building project'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests'
            }
        }
    }
}
