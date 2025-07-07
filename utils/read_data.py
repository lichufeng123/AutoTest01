import os
import yaml


def get_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    yaml_path = os.path.join(current_dir, "../conf/config.yml")
    with open(yaml_path, encoding="utf8") as f:
        return yaml.safe_load(f)
