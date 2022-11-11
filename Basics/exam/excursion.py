group = int(input())
nights = int(input())
transport_cards = int(input())
museum_tickets = int(input())

expenses_per_person = nights * 20 + transport_cards * 1.6 + museum_tickets * 6
total_cost = expenses_per_person * group
total_cost *= 1.25

print(f"{total_cost:.2f}")