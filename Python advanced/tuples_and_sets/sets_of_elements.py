length1, length2 = [int(x) for x in input().split()]
set1 = set()
set2 = set()
for num in range(length1):
    set1.add(int(input()))

for num in range(length2):
    set2.add(int(input()))

# [print(element) for element in set1.intersection(set2)]
result = set1.intersection(set2)
for num in result:
    print(num)
