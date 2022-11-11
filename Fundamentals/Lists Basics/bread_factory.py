energy = 100
coins = 100
daily_events = input().split("|")
condition = True

for event in daily_events:
    current_event = event.split("-")
    command = current_event[0]
    number = int(current_event[1])
    if command == "rest":
        if energy < 100:
            energy += number
            print(f"You gained {number} energy.")
        else:
            energy = 100
            print(f"You gained 0 energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            print(f"You had to rest!")
            energy += 50
    else:
        if number <= coins:
            print(f"You bought {command}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {command}.")
            condition = False
            break

if condition:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")