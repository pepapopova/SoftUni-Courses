age = int(input())
price_laudrymat = float(input())
price_per_toy = int(input())
count_toy = 0
cash = 0
total_cash = 0
total_money = 0

for num in range(1, age + 1):
    if num % 2 == 0:
        cash += 10
        total_cash += cash - 1
    else:
        count_toy += 1

price_toys = count_toy * price_per_toy
total_cash += price_toys

diff = abs(total_cash - price_laudrymat)
if total_cash >= price_laudrymat:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
