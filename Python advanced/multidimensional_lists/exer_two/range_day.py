def direction_path(row, col, command, steps):
    if command == "right":
        return row, col + steps
    elif command == "left":
        return row, col - steps
    elif command == "up":
        return row - steps, col
    elif command == "down":
        return row + steps, col


def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = 5
field = []

pos_row = 0
pos_col = 0
total_targets = 0
bullet_list = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "A":
            pos_row = row
            pos_col = col
        elif row_elements[col] == 'x':
            total_targets += 1
    field.append(row_elements)

number_commands = int(input())
for _ in range(number_commands):
    current_command = input().split()
    direction = current_command[1]
    if current_command[0] == "move":
        steps = int(current_command[2])
        next_row, next_col = direction_path(pos_row, pos_col, direction, steps)

        if is_inside(next_row, next_col, size) and field[next_row][next_col] == ".":
            field[next_row][next_col] = 'A'
            field[pos_row][pos_col] = "."
            pos_row, pos_col = next_row, next_col

    elif current_command[0] == "shoot":
        bullet_row, bullet_col = direction_path(pos_row, pos_col, direction, 1)
        while is_inside(bullet_row, bullet_col, size):
            if field[bullet_row][bullet_col] == "x":
                bullet_list.append([bullet_row, bullet_col])
                total_targets -= 1
                field[bullet_row][bullet_col] = "."
                break
            bullet_row, bullet_col = direction_path(bullet_row, bullet_col, direction, 1)
        if total_targets == 0:
            break

if total_targets == 0:
    print(f"Training completed! All {len(bullet_list)} targets hit.")
else:
    print(f"Training not completed! {total_targets} targets left.")

if len(bullet_list) > 0:
    for row in bullet_list:
        print(row)
