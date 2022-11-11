def get_children(row, col, rows, cols):
    possible_children = [
        [row - 1, col],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col],
    ]

    result = []
    for child_row, child_col in possible_children:
        if 0 <= child_row < rows and 0 <= child_col < cols:
            result.append([child_row, child_col])

    return result


def is_inside(row, col, rows, cols):
    if 0 <= row < rows and 0 <= col < cols:
        return True


rows, cols = [int(x) for x in input().split()]
matrix = []
bunnies = []

for row in range(rows):
    row_elements = list(input())
    for col in range(cols):
        if row_elements[col] == "P":
            player_row = row
            player_col = col
        elif row_elements[col] == "B":
            bunnies.append((row, col))

    matrix.append(row_elements)

directions = {
    "L": lambda r, c: (r, c - 1),
    "R": lambda r, c: (r, c + 1),
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c),
}
player_won = False
bunny_won = False

string = input()
for ch in string:
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                bunnies.append((row, col))
    if bunny_won or player_won:
        # for bunny in bunnies:
        #     for row, col in get_children(bunny[0], bunny[1], rows, cols):
        #         matrix[row][col] = "B"
        break
    next_row, next_col = directions[ch](player_row, player_col)
    matrix[player_row][player_col] = "."
    if not is_inside(next_row, next_col, rows, cols):
        player_won = True
    elif matrix[next_row][next_col] == "B":
        bunny_won = True
    if is_inside(next_row, next_col, rows, cols):
        matrix[next_row][next_col] = "P"
        player_row, player_col = next_row, next_col
    for bunny in bunnies:
        for row, col in get_children(bunny[0], bunny[1], rows, cols):
            if matrix[row][col] == "P":
                matrix[row][col] = "B"
                bunny_won = True
            elif matrix[row][col] == ".":
                matrix[row][col] = "B"


for row in matrix:
    print(*row, sep="")

if player_won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")