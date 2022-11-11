from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautSpecialists:
    astrounaut_spec = {
        'Biologist': Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def find_astronaut(self, astronaut_specialist, name):
        if astronaut_specialist not in self.astrounaut_spec:
            raise Exception("Astronaut type is not valid!")
        return self.astrounaut_spec[astronaut_specialist](name)

