number_detergent = int(input())
total_detergent = number_detergent * 750
detergent_was_enough = True
command = int(input())
count = 0
count_plates = 0
count_pots = 0

while command != "End":
    load = int(command)
    count += 1
    if count % 3 == 0:
        total_detergent = total_detergent - (load * 15)
        count_pots += load
    else:
        total_detergent = total_detergent - (load * 5)
        count_plates += load
        detergent_was_enough = False
        break
    command = input()

if detergent_was_enough:
    print("Detergent was enough!")
    print(f"{count_plates} dishes and {count_pots} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
else:
    diff = abs(total_detergent)
    print(f"Not enough detergent, {diff} ml. more necessary!")
