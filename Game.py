import json

import xmltodict
import Utilities
from Characters import Characters


class Game:
    def __init__(self, scene_file, starting_scene, character_file, file_type="json"):
        self.data = Utilities.import_file(scene_file, file_type, "scenes")
        self.scene_file = scene_file
        self.current_scene = starting_scene
        self.current_characters = list(self.data[self.current_scene]["characters"].items())
        self.current_choices = list(self.data[self.current_scene]["choices"].items())
        characters = Characters(character_file,  file_type)

    def start(self):
        if self.data is not None:
            if self.current_scene in self.data.keys():
                print(self.data[self.current_scene]["onenter"])
                self.show_choices()
                self.set_current_scene(self.read_choices())
                self.show_characters()
                self.start()
                return True
        else:
            return False

    def show_choices(self):
        count = 1
        for att, val in self.current_choices:
            print(count, val["text"])
            count += 1

    def show_characters(self):
        print("Current Characters:")
        for att, val in self.current_characters:
            print(val["name"])

    def read_choices(self):
        user_input = input("Enter input: ")
        if 0 <= int(user_input) < len(self.current_choices) + 1:
            return self.current_choices[int(user_input) - 1][1]["pointer"]
        else:
            return False

    def set_current_scene(self, new_scene):
        self.current_scene = new_scene
        self.set_current_choices()
        self.set_current_characters()

    def set_current_choices(self):
        self.current_choices = list(self.data[self.current_scene]["choices"].items())

    def set_current_characters(self):
        self.current_characters = list(self.data[self.current_scene]["characters"].items())
