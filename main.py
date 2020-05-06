from Game import Game
from Characters import Characters

game = Game("scenes.json", "ship_bridge", "characters.json")
print(game.process_string("{{name}} walks onto the Bridge and take command."))
