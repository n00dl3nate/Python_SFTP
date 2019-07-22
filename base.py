import configparser
from pathlib import Path

class Configuration:
    file_name = 'config.ini'

    def __init__(self):
        self.file_path = [str(path) for path in Path('./').iterdir() if path.name == self.file_name][0]

    def get_raw_configuration_for(self, section, option):
        config = configparser.RawConfigParser()
        config.read(self.file_path)
        return config.get(section, option)

    def get_configuration_for(self, section, option):
        config = configparser.ConfigParser()
        config.read(self.file_path)
        return config.get(section, option)
