import os
import yaml

class ConfigHandler:
    def __init__(self):
        self.config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "config.yml")
        
        self.gpt_organization_key   = None
        self.gpt_api_key            = None
        self.gpt_engine             = None
    
    def read_config(self):
        with open(self.config_file, "r") as f:
            config = yaml.safe_load(f)
            
            # GPT Configurations
            gpt_config = config["gpt"]
            self.gpt_organization_key   = gpt_config["organization-key"]
            self.gpt_api_key            = gpt_config["api-key"]
            self.gpt_engine             = gpt_config["engine"]