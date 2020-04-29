from Character import Character

becky = Character("Characters/becky.json")
becky.print_data()
print(becky.delete_value("Penis"))
becky.print_data()