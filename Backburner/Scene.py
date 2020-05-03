import json


class Scene:

    def __init__(self, scene_file, file_type="json"):
        if file_type == "json":
            self.data = None
            self.character_file = scene_file
            self.import_json(scene_file)

    def import_json(self, scene_json_file):
        with open(scene_json_file) as f:
            self.data = json.load(f)

    def save_json(self, scene_json_file):
        with open(scene_json_file, 'w') as f:
            json.dump(self.data, f)

    def run(self):
        print(self.data["onenter"])

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
