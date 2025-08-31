
from src.maven_builder import build_maven_project

def test_maven():
    result = build_maven_project("examples/maven_projects")
    assert result["status"] == "success"
