needed_amount = int(input())
count = 0
cash_amount = 0
pos_amount = 0
cash_count = 0
pos_count = 0
average_cash = 0
average_pos = 0
command = input()
total_collected = 0

while command != "End":
    cost = int(command)
    count += 1
    if count % 2 != 0 and cost <= 100:
        print("Product sold!")
        cash_amount += cost
        cash_count += 1
        average_cash = cash_amount / cash_count
        money_are_collected = True
    elif count % 2 == 0 and cost >= 10:
        print("Product sold!")
        pos_amount += cost
        pos_count += 1
        average_pos = pos_amount / pos_count
        money_are_collected = True
    else:
        print("Error in transaction!")
    total_collected = cash_amount + pos_amount
    if total_collected >= needed_amount:
        break
    command = input()



if total_collected >= needed_amount:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_pos:.2f}")
else:
    print(f"Failed to collect required money for charity.")
