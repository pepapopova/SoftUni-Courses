def sum_numbers(num):
    sum_even_num = 0
    sum_odd_num = 0
    for n in range(len(num)):
        current_num = int(num[n])
        if current_num % 2 == 0:
            sum_even_num += current_num
        else:
            sum_odd_num += current_num
    print(f"Odd sum = {sum_odd_num}, Even sum = {sum_even_num}")


single_number = input()
sum_numbers(single_number)