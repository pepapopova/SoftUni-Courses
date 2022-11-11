from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_PER_BREATHE = 15

    def __init__(self, name: str, oxygen=90):
        super().__init__(name, oxygen)

    def breathe(self):
        pass
