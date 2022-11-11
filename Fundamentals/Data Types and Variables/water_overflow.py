capacity = 255
n = int(input())
poured_liters = 0
for _ in range(n):
    current_liters = int(input())
    if current_liters > capacity:
        print(f'Insufficient capacity!')
    else:
        capacity -= current_liters
        poured_liters += current_liters

print(poured_liters)