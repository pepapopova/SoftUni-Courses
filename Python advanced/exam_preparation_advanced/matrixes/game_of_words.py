def find_next_position(command, row, col):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


def validation(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True


string = input()

size = int(input())
matrix = []

for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col

commands = int(input())

for command in range(commands):
    current_command = input()
    next_row, next_col = find_next_position(current_command, player_row, player_col)
    if validation(next_row, next_col, size):
        if matrix[next_row][next_col] == "-":
            pass
        else:
            string += matrix[next_row][next_col]
        matrix[next_row][next_col] = "P"
        matrix[player_row][player_col] = "-"
        player_row, player_col = next_row, next_col
    else:
        if string:
            string = string[:-1]


print(string)
for row in matrix:
    print(*row, sep="")