hall_rent = float(input())

cake = 0.2 * hall_rent
drinks = 0.55 * cake
animator = 1 / 3 * hall_rent

total_budget = hall_rent + cake + drinks + animator

print(f"{total_budget:.1f}")