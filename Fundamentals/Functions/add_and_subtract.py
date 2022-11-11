def sum_numbers(a, b):
    return a + b


def subtract(current_sum, c):
    return current_sum - c


num1 = int(input())
num2 = int(input())
num3 = int(input())

result = subtract(sum_numbers(num1, num2), num3)
print(result)
