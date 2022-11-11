import sys

number = int(input())
total_sum = 0
max_num = -sys.maxsize

for num in range(number):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_num:
        max_num = current_number

if max_num == total_sum - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = abs(max_num - (total_sum - max_num))
    print("No")
    print(f"Diff = {diff}")