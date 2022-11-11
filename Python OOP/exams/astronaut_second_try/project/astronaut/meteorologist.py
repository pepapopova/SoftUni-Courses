from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_PER_BREATHE = 15

    def __init__(self, name: str):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= self.OXYGEN_PER_BREATHE