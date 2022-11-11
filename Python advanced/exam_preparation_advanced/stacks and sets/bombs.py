from collections import deque

bomb_collection = {
    "Datura" : 0,
    "Cherry": 0,
    "Smoke Decoy": 0
}

all_collected = False
bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = deque([int(x) for x in input().split(", ")])

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    sum = current_effect + current_casing
    if sum == 40:
        bomb_collection["Datura"] += 1
    elif sum == 60:
        bomb_collection["Cherry"] += 1
    elif sum == 120:
        bomb_collection["Smoke Decoy"] += 1
    else:
        bomb_casings.append(current_casing - 5)
        bomb_effects.appendleft(current_effect)

    if bomb_collection["Datura"] >=3 and bomb_collection["Cherry"] >= 3 and bomb_collection["Smoke Decoy"] >= 3:
        all_collected = True
        break

if all_collected:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")

for bomb, value in sorted(bomb_collection.items()):
    print(f"{bomb} Bombs: {value}")