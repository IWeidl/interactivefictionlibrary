import Utilities
from Characters import Characters
import re


class Game:
    def __init__(self, scene_file, starting_scene, character_file, file_type="json"):
        self.data = Utilities.import_file(scene_file, file_type, "scenes")
        self.scene_file = scene_file
        self.current_scene = starting_scene
        self.current_choices = list(self.data[self.current_scene]["choices"].items())
        self.characters = Characters(character_file, file_type)

    # This is our game play loop, must be called after init
    def start(self):
        if self.data is not None:
            if self.current_scene in self.data.keys():
                self.process_scene_text("")
                print(self.data[self.current_scene]["onenter"])
                self.show_choices()
                self.set_current_scene(self.read_choices())
                self.start()
                return True
        else:
            return False

    def show_choices(self, flavor_text=""):
        print(flavor_text)
        count = 1
        for choice_id, choice_contents in self.data[self.current_scene]["choices"].items():
            valid = True
            if "statcheck" in choice_contents:
                for character, stat in choice_contents["statcheck"].items():
                    for stat_id, stat_value in stat.items():
                        if not (self.characters.check_stat(character, stat_id, stat_value)):
                            valid = False
            print(f'{count}: {choice_contents["text"]} === {valid}')
            count += 1

    def read_choices(self):
        user_input = input("Enter input: ")
        if 0 <= int(user_input) < len(self.current_choices) + 1:
            current_choice = self.current_choices[int(user_input) - 1][1]

            # THIS is really disgusting....
            if "statmod" in current_choice:
                for character, stat in current_choice["statmod"].items():
                    for stat_action, stat_id in stat.items():
                        for stat_target, stat_value in stat_id.items():
                            if stat_action == "set":
                                self.characters.mod_value(character, stat_target, stat_value)
                            elif stat_action == "add":
                                if isinstance(stat_value, int):
                                    self.characters.mod_value(character, stat_target, (
                                            self.characters[character][stat_target] + int(stat_value)))
                                else:
                                    print("CAN'T PERFORM ADD OP ON NON INT")
                            elif stat_action == "delete":
                                if self.characters.check_exists(character, stat_target):
                                    self.characters.del_key(character, stat_target)

            self.characters.print_data()
            return current_choice["pointer"]
        else:
            return False

    def set_current_scene(self, new_scene):
        if new_scene in self.data:
            self.current_scene = new_scene
            self.set_current_choices()
        else:
            self.set_current_choices()

    def set_current_choices(self):
        self.current_choices = list(self.data[self.current_scene]["choices"].items())

    def process_scene_text(self, raw_string):
        for variables, variable in self.data[self.current_scene]["variables"].items():
            for variable_1, character in variable.items():
                    print(variable_1, character)
        return raw_string
