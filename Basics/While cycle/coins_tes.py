sum = float(input())
sum = int(sum * 100)
coins_counter = 0

while sum > 0:
    if sum - 200 >= 0:
        coins_counter += 1
        sum -= 200
        continue
    elif sum - 100 >= 0:
        coins_counter += 1
        sum -= 100
        continue
    elif sum - 50 >= 0:
        coins_counter += 1
        sum -= 50
        continue
    elif sum - 20 >= 0:
        coins_counter += 1
        sum -= 20
        continue
    elif sum - 10 >= 0:
        coins_counter += 1
        sum -= 10
        continue
    elif sum - 5 >= 0:
        coins_counter += 1
        sum -= 5
        continue
    elif sum - 2 >= 0:
        coins_counter += 1
        sum -= 2
        continue
    else:
        coins_counter += 1
        sum -= 1

print(coins_counter)