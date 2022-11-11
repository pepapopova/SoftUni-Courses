from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary, 1)
        self.appliances = [TV()]
        self.room_cost = 10
