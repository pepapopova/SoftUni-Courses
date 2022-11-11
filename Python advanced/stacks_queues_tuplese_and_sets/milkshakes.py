from collections import deque

chocolates = deque([int(x) for x in input().split(", ")])
cups = deque([int(x) for x in input().split(", ")])

milkshakes = 0
while True:
    if milkshakes >= 5 or not chocolates or not cups:
        break

    current_cup = cups.popleft()
    current_chocolate = chocolates.pop()

    if current_chocolate <= 0 and current_cup <= 0:
        continue

    if current_chocolate <= 0:
        cups.appendleft(current_cup)
        continue

    if current_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_cup:
        milkshakes += 1
    else:
        cups.append(current_cup)
        chocolates.append(current_chocolate - 5)

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if cups:
    print(f"Milk: {', '.join([str(x) for x in cups])}")
else:
    print("Milk: empty")

