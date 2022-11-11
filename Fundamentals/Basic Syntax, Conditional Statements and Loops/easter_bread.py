budget = float(input())
price_flour = float(input())
price_eggs = 0.75 * price_flour
price_milk = 1.25 * price_flour
loaves = 0
price_per_loaf = price_flour + price_eggs + 0.25 * price_milk
count_loaves = 0
colored_eggs = 0

while budget > price_per_loaf:
    count_loaves += 1
    colored_eggs += 3
    if count_loaves % 3 == 0:
        colored_eggs -= count_loaves - 2
    budget -= price_per_loaf


print(f"You made {count_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")