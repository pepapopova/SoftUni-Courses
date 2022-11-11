def get_next_position(r, c, command):
    if command == "right":
        return r, c + 1
    elif command == "left":
        return r, c - 1
    elif command == "up":
        return r - 1, c
    elif command == "down":
        return r + 1, c


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())

commands = input().split()

field = []
miner_row = 0
miner_col = 0
total_coal = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "s":
            miner_row = row
            miner_col = col
        elif row_elements[col] == "c":
            total_coal += 1
    field.append(row_elements)

for command in commands:
    next_row, next_cow = get_next_position(miner_row, miner_col, command)
    if is_inside(next_row, next_cow, size):
        field[miner_row][miner_col] = "*"
        if field[next_row][next_cow] == "c":
            total_coal -= 1
            field[next_row][next_cow] = "s"
        elif field[next_row][next_cow] == "e":
            print(f"Game over! ({next_row}, {next_cow})")
            break
        miner_row, miner_col = next_row, next_cow
    if total_coal == 0:
        print(f"You collected all coal! ({next_row}, {next_cow})")
        break
else:
    print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_col})")


