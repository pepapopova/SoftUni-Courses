first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    sum_odd = 0
    sum_even = 0
    current_number_as_string = str(current_number)
    for index, digit in enumerate(current_number_as_string):
        if index % 2 == 0:
            sum_even += int(digit)
        else:
            sum_odd += int(digit)

    if sum_odd == sum_even:
        print(current_number, end = " ")
