from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.fish_factory import FishFactory
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller():
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []
        self.fish_factory = FishFactory()

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        if aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            decoration = Ornament()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        if decoration_type == "Plant":
            decoration = Plant()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."
        return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        self.decorations_repository.remove(decoration)

        aquarium = self.__find_aquarium_by_name(aquarium_name)
        if not aquarium:
            return
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        try:
            fish = self.fish_factory.create_fish_by_type(fish_type, fish_name, fish_species, price)
            aquarium = self.__find_aquarium_by_name(aquarium_name)
            return aquarium.add_fish(fish)
        except ValueError as error:
            return str(error)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium_by_name(aquarium_name)
        value = sum(f.price for f in aquarium.fish) + sum(d.price for d in aquarium.decorations)
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'
        return result.strip()

    def __find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
