from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, name: str, budget: float, budget2: float, *children):
        count = 2 + len(children)
        super().__init__(name, budget + budget2, count)
        self.budget += budget2
        self.appliances = [TV(), Fridge(), Laptop()] * count
        self.expenses = self.calculate_expenses(self.appliances)
        self.children = list(children)
        self.room_cost = 30