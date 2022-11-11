rows, columns = [int(x) for x in input().split(" ")]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

counter = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        if matrix[row][column] == matrix[row][column + 1] == matrix[row + 1][column] == matrix[row + 1][column + 1]:
            counter += 1

print(counter)