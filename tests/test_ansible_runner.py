
from src.ansible_runner import run_playbook

def test_playbook():
    result = run_playbook("examples/ansible_playbooks/setup_server.yml")
    assert result["status"] == "success"
