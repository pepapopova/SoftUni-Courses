quantity = int(input())
days = int(input())
total_price = 0
christmas_spirit = 0

for i in range(1, days + 1 ):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_price += 2 * quantity
        christmas_spirit += 5
    if i % 3 == 0:
        total_price += (5 + 3) * quantity
        christmas_spirit += 13
    if i % 5 == 0:
        total_price += 15 * quantity
        christmas_spirit += 17

    if i % 3 == 0 and i % 5 == 0:
        christmas_spirit += 30

    if i % 10 == 0:
        christmas_spirit -= 20
        total_price += 23

if days % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {total_price}")
print(f"Total spirit: {christmas_spirit}")
