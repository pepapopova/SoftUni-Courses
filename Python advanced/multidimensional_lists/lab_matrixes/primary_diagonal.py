def secondary_diagonal(size, matrix):
    return sum(matrix[x][size - x - 1] for x in range(size))


size = int(input())

matrix = []

for row in range(size):
    matrix.append([int(x) for x in input().split()])

primary_diagonal = 0
# primary_diagonal = sum([matrix[x][x] for x in range(size)])

for row in range(size):
    # for column in range(size):
    #     if row == column:
    #         primary_diagonal += matrix[row][column]
    primary_diagonal += matrix[row][row]


print(primary_diagonal)
print(secondary_diagonal(size, matrix))