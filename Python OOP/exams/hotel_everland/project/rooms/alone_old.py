from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, name: str, budget: float):
        super().__init__(name, budget, 1)
        self.room_cost = 10

