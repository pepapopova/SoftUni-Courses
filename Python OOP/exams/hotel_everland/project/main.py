from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room

tv = TV()
stove = Stove()
child1 = Child(10, 12, 13)
room = Room('Penthouse', 200, 3)
room.calculate_expenses(tv, stove, child1)
print(room.expenses)