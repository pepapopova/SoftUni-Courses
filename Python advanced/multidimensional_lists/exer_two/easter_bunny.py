import sys

size = int(input())

field = []

bunny_row = 0
bunny_col = 0
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "B":
            bunny_col = col
            bunny_row = row
    field.append(row_elements)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}
best_sum = -sys.maxsize
best_dir = ''
best_path = []

for direction in directions:
    current_sum = 0
    current_path = []
    row, col = directions[direction](bunny_row, bunny_col)

    while 0 <= row < len(field) and 0 <= col < len(field) and field[row][col] != "X":
        current_sum += int(field[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

    if current_sum > best_sum and current_path:
        best_sum = current_sum
        best_dir = direction
        best_path = current_path

print(best_dir)
print(*best_path, sep='\n')
print(best_sum)