n = int(input())
sum_odd = 0
sum_even = 0

for num in range(n):
    current_number = int(input())
    if num % 2 == 0:
        sum_even +=current_number
    else:
        sum_odd +=current_number

if sum_even == sum_odd:
    print(f"Yes")
    print(f"Sum = {sum_odd}")
else:
    print("No")
    diff = abs(sum_even - sum_odd)
    print(f"Diff = {diff}")