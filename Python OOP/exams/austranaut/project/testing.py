from project.astronaut.astronaut_repository import AstronautRepository
from project.space_station import SpaceStation

space_station = SpaceStation()
print(space_station.add_astronaut('Geodesist', 'Yanko'))
print(space_station.add_astronaut('Geodesist', 'Pepa'))
# print(space_station.astronaut_repository.astronauts)
print(space_station.add_planet('Luna', 'laino, kosa, boza'))
print(space_station.add_planet('Luna', 'laino, kosa, boza'))
print(space_station.planet_repository.planets[0].items)
print(space_station.retire_astronaut('Pepa'))
print(space_station.astronaut_repository.astronauts[0].name)
print(space_station.add_astronaut('Geodesist', 'Gabi'))
print(space_station.add_astronaut('Geodesist', 'Doca'))

print(space_station.send_on_mission('Luna'))
print(space_station.report())