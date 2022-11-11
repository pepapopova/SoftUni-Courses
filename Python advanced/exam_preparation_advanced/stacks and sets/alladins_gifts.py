from collections import deque

materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])

presents = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    result = current_magic + current_material
    if result < 100:
        if result % 2 == 0:
            result = 2 * current_material + 3 * current_magic
        else:
            result = 2 * current_material + 2 * current_magic
    if result > 499:
        result /= 2
    if 100 <= result <= 199:
        presents["Gemstone"] += 1
    elif 200 <= result <= 299:
        presents["Porcelain Sculpture"] += 1
    elif 300 <= result <= 399:
        presents["Gold"] += 1
    elif 400 <= result <= 499:
        presents["Diamond Jewellery"] += 1

if (presents["Gemstone"] > 0 and presents["Porcelain Sculpture"] > 0) or \
    (presents["Gold"] > 0 and presents["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for present, count in sorted(presents.items()):
    if count > 0:
        print(f"{present}: {count}")
