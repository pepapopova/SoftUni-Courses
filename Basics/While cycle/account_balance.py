command = input()
total_balance = 0

while True:
    if command == "NoMoreMoney":
        break
    elif float(command) < 0:
        print("Invalid operation!")
        break
    total_balance += float(command)
    print(f"Increase: {float(command):.2f}")
    command = input()

print(f"Total: {total_balance:.2f}")