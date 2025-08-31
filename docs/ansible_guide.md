
# Ansible Guide

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
