# number = int(input())
# sum_to_be_perfect = 0
#
# for n in range(1, number):
#     if number % n == 0:
#         sum_to_be_perfect += n
#
# if sum_to_be_perfect == number:
#     print(f"We have a perfect number!")
# else:
#     print(f"It's not so perfect.")

def perfect_number(random_number):
    sum_to_test = 0
    for num in range(1, random_number):
        if random_number % num == 0:
            sum_to_test += num
    if sum_to_test == random_number:
        print(f"We have a perfect number!")
    else:
        print(f"It's not so perfect.")

number = int(input())
perfect_number(number)