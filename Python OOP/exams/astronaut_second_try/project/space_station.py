from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    SUCCESSFULL_MISSIONS = 0
    FAILED_MISSIONS = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")
        astronaut = self.__create_astronaut_by_type(astronaut_type, name)
        if astronaut in self.astronaut_repository.astronauts:
            return f"{astronaut.name} is already added."
        self.astronaut_repository.astronauts.append(astronaut)
        return f"Successfully added {astronaut_type}: {astronaut.name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet in self.planet_repository.planets:
            return f"{name} is already added."
        new_planet = PlanetRepository.add_planet(name)
        new_planet.items.extend = items.split(", ")
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self,name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        most_suitable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30][:5]
        if len(most_suitable_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")
        sorted_astronauts = sorted(most_suitable_astronauts,key= lambda a: -a.oxygen)
        participated_astronauts = 0
        for astronaut in sorted_astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_astronauts +=1

        if len(planet.items) == 0:
            self.SUCCESSFULL_MISSIONS += 1
            return f"Planet: {planet.name} was explored. {participated_astronauts} astronauts participated in collecting items."
        else:
            self.FAILED_MISSIONS += 1
            return "Mission is not completed."

    def report(self):
        result = f"{self.SUCCESSFULL_MISSIONS} successful missions!\n{self.FAILED_MISSIONS} missions were not completed!\n" \
                 f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n" \
                      f"Oxygen: {astronaut.oxygen}\n" \
                      f"Backpack items: {', '.join(astronaut.items) if len(astronaut.items) > 0 else 'none'}\n"
        return result.strip()


    @staticmethod
    def __create_astronaut_by_type(astronaut_type, name):
        if astronaut_type == "Biologist":
            return Biologist(name)
        elif astronaut_type == "Geodesist":
            return Geodesist(name)
        elif astronaut_type == "Meteorologist":
            return Meteorologist(name)

    def __find_planet_by_name(self, name):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return planet