from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = deque([int(x) for x in input().split()])
signs = deque(input().split())
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}
total_honey = 0

while bees and nectars:
    current_bee = bees.popleft()
    current_nectar = nectars.pop()

    if current_nectar >= current_bee:
        operator = signs.popleft()
        if current_nectar == 0 and operator == "/":
            continue
        total_honey += abs(operations[operator](current_bee, current_nectar))

    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")