stadium_capacity = int(input())
number_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for fans in range(number_fans):
    sector = input()
    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_v += 1
    if sector == "G":
        fans_g += 1

procent_a = fans_a / number_fans * 100
procent_b = fans_b / number_fans * 100
procent_v = fans_v / number_fans * 100
procent_g = fans_g / number_fans * 100
percent_all_fans = (fans_a + fans_b + fans_v + fans_g) / stadium_capacity * 100

print(f"{procent_a:.2f}%")
print(f"{procent_b:.2f}%")
print(f"{procent_v:.2f}%")
print(f"{procent_g:.2f}%")
print(f"{percent_all_fans:.2f}%")