rows = int(input())
matrix = []

# for i in range(rows):
#     matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])
#
# rows = int(input())
# matrix = []

for i in range(rows):
    row = input().split(", ")
    matrix.append(list(map(int, row)))
evens = [[x for x in row if x % 2 == 0] for row in matrix]

print(evens)


print(matrix)
