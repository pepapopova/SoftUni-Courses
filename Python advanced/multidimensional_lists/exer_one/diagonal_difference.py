size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

sum_primary = sum(matrix[i][i] for i in range(size))
sum_secondary = sum(matrix[i][size - 1 - i] for i in range(size))

print(abs(sum_primary - sum_secondary))