n = int(input())
numbers = []
filtered = []

for num in range(n):
    numbers.append(int(input()))

command = input()

if command == 'even':
    for number in numbers:
        if number % 2 == 0 or number == 0:
            filtered.append(number)
elif command == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
elif command == 'negative':
    for number in numbers:
        if number < 0:
            filtered.append(number)
else:
    for number in numbers:
        if number >= 0:
            filtered.append(number)

print(filtered)

n = int(input())
odd = []
even = []
positive = []
negative = []

# for num in range(n):
#     current_num = int(input())
#     if current_num >= 0:
#         positive.append(current_num)
#     if current_num < 0:
#         negative.append(current_num)
#     if current_num % 2 != 0:
#         odd.append(current_num)
#     if current_num % 2 == 0 or current_num == 0:
#         even.append(current_num)
#
# filter_word = input()
#
# print(eval(filter_word))