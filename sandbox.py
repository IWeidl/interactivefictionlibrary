from Game import Game
from Characters import Characters

# game = Game("Scenes/main.json", "entry_room", file_type="json")
# game.start()

characters = Characters("characters.json")
print(characters.get_value("becky_1", "job"))
characters.print_data()
characters.save()
