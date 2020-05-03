import json

import xmltodict
import Utilities


class Characters:
    def __init__(self, character_file, file_type="json"):
        self.data = Utilities.import_file(character_file, file_type)
        self.character_file = character_file
        
    def save_json(self, character_json_file):
        with open(character_json_file, 'w') as f:
            json.dump(self.data, f)

    def add_value(self, key, value):
        if key in self.data.keys():
            return False
        else:
            self.data[key] = value
            return True

    def delete_value(self, key):
        if key not in self.data.keys():
            return False
        else:
            del self.data[key]
            return True

    def change_value(self, key, value):
        if key not in self.data.keys():
            return False
        else:
            self.data[key] = value
            return True

    def print_data(self):
        for char in self.data:
            print(self.data[char])
