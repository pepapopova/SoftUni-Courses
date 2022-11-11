hall_rent = int(input())
oscars = 0.7 * hall_rent
catering = 0.85 * oscars
sound = 0.5 * catering

total_cost = hall_rent + oscars + catering + sound
print(f"{total_cost:.2f}")