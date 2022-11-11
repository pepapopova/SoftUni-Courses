number_heroes = int(input())
heroes_collection = {}
for n in range(number_heroes):
    current_hero = input().split(" ")
    if current_hero[0] not in heroes_collection:
        heroes_collection[current_hero[0]] = {}
        heroes_collection[current_hero[0]]['HP'] = int(current_hero[1])
        heroes_collection[current_hero[0]]['MP'] = int(current_hero[2])
    else:
        heroes_collection[current_hero[0]]['HP'] += int(current_hero[1])
        heroes_collection[current_hero[0]]['MP'] += int(current_hero[2])

command = input().split(" - ")
while command[0] != "End":
    hero_name = command[1]
    if command[0] == "CastSpell":
        if heroes_collection[hero_name]['MP'] >= int(command[2]):
            heroes_collection[hero_name]['MP'] -= int(command[2])
            print(f"{hero_name} has successfully cast {command[3]} and now has {heroes_collection[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {command[3]}!")
    elif command[0] == "TakeDamage":
        heroes_collection[hero_name]['HP'] -= int(command[2])
        if heroes_collection[hero_name]['HP'] > 0:
            print(f"{hero_name} was hit for {command[2]} HP by {command[3]} and now has {heroes_collection[hero_name]['HP']} HP left!")
        else:
            del heroes_collection[hero_name]
            print(f"{hero_name} has been killed by {command[3]}!")
    elif command[0] == "Recharge":
        recharged_max = 200 - heroes_collection[hero_name]['MP']
        heroes_collection[hero_name]['MP'] += int(command[2])
        if heroes_collection[hero_name]['MP'] > 200:
            heroes_collection[hero_name]['MP'] = 200
            print(f"{hero_name} recharged for {recharged_max} MP!")
        else:
            print(f"{hero_name} recharged for {command[2]} MP!")
    elif command[0] == "Heal":
        healed_max = 100 - heroes_collection[hero_name]['HP']
        heroes_collection[hero_name]['HP'] += int(command[2])
        if heroes_collection[hero_name]['HP'] > 100:
            heroes_collection[hero_name]['HP'] = 100
            print(f"{hero_name} healed for {healed_max} HP!")
        else:
            print(f"{hero_name} healed for {command[2]} HP!")
    command = input().split(" - ")

my_list = []
index = 0
for name, points in heroes_collection.items():
    current_hp = points['HP']
    current_mp = points['MP']
    print(f"{name}\n  HP: {current_hp}\n  MP: {current_mp}")
