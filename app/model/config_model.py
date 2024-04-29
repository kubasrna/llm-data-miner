"""ConfigModel"""
import yaml
from easydict import EasyDict


class ConfigModel:
    """COnfig model is class containing storage update and safe of application configuration"""

    def __init__(self) -> None:
        self.config = None

    def load_config(self) -> None:
        """ function loads config from the config file

        Returns:
            dict: all configuration found in config file
        """
        with open('config/config.yml', 'r', encoding='utf8') as ymlfile:
            self.config = EasyDict(yaml.safe_load(ymlfile))

    def update_config(self, key: str, value: str) -> None:
        """update config is function responsible for updating internal configuration

        Args:
            key (str): parameter key
            value (str): parameter new value
        """
        if key in self.config:
            self.config[key] = value

    def save_config(self) -> None:
        """saves the config either upon shutdown or when user requests change through ui"""
        with open('config/config.yml', 'w', encoding='utf8') as ymlfile:
            yaml.dump(dict(self.config), ymlfile, default_flow_style=False)
