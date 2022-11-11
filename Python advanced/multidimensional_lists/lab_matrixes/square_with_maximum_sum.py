import sys

rows, columns = [int(x) for x in input().split(", ")]
matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

max_sum = -sys.maxsize
start_row = 0
start_col = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        current_sum = matrix[row][column] + matrix[row][column + 1] + matrix[row + 1][column] + matrix[row + 1][column + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            start_row = row
            start_col = column

print(f"{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]}")
print(f"{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]}")
print(max_sum)
