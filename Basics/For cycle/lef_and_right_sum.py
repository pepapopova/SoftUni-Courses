

#for x in range(num):
#    current_number1 = int(input())
#    sum1 += current_number1


#for x in range(num):
#    current_number2 = int(input())
#    sum2 += current_number2

num = int(input())
sum1 = 0
sum2 = 0

for x in range(2 * num):
    current_number = int(input())
    if x <= 1:
        sum1 += current_number
    else:
        sum2 += current_number

if sum1 == sum2:
    print(f"Yes, sum = {sum1}")
else:
    diff = abs(sum1 - sum2)
    print(f"No, diff = {diff}")