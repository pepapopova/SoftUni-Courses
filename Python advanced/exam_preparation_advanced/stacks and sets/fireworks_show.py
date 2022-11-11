from collections import deque

effects = deque([int(x) for x in input().split(", ")])
power = deque([int(x) for x in input().split(", ")])

fireworks = {
    "Palm": 0,
    "Willow": 0,
    "Crossette": 0
}
all_collected = False

while effects and power and not all_collected:
    current_effect = effects.popleft()
    if current_effect <= 0:
        continue
    current_power = power.pop()
    if current_power <= 0:
        effects.appendleft(current_effect)
        continue
    result = current_effect + current_power
    if result % 3 == 0 and result % 5 != 0:
        fireworks["Palm"] += 1
    elif result % 5 == 0 and result % 3 != 0:
        fireworks["Willow"] += 1
    elif result % 3 == 0 and result % 5 == 0:
        fireworks["Crossette"] += 1
    else:
        effects.append(current_effect - 1)
        power.append(current_power)
    if fireworks["Palm"] >= 3 and fireworks["Willow"] >= 3 and fireworks["Crossette"] >= 3:
        all_collected = True


if all_collected:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

for firework, count in fireworks.items():
    print(f"{firework} Fireworks: {count}")