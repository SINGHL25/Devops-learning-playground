
from src.chef_runner import run_recipe

def test_recipe():
    result = run_recipe("examples/chef_cookbooks/default.rb")
    assert result["status"] == "success"
