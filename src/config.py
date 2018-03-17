import yaml
from pathlib import Path


def config():
    config_file = Path('config.yml')
    if config_file.is_file():
        with config_file.open() as ymlfile:
            config = yaml.safe_load(ymlfile)
            return config
    else:
        raise FileNotFoundError("{} not found".format(config_file))