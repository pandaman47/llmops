import yaml
import os


def load_config(config_path: str = "config/config.yaml") -> dict:
    """Load configuration from a YAML file.

    Args:
        config_path (str): The path to the YAML configuration file.

    Returns:
        dict: The configuration data as a dictionary.
    """
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        print(config)
    return config

