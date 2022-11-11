from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_value = 0
        for room in self.rooms:
            total_value += room.expenses
        return f"Monthly consumption: {total_value:.2f}$."

    def pay(self):
        pass

    def status(self):
        pass