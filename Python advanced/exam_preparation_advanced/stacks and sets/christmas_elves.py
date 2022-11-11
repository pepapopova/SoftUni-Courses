from collections import deque

elves = deque([int(x) for x in input().split()])
materials = deque([int(x) for x in input().split()])

total_energy = 0
toys = 0
count = 1

while elves and materials:
    current_energy = elves.popleft()
    if current_energy < 5:
        continue
    current_material = materials.pop()
    if count % 3 == 0 and count % 5 == 0:
        if current_energy >= current_material * 2:
            current_energy -= current_material
            elves.append(current_energy)
            total_energy += current_material
        else:
            materials.append(current_material)
            elves.append(current_energy * 2)
    elif count % 3 == 0:
        if current_energy >= current_material * 2:
            current_energy = current_energy - (current_material * 2) + 1
            elves.append(current_energy)
            toys += 2
            total_energy += (current_material * 2)
        else:
            materials.append(current_material)
            elves.append(current_energy * 2)
    elif count % 5 == 0:
        if current_energy >= current_material:
            current_energy -= current_material
            elves.append(current_energy)
            total_energy += current_material
        else:
            materials.append(current_material)
            elves.append(current_energy * 2)
    else:
        if current_energy >= current_material:
            current_energy = current_energy - current_material + 1
            elves.append(current_energy)
            toys += 1
            total_energy += current_material
        else:
            materials.append(current_material)
            elves.append(current_energy * 2)
    count += 1

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")
if elves:
    print(f"Elves left: {', '.join([str(x) for x in elves])}")
if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")