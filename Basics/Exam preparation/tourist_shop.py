budget = float(input())
counter = 0
command = input()
you_dont_run_out_of_money = True
total_cost = 0

while command != "Stop":
    name_product = command
    price_product = float(input())
    counter += 1
    if counter % 3 == 0:
        price_product *= 0.5
    if price_product > budget:
        diff = price_product - budget
        you_dont_run_out_of_money = False
        break
    total_cost += price_product
    budget -= price_product
    command = input()

if you_dont_run_out_of_money:
    print(f"You bought {counter} products for {total_cost:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {diff:.2f} leva!")

