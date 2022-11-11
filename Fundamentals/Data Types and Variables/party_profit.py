group_size = int(input())
days = int(input())
count_coins = 0


for day in range(1, days + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    count_coins += 50 - group_size * 2
    if day % 3 == 0:
        count_coins -= group_size * 3
    if day % 5 == 0:
        count_coins += group_size * 20
    if day % 3 == 0 and day % 5 == 0:
        count_coins -= group_size * 2


coin_per_person = count_coins // group_size
print(f"{group_size} companions received {coin_per_person} coins each.")