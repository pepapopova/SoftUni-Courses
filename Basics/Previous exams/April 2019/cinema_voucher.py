voucher = int(input())
counter_movie_tickets = 0
command = input()
purchases_price = 0
counter_other = 0
while command != "End":
    purchase = command

    if len(purchase) > 8:
        purchases_price = ord(purchase[0]) + ord(purchase[1])
        if purchases_price > voucher:
            break
        counter_movie_tickets += 1
    else:
        purchases_price = ord(purchase[0])
        if purchases_price > voucher:
            break
        counter_other += 1

    voucher -= purchases_price
    command = input()

print(f"{counter_movie_tickets}")
print(f"{counter_other}")