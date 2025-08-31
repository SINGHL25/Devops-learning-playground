
import yaml

def load_yaml(file_path):
    """Load YAML configuration."""
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    return data
