number = int(input())
even_set = set()
odd_set = set()
result = set()

for row in range(1, number + 1):
    name = input()
    current_sum = sum([ord(x) for x in name]) // row
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)

# it is better to calculate the sum in new variables at the beginning to make it make only 1 calculation

if sum(even_set) == sum(odd_set):
    result = even_set.union(odd_set)
elif sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=", ")
