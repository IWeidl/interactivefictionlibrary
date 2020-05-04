import Utilities
from Characters import Characters


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
                print(self.data[self.current_scene]["onenter"])
                self.show_choices()
                self.set_current_scene(self.read_choices())
                self.start()
                return True
        else:
            return False

    def show_choices(self):
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
            return current_choice["pointer"]
        else:
            return False

    def set_current_scene(self, new_scene):
        self.current_scene = new_scene
        self.set_current_choices()

    def set_current_choices(self):
        self.current_choices = list(self.data[self.current_scene]["choices"].items())
