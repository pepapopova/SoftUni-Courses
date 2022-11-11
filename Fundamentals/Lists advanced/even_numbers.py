number_string = list(map(int, input().split(", ")))
even_string = []

for num in range(len(number_string)):
    if number_string[num] % 2 == 0:
        even_string.append(num)

print(even_string)