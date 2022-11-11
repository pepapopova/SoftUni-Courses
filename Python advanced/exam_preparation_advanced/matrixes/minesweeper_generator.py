def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size

size = int(input())

matrix = [[None] * size for x in range(size)]

mines = int(input())

for mine in range(mines):
    mine_row, mine_col = eval(input())
    matrix[mine_row][mine_col] = "*"

d = {
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c),
    "left": lambda r, c: (r, c - 1),
    "right": lambda r, c: (r, c + 1),
    "up_right": lambda r, c: (r - 1, c + 1),
    "up_left": lambda r, c: (r - 1, c - 1),
    "down_right": lambda r, c: (r + 1, c + 1),
    "down_left": lambda r, c: (r + 1, c - 1),
}

for row in range(size):
    for col in range(size):
        if matrix[row][col] != "*":
            current_value = 0
            for direction in d:
                check_row, check_col = d[direction](row, col)
                if is_inside(check_row, check_col, size):
                    if matrix[check_row][check_col] == "*":
                        current_value += 1
            matrix[row][col] = current_value

for row in matrix:
    print(*row, sep=" ")