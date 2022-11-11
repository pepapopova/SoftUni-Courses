town_data = input()
town_dict = {}
while town_data != "Sail":
    current_town = town_data.split('||')
    town = current_town[0]
    population = int(current_town[1])
    gold = int(current_town[2])
    if town not in town_dict:
        town_dict[town] = {}
        town_dict[town]['population'] = population
        town_dict[town]['gold'] = gold
    else:
        town_dict[town]['population'] += population
        town_dict[town]['gold'] += gold
    town_data = input()

command = input()
while command != 'End':
    current_command = command.split('=>')
    town = current_command[1]
    if current_command[0] == 'Plunder':
        people = int(current_command[2])
        gold = int(current_command[3])
        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        town_dict[town]['gold'] -= gold
        town_dict[town]['population'] -= people
        if town_dict[town]['gold'] == 0 or town_dict[town]['population'] == 0:
            del town_dict[town]
            print(f"{town} has been wiped off the map!")
    elif current_command[0] == 'Prosper':
        gold = int(current_command[2])
        if gold < 0:
            print('Gold added cannot be a negative number!')
        if gold > 0:
            town_dict[town]['gold'] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {town_dict[town]["gold"]} gold.')
    command = input()

if len(town_dict) > 0:
    print(f'Ahoy, Captain! There are {len(town_dict)} wealthy settlements to go to:')
    for town, char in town_dict.items():
        print(f'{town} -> Population: {town_dict[town]["population"]} citizens, Gold: {town_dict[town]["gold"]} kg')

else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
