needed_money = float(input())
cash = float(input())
counter_spend = 0
succeed = True
counter = 0

while cash < needed_money:
    command = input()
    extra_cash = float(input())
    counter += 1
    if command == "spend":
        cash -= extra_cash
        counter_spend +=1
        if counter_spend == 5:
            succeed = False
            break
    elif command == "save":
        cash += extra_cash
        counter_spend = 0
    if cash < 0:
        cash = 0

if succeed:
    print(f"You saved the money for {counter} days.")
else:
    print("You can't save the money.")
    print(f"{counter}")