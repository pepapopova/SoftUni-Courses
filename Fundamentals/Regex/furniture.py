import re

furniture = input()
total_cost = 0
bought_list = []
while furniture != "Purchase":
    matches = re.finditer(r'>{2}(?P<furniture>[A-Za-z]+)<{2}(?P<price>(\d+(\.\d+)?))!(?P<quantity>\d+)', furniture)
    if matches is not None: #this is important
        for furniture in matches:
            bought_list.append(furniture.group('furniture'))
            total_cost += float(furniture.group('price')) * int(furniture.group('quantity'))
    furniture = input()

print("Bought furniture:")
if len(bought_list) > 0:
    print("\n".join(bought_list))
print(f"Total money spend: {total_cost:.2f}")