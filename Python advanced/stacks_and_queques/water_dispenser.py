from collections import deque

queue = deque()

water_quantity = int(input())

while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == 'refill':
        water_quantity += int(command[1])
    else:
        needed_water = int(command[0])
        if needed_water <= water_quantity:
            print(f"{queue.popleft()} got water")
            water_quantity -= needed_water
        else:
            print(f"{queue.popleft()} must wait")

print(f"{water_quantity} liters left")