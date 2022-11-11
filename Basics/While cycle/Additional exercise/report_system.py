needed_sum = int(input())
collected_money = 0
cash_collected = 0
pos_collected = 0
count_cash = 0
count_pos = 0
average_cash = 0
average_pos = 0
cash_is_collected = True
count = 0


while collected_money < needed_sum:
    count += 1
    command = input()
    if command == "End":
        cash_is_collected = False
        break
    if count % 2 != 0:
        cash_payment = int(command)
        if cash_payment > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            count_cash += 1
            cash_collected += cash_payment
            collected_money += cash_payment
            average_cash = cash_collected / count_cash
    else:
        pos_payment = int(command)
        if pos_payment < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            count_pos += 1
            pos_collected += pos_payment
            collected_money += pos_payment
            average_pos = pos_collected / count_pos


if cash_is_collected:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_pos:.2f}")
else:
    print(f"Failed to collect required money for charity.")
