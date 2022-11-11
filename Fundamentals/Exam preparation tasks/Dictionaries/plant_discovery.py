number_plants = int(input())
plants_seen = {}
for plant in range(number_plants):
    current_plant = input().split("<->")
    plant_name = current_plant[0]
    rarity = int(current_plant[1])
    if plant_name not in plants_seen:
        plants_seen[plant_name] = {'Rarity': 0, 'Rating': []}
        plants_seen[plant_name]['Rarity'] = rarity
    else:
        plants_seen[plant_name]['Rarity'] = rarity

command = input().split(": ")

while command[0] != "Exhibition":
    current_command = command[1].split(" - ")
    plant_name = current_command[0]
    if plant_name not in plants_seen:
        print("error")
    else:
        if command[0] == "Rate":
            rating = int(current_command[1])
            plants_seen[plant_name]['Rating'].append(rating)
        elif command[0] == "Update":
            rarity_new = current_command[1]
            plants_seen[plant_name]['Rarity'] = rarity_new
        elif command[0] == "Reset":
            plants_seen[plant_name]['Rating'].clear()
    command = input().split(": ")

print("Plants for the exhibition:")

for plant, char in plants_seen.items():
    if len(plants_seen[plant]['Rating']) > 0:
        average_rating = sum(plants_seen[plant]['Rating'])/len(plants_seen[plant]['Rating'])
        print(f"- {plant}; Rarity: {plants_seen[plant]['Rarity']}; Rating: {average_rating:.2f}")
    else:
        print(f"- {plant}; Rarity: {plants_seen[plant]['Rarity']}; Rating: 0.00")