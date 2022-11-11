def find_next_position(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


def validation(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
matrix = []
burrows = []
for row in range(size):
    row_elements = list(input())
    for col in range(size):
        if row_elements[col] == "S":
            next_row = row
            next_col = col
        elif row_elements[col] == "B":
            burrows.append((row, col))
    matrix.append(row_elements)

total_food = 0


while True:
    command = input()
    matrix[next_row][next_col] = "."
    next_row, next_col = find_next_position(next_row, next_col, command)
    if not validation(next_row, next_col, size):
        print("Game over!")
        break
    else:
        if matrix[next_row][next_col] == "*":
            total_food += 1
            matrix[next_row][next_col] == "S"
        elif matrix[next_row][next_col] == "B":
            burrows.remove((next_row, next_col))
            matrix[next_row][next_col] = "."
            next_row, next_col = burrows[0][0], burrows[0][1]
    if total_food >= 10:
        matrix[next_row][next_col] = "S"
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {total_food}")
for row in matrix:
    print(*row, sep="")