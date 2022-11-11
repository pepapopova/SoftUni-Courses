command = input()
count_kids = 0
count_adults = 0
money_toys = 0
money_sweatshirts = 0

while command != "Christmas":
    age = int(command)
    if age <= 16:
        count_kids += 1
        money_toys += 5
    elif age > 16:
        count_adults += 1
        money_sweatshirts += 15
    command = input()

print(f"Number of adults: {count_adults}")
print(f"Number of kids: {count_kids}")
print(f"Money for toys: {money_toys}")
print(f"Money for sweaters: {money_sweatshirts}")
