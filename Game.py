import json


class Game:
    def __init__(self, game_file, starting_scene, file_type="json"):
        self.data = None
        self.starting_scene = starting_scene
        if file_type == "json":
            self.import_json(game_file)
            self.game_file = game_file

    def start(self):
        if self.data is not None:
            if self.starting_scene in self.data.keys():
                print(self.data[self.starting_scene]["onenter"])
                return True
        else:
            return False

    def import_json(self, game_json_file):
        with open(game_json_file) as f:
            self.data = json.load(f)
