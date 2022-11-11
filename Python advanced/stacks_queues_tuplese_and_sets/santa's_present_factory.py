from collections import deque

materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
crafted_presents = {}
has_succeeded = False

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    total_magic = current_material * current_magic

    if current_material == 0 and current_magic == 0:
        continue

    if current_material == 0:
        magic.appendleft(current_magic)
        continue

    if current_magic == 0:
        materials.append(current_material)
        continue

    if total_magic in presents:
        if presents[total_magic] not in crafted_presents:
            crafted_presents[presents[total_magic]] = 1
        else:
            crafted_presents[presents[total_magic]] += 1
    elif total_magic < 0:
        materials.append(current_material + current_magic)
    else:
        materials.append(current_material + 15)


if "Doll" in crafted_presents and "Wooden train" in crafted_presents or \
        "Teddy bear" in crafted_presents and "Bicycle" in crafted_presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(reversed([str(x) for x in materials]))}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for present, count in sorted(crafted_presents.items(), key=lambda x: x[0]):
    print(f"{present}: {count}")


