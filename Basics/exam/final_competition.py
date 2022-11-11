number_dancers = int(input())
points = float(input())
season = input()
place = input()
prize = 0

if place == "Bulgaria":
    prize = points * number_dancers
    if season == "summer":
        prize *= 0.95
    else:
        prize *= 0.92
elif place == "Abroad":
    prize = points * number_dancers * 1.5
    if season == "summer":
        prize *= 0.90
    else:
        prize *= 0.85

charity_prize = prize * 0.75
left_amount = prize * 0.25
amount_per_person = left_amount / number_dancers

print(f"Charity - {charity_prize:.2f}")
print(f"Money per dancer - {amount_per_person:.2f}")
