import os
import json

class ConfigHandler:
    def __init__(self):
        self.avatar_config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "avatar_config.json")
        self.training_config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "training_config.json") # NOT USED

    def read_avatar_config(self):
        with open(self.avatar_config_file, "r") as f:
            config = json.load(f)
        return config
    
    def get_narrarator_config(self, id):
        config = self.read_avatar_config()
        for narrator in config['narrarator']:
            if narrator['id'] == id:
                return narrator
        else:
            raise Exception(f"Narrator with ID {id} is not fount in config ({self.config_file}).")
    
    def get_character_config(self, id):
        config = self.read_avatar_config()
        for character in config['characters']:
            if character['id'] == id:
                return character
        else:
            raise Exception(f"Character with ID {id} is not fount in config ({self.config_file}).")
    
    def get_all_character_config(self):
        return self.read_avatar_config()['characters']
            
            
if __name__ == "__main__":
    c = ConfigHandler()
    print(c.get_character_config("C1"))