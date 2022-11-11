from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, name: str, budget: float, budget2: float):
        super().__init__(name, budget + budget2, 1)
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
        self.expenses = self.calculate_expenses(self.appliances)
        self.room_cost = 15
