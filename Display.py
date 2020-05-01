
import Scene as Scene


class Display:

    def __init__(self, starting_scene):
        self.window = None
        self.layout = [
            [sg.Text(starting_scene.data["onenter"])]
        ]

    def start(self, x, y):
        self.window = sg.Window("IFL", self.layout, size=(x, y))

        while True:
            event, values = self.window.read()
            print(event, values)
            if event in (None, 'Exit'):
                break
