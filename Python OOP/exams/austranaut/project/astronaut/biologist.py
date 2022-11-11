from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_PER_BREATHE = 5

    def __init__(self, name: str, oxygen=70):
        super().__init__(name, oxygen)

    def breathe(self):
        pass
