

**`jenkins_pipeline.md`**
<img width="2048" height="2048" alt="Gemini_Generated_Image_kbx5ahkbx5ahkbx5" src="https://github.com/user-attachments/assets/cc1bc1ea-11ef-4591-bc86-f873ec40e640" />


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
