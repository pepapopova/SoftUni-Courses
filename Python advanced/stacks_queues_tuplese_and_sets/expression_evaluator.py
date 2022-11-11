from collections import deque

line = input().split(" ")
numbers = deque()
operations = {
    "+": lambda a,b: a + b,
    "-": lambda a,b: a - b,
    "*": lambda a,b: a * b,
    "/": lambda a,b : a // b
}

for el in line:
    ''' If we do not want to make this two conditions we can start with is el in "+-/*"'''
    if el.isdigit():
        numbers.append(int(el))
    elif el.startswith("-") and len(el) >= 2:
        numbers.append(int(el))
    else:
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            result = operations[el](first, second)
            numbers.appendleft(result)

print(numbers.popleft())