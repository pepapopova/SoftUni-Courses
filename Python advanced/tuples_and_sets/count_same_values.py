numbers = tuple(map(float, input().split()))
# [float(x) for x in input().split()]

occurances = {}

for num in numbers:
    if num not in occurances:
        occurances[num] = 1
    else:
        occurances[num] += 1

for number, occurance in occurances.items():
    print(f"{number} - {occurance} times")


# [print(f"{key} - {value} times") for key, value in occurances.items()]
