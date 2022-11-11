from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.core.astonaut_types import AstronautSpecialists
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from collections import deque


class SpaceStation:
    SUCCESSFULL_MISSIONS = 0
    FAILED_MISSIONS = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.__find_astronaut_by_type(astronaut_type, name)
        if not astronaut:
            raise Exception("Astronaut type is not valid!")

        if self.__find_astronaut_by_name(name):
            return f"{name} is already added."

        self.astronaut_repository.astronauts.append(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if any(p.name == name for p in self.planet_repository.planets):
            return f"{name} is already added."
        planet = Planet(name)
        self.planet_repository.planets.append(planet)
        item_list = items.split(', ')
        planet.items.extend(item_list)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                self.astronaut_repository.astronauts.remove(astronaut)
                return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.__find_planet_by_name(planet_name)
        if planet is None:
            raise Exception("Invalid planet name!")
        suitable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        top_5 = sorted(suitable_astronauts, key=lambda x: x.oxygen, reverse=True)[:5]
        if len(top_5) < 1:
            raise Exception("You need at least one astronaut to explore the planet!")
        top_5 = deque(top_5)
        participated = 0
        while True:
            if not planet.items:
                self.SUCCESSFULL_MISSIONS += 1
                return f"Planet: {planet_name} was explored. {participated} astronauts participated     in collecting items"
            if not top_5:
                self.FAILED_MISSIONS += 1
                return "Mission is not completed."
            current_astronaut = top_5.popleft()
            participated += 1

            for item in reversed(planet.items):
                current_astronaut.backpack.append(item)
                planet.items.pop(0)
                current_astronaut.breathe()
                if current_astronaut.oxygen <= 0:
                    break

    def report(self):
        result = f"{self.SUCCESSFULL_MISSIONS} successful missions\n{self.FAILED_MISSIONS} missions were not completed!"
        result += "\nAstronauts' info:"
        for astronaut in self.astronaut_repository.astronauts:
            result += f'\n{astronaut.details()}'
        return result

    def __find_astronaut_by_name(self, name):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return astronaut

    @staticmethod
    def __find_astronaut_by_type(astronaut_type, name):
        if astronaut_type == "Geodesist":
            return Geodesist(name)
        elif astronaut_type == "Biologist":
            return Biologist(name)
        elif astronaut_type == "Metereologist":
            return Meteorologist(name)

    def __find_planet_by_name(self, planet_name):
        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                return planet
