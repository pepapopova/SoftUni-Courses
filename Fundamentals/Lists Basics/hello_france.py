list_of_clothes = input().split("|")
budget = float(input())
sold_items = []
sold_items_data = []
profit = 0
condition = False

for item in list_of_clothes:
    current_item = item.split("->")
    if budget >= float(current_item[1]):
        if current_item[0] == "Clothes":
            if float(current_item[1]) <= 50:
                condition = True
        elif current_item[0] == "Shoes":
            if float(current_item[1]) <= 35:
                condition = True
        elif current_item[0] == "Accessories":
            if float(current_item[1]) <= 20.5:
                condition = True
        if condition:
            current_profit = float(current_item[1]) * 0.4
            new_price = float(current_item[1]) * 1.4
            budget -= float(current_item[1])
            sold_items.append(new_price)
            sold_items_data.append(f"{new_price:.2f}")
            profit += current_profit
            condition = False

print(" ".join(sold_items_data))
print(f"Profit: {profit:.2f}")

if budget + sum(sold_items) >= 150:
    print("Hello, France!")
else:
    print(f"Not enough money.")
