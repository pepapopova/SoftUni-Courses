number_processors = int(input())
number_staff = int(input())
working_days = int(input())

total_working_hours = working_days * 8 * number_staff
processors_made = total_working_hours // 3
total_profit = processors_made * 110.10
diff = abs(number_processors - processors_made)

if processors_made >= number_processors:
    diff *= 110.10
    print(f"Profit: -> {diff:.2f} BGN")
else:
    diff *= 110.10
    print(f"Losses: -> {diff:.2f} BGN")
