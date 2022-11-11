number_offer_sea = int(input())
number_offer_mountain = int(input())
command = input()
count_mountain = 0
count_sea = 0
profit = 0

while command != "Stop":
    packet_name = command
    if command == "sea":
        if number_offer_sea > 0:
            profit += 680
            number_offer_sea -= 1
    elif command == "mountain":
        if number_offer_mountain > 0:
            profit += 499
            number_offer_mountain -= 1
    if number_offer_mountain == 0 and number_offer_sea == 0:
        print("Good job! Everything is sold.")
        break

    command = input()

print(f"Profit: {profit} leva.")

