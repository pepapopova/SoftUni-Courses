number = input()
current_number = 0
largest_number = 0
new_number = 0


for i in range(len(number)):
    current_number = int(number[i])
    if current_number > largest_number:
        largest_number = current_number

for i in range(len(number)):
    if largest_number == int(number[i]):
        number = number[:i] + number[i+1:]
        new_number = largest_number
        print(largest_number)

#това е вярното решение
number = list(input())
number.sort(reverse=True)  # сортиране на числата във възходящ ред и след това ги обръщам.
print(''.join(number))