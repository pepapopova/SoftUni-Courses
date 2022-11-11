rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

print([num for sublist in matrix for num in sublist])