season = input()
km_per_month = float(input())
tariff = 0

if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        tariff = 0.75
    elif 5000 < km_per_month <= 10000:
        tariff = 0.95
    elif 10000 < km_per_month <= 20000:
        tariff = 1.45
elif season == "Summer":
    if km_per_month <= 5000:
        tariff = 0.9
    elif 5000 < km_per_month <= 10000:
        tariff = 1.1
    elif 10000 < km_per_month <= 20000:
        tariff = 1.45
elif season == "Winter":
    if km_per_month <= 5000:
        tariff = 1.05
    elif 5000 < km_per_month <= 10000:
        tariff = 1.25
    elif 10000 < km_per_month <= 20000:
        tariff = 1.45

total_salary_season = km_per_month * tariff * 4
net_salary = total_salary_season * 0.9

print(f"{net_salary:.2f}")