n = int(input())
number_is_special = False


for num in range(1, n+ 1):
    sum_of_digits = 0
    working_number = num

    while working_number > 0:
        sum_of_digits += working_number % 10
        working_number = working_number // 10

    is_special = sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11
    print(f'{num} -> {is_special}')

    # if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
    #     print(f'{num} -> True')
    # else:
    #     print(f'{num} -> False')