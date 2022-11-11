n = int(input())
plants_dict = {}

for plant in range(n):
    current_plant = input().split("<->")
    if current_plant[0] not in plants_dict:
        plants_dict[current_plant[0]] = {}
        plants_dict[current_plant[0]]['Rating'] = []
        plants_dict[current_plant[0]]['Rarity'] = current_plant[1]
    else:
        plants_dict[current_plant[0]]['Rarity'] = current_plant[1]

command = input()
while command != "Exhibition":
    current_command = command.split(": ")
    plant_details = current_command[1].split(" - ")
    plant = plant_details[0]
    if plant not in plants_dict:
        print("error")
    else:
        if current_command[0] == "Rate":
            rating = int(plant_details[1])
            plants_dict[plant]['Rating'].append(rating)
        elif current_command[0] == "Update":
            plants_dict[plant]['Rarity'] = plant_details[1]
        elif current_command[0] == "Reset":
            plants_dict[plant]['Rating'] = []
    command = input()

print("Plants for the exhibition:")

for plant in plants_dict:
    if len(plants_dict[plant]['Rating']) > 0:
        average_rating = sum(plants_dict[plant]['Rating'])/len(plants_dict[plant]['Rating'])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {plants_dict[plant]['Rarity']}; Rating: {average_rating:.2f}")