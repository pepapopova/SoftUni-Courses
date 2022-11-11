n = int(input())
plants_dict = {}

for plants in range(n):
    plant = input().split("<->")
    plant_name = plant[0]
    plant_rarity = int(plant[1])
    if plant_name not in plants_dict:
        plants_dict[plant_name] = {}
        plants_dict[plant_name]['rarity'] = plant_rarity
        plants_dict[plant_name]['rating'] = []
    else:
        plants_dict[plant_name]['rarity'] = plant_rarity

command = input()
while command != "Exhibition":
    current_command = command.split(": ")
    plants_data = current_command[1].split(" - ")
    current_plant = plants_data[0]
    if current_plant not in plants_dict:
        print("error")
    else:
        if current_command[0] == "Rate":
            rating = int(plants_data[1])
            plants_dict[current_plant]['rating'].append(rating)
        elif current_command[0] == "Update":
            rarity = int(plants_data[1])
            plants_dict[current_plant]['rarity'] = rarity
        elif current_command[0] == "Reset":
            plants_dict[current_plant]['rating'] = []
    command = input()


print("Plants for the exhibition:")
for plant in plants_dict:
    if len(plants_dict[plant]['rating']) > 0:
        average_rating = sum(plants_dict[plant]['rating'])/len(plants_dict[plant]['rating'])
        print(f"- {plant}; Rarity: {plants_dict[plant]['rarity']}; Rating: {average_rating:.2f}")
    else:
        print(f"- {plant}; Rarity: {plants_dict[plant]['rarity']}; Rating: 0.00")