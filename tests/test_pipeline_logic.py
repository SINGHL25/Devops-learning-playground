
from src.jenkins_pipeline import simulate_pipeline

def test_pipeline():
    result = simulate_pipeline("Sample Pipeline")
    assert result["status"] == "success"
