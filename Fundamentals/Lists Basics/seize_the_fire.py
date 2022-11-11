fire_cell = input().split("#")
water_amount = int(input())
effort = 0
total_fire = 0

print("Cells:")
for current_fire in fire_cell:
    fire_info = current_fire.split(" = ")
    type_of_fire = fire_info[0]
    cell = int(fire_info[1])
    if type_of_fire == "High":
        if 81 <= cell <= 125:
            if water_amount >= cell:
                print(f" - {cell}")
                water_amount -= cell
                effort += 0.25 * cell
                total_fire += cell
    elif type_of_fire == "Medium":
        if 51 <= cell <= 80:
            if water_amount >= cell:
                print(f" - {cell}")
                water_amount -= cell
                effort += 0.25 * cell
                total_fire += cell
    elif type_of_fire == "Low":
        if 1 <= cell <= 50:
            if water_amount >= cell:
                print(f" - {cell}")
                water_amount -= cell
                effort += 0.25 * cell
                total_fire += cell

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")