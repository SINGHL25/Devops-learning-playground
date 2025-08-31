
# Ansible Guide

<img width="2048" height="2048" alt="Gemini_Generated_Image_z36rdbz36rdbz36r" src="https://github.com/user-attachments/assets/012f15e9-3886-4a8c-a43c-4b76f7dabff9" />


- YAML playbooks
- Roles and tasks
- Example:
```yaml
- hosts: localhost
  tasks:
    - name: Install Apache
      apt:
        name: apache2
        state: present
