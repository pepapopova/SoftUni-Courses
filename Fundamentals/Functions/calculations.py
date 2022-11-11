operation = input()
num1 = int(input())
num2 = int(input())


def calculator(operator, a, b):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return int(a/ b)
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


print(calculator(operation, num1, num2))