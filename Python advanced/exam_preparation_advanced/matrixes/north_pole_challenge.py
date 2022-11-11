def validation(rows, cols, next_row, next_col):
    if next_row < 0:
        next_row = rows - 1
    elif next_row > rows - 1:
        next_row = 0
    if next_col < 0:
        next_col = cols - 1
    elif next_col > cols - 1:
        next_col = 0
    return next_row, next_col



rows, cols = [int(x) for x in input().split(", ")]
santa_row = 0
santa_col = 0
matrix = []

def the_matrix_is_empty(matrix):
    for row in matrix:
        for el in row:
            if el not in "Yx.":
                return False
    return True



decorations_count = 0
gifts_count = 0
cookies_count = 0

for row in range(rows):
    row_elements = input().split()
    for col in range(cols):
        if row_elements[col] == "Y":
            santa_row = row
            santa_col = col
    matrix.append(row_elements)


# def find_next_position(matrix, row, col, direction):

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    direction = command[0]
    steps = int(command[1])
    for step in range(steps):
        next_row, next_col = directions[direction](santa_row, santa_col)
        next_row, next_col = validation(rows, cols, next_row, next_col)
        if matrix[next_row][next_col] == "D":
            decorations_count += 1
        elif matrix[next_row][next_col] == "G":
            gifts_count += 1
        elif matrix[next_row][next_col] == "C":
            cookies_count += 1
        matrix[santa_row][santa_col] = "x"
        matrix[next_row][next_col] = "x"
        santa_row, santa_col = next_row, next_col
        if the_matrix_is_empty(matrix):
            print("Merry Christmas!")
            break
    if the_matrix_is_empty(matrix):
        break

matrix[santa_row][santa_col] = "Y"
print("You've collected:")
print(f"- {decorations_count} Christmas decorations")
print(f"- {gifts_count} Gifts")
print(f"- {cookies_count} Cookies")

for row in matrix:
    print(*row, sep=" ")