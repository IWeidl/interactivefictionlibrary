import json

import xmltodict
import Utilities


class Characters:
    def __init__(self, character_file, file_type="json"):
        self.data = Utilities.import_file(character_file, file_type)
        self.character_file = character_file
        self.file_type = file_type

    def save(self):
        if self.file_type == "json":
            self.save_json(self.character_file)

    def save_json(self, character_json_file):
        with open(character_json_file, 'w') as f:
            json.dump(self.data, f, indent=4)

    def mod_value(self, char, key, value):
        try:
            self.data[char][key] = value
            return True
        except KeyError:
            print(f'DEBUG ERROR: KEY: [{char}][{key}] NOT FOUND')
            return False

    def del_key(self, char, key):
        try:
            del self.data[char][key]
            return True
        except KeyError:
            print(f'DEBUG ERROR: KEY: [{char}][{key}] NOT FOUND')
            return False

    def get_value(self, char, key):
        try:
            return self.data[char][key]
        except KeyError:
            print(f'DEBUG ERROR: KEY: [{char}][{key}] NOT FOUND')

    def print_data(self):
        for char in self.data:
            print(self.data[char])
