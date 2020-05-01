import json

import xmltodict


class Game:
    def __init__(self, scene_file, starting_scene, file_type="json"):
        self.data = None
        self.scene_file = scene_file
        self.current_scene = starting_scene
        self.import_file(scene_file, file_type)
        self.current_choices = list(self.data[self.current_scene]["choices"].items())

    def start(self):
        if self.data is not None:
            if self.current_scene in self.data.keys():
                print(self.data[self.current_scene]["onenter"])
                self.show_choices()
                self.set_current_scene(self.read_choices())
                self.start()
                return True
        else:
            return False

    def show_choices(self):
        count = 1
        for att, val in self.current_choices:
            print(count, val["text"])
            count += 1

    def read_choices(self):
        user_input = input("Enter input: ")
        if 0 <= int(user_input) < len(self.current_choices) + 1:
            return self.current_choices[int(user_input) - 1][1]["pointer"]
        else:
            return False

    def import_file(self, scene_file, file_type="json"):
        if file_type == "json":
            with open(scene_file) as f:
                self.data = json.load(f)
        elif file_type == "xml":
            with open(scene_file) as f:
                self.data = xmltodict.parse(f.read())["scenes"]
        self.scene_file = scene_file

    def set_current_scene(self, new_scene):
        self.current_scene = new_scene
        self.set_current_choices()

    def set_current_choices(self):
        self.current_choices = list(self.data[self.current_scene]["choices"].items())
