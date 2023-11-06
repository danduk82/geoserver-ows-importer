from configparser import ConfigParser


class ScriptConfiguration():
    def __init__(self, configFile = 'config.ini') -> None:
        # parse the config file
        self.configParser = ConfigParser()
        self.configParser.read(configFile)

