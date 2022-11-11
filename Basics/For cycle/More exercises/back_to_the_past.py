inherited_money = float(input())
year_until_live = int(input())
spend_money = 0
current_year = 1800
total_life = year_until_live - current_year


for year in range(0, total_life + 1):
    if year % 2 == 0:
        spend_money += 12000
    else:
        spend_money += 12000 + 50 * (18+year)

diff = abs(inherited_money - spend_money)
if inherited_money >= spend_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")