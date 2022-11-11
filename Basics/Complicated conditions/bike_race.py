number_juniors = int(input())
number_seniors = int(input())
trace = input()

revenue_seniors = 0
revenue_juniors = 0
discount = 0

if trace == "trail":
    revenue_juniors = number_juniors * 5.5
    revenue_seniors = number_seniors * 7
elif trace == "cross-country":
    revenue_juniors = number_juniors * 8
    revenue_seniors = number_seniors * 9.5
    if number_seniors + number_juniors >= 50:
        discount = 0.25
elif trace == "downhill":
    revenue_juniors = number_juniors * 12.25
    revenue_seniors = number_seniors * 13.75
else:
    revenue_juniors = number_juniors * 20
    revenue_seniors = number_seniors * 21.5

total_revenue = (revenue_seniors + revenue_juniors) * (1 - discount)
revenue_minus_expenses = total_revenue * 0.95

print(f"{revenue_minus_expenses:.2f}")