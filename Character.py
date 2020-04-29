import json


class Character:
    def __init__(self, character_file, file_type="json"):
        if file_type == "json":
            self.data = None
            self.character_file = character_file
            self.import_json(character_file)

    def import_json(self, character_json_file):
        with open(character_json_file) as f:
            self.data = json.load(f)

    def save_json(self, character_json_file):
        with open(character_json_file, 'w') as f:
            json.dump(self.data, f)

    def add_value(self, key, value):
        if key in self.data.keys():
            return False
        else:
            self.data[key] = value

    def delete_value(self, key):
        if key not in self.data.keys():
            return False
        else:
            del self.data[key]

    def print_data(self):
        print(self.data)
        print(type(self.data))
