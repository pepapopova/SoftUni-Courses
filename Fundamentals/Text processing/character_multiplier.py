string = input().split(" ")
min_len = 0
total_sum = 0

if len(string[0]) > len(string[1]):
    min_len = len(string[1])
else:
    min_len = len(string[0])

for index in range(min_len):
    total_sum += ord(string[0][index]) * ord(string[1][index])

print(ord("c"))

