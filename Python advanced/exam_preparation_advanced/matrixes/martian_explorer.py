def find_next_move(command, row, col):
    if command == "right":
        return row, col + 1
    elif command == "left":
        return row, col - 1
    elif command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col


def validation(size, row, col):
    if row < 0:
        return size - 1, col
    elif row >= size:
        return 0, col
    elif col < 0:
        return row, size - 1
    elif col >= size:
        return row, 0
    else:
        return row, col


size = 6

matrix = []
rover_row = 0
rover_col = 0

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "E":
            rover_row = row
            rover_col = col

commands = input().split(", ")

deposits = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete",
}
deposits_needed = {"W", "M", "C"}
deposits_collected = set()

for command in commands:
    next_row, next_col = find_next_move(command, rover_row, rover_col)
    next_row, next_col = validation(size, next_row, next_col)
    if matrix[next_row][next_col] in deposits:
        print(f"{deposits[matrix[next_row][next_col]]} deposit found at ({next_row}, {next_col})")
        deposits_collected.add(matrix[next_row][next_col])
        matrix[next_row][next_col] = "-"

    elif matrix[next_row][next_col] == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break

    rover_row, rover_col = next_row, next_col

if deposits_needed.issubset(deposits_collected):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")