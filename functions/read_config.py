import json
import os

def read_config():
    """
    Reads the configuration file from the parent directory and returns the configuration as a dictionary.
    """
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    config_path = os.path.join(parent_directory, 'config.json')

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, 'r') as config_file:
        config = json.load(config_file)

    return config.get('api_key', None)
