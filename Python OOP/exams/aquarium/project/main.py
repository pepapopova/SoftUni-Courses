from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


decoration1 = Ornament()
decoration2 = Plant()
decoration3 = Plant()
decoration4 = Ornament()
decoration_rep = DecorationRepository()
decoration_rep.add(decoration1)
decoration_rep.add(decoration2)
decoration_rep.add(decoration3)
decoration_rep.add(decoration4)
controller = Controller()
print(controller.add_aquarium('FreshwaterAquarium', 'Topa'))
print(controller.add_aquarium('SaltwaterAquarium', 'Luksa'))
print(controller.add_decoration('Plant'))
print(controller.add_decoration('Ornament'))
print(controller.add_decoration('Plant'))
print(len(controller.decorations_repository.decorations))
print(controller.insert_decoration('Luksa', 'Plant'))
print(controller.insert_decoration('Topa', 'Ornament'))
print(controller.insert_decoration('Topa', 'Ornament'))
print(controller.add_fish('Topa', 'FreshwaterFish', 'Dori', 'Skat', 2.50))
print(controller.feed_fish('Topa'))
print(controller.calculate_value('Topa'))
print(controller.report())