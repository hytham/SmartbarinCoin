"""
Load and save the configuration, this is a read only operation that will only allow dumping a
json file
"""
import json

class ConfigurationManager:
    def __init__(self,config_filepath="config.json"):
        with open(config_filepath) as fn:
            self.configs = json.load(fn)

    def get(self,name):
        return self.configs[name]