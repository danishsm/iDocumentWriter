import configparser

class UIConfigLoader():
    def __init__(self,path):
        self.config = configparser.ConfigParser()
        self.config.read(path)


    def get_config_values(self,section,key):
        return self.config[section][key]