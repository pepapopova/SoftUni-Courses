from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0
cups_filled = 0

while cups and bottles:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()
    if current_bottle >= current_cup:
        wasted_water += (current_bottle - current_cup)
    elif current_cup > current_bottle:

        while current_cup > 0:
            current_cup -= current_bottle
            if current_cup <= 0:
                cups_filled += 1
                wasted_water += -current_cup
                break
            if bottles:
                current_bottle = bottles.pop()
            else:
                cups.appendleft(current_cup)
                break

reversed_bottles = reversed(bottles)
if not cups:
    print(f"Bottles: {' '.join(str(x) for x in reversed_bottles)}")
if not bottles:
    print(f"Cups: {' '.join(str(x) for x in cups)}")

print(f"Wasted litters of water: {wasted_water}")


