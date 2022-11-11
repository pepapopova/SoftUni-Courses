#
# new_list = [int(input()), int(input()), int(input())]
#
#
# def smallest_of_three(base_list):
#    min_number = min(base_list)
#    return min_number
#
# print(smallest_of_three(new_list))


def smallest_of_three_numbers(a, b, c):
      return min(a, b, c)


num1, num2, num3 = int(input()), int(input()), int(input())

print(smallest_of_three_numbers(num1, num2, num3))