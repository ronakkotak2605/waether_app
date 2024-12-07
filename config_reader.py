import os
from configparser import ConfigParser
import logging

logger = logging.getLogger(__name__)

class ConfigReader:
    def __init__(self, config_file="config.cfg"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_file = os.path.join(base_dir, config_file)
        self.config = ConfigParser()
        self.config.read(self.config_file)
        logger.info(f"Config file loaded: {self.config_file}")

    def get(self, section, key):
        try:
            value = self.config[section][key]
            logger.debug(f"Retrieved [{section}] {key}: {value}")
            return value
        except KeyError as e:
            logger.error(f"Error in config: {e}")
            return None

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    reader = ConfigReader()
    print(reader.get("API", "base_url"))
    print(reader.get("API", "api_key"))