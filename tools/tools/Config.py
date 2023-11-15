from configparser import ConfigParser
import os

class ScriptConfiguration():
    def __init__(self, configFile = 'config.ini', defaultsFile = 'defaults.ini') -> None:
        # parse the config file
        self.configParser = ConfigParser()
        self.configParser.read(configFile)
        # get the default file from the same directory as this script
        self.defaults = ConfigParser()
        self.defaults.read(os.path.join(os.path.dirname(__file__), defaultsFile))

