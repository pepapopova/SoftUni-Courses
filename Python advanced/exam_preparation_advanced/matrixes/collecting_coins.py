def find_next_position(command, row, col):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


def traverse(row, col, size):
    if row < 0:
        row = size - 1
    elif row >= size:
        row = 0
    if col < 0:
        col = size - 1
    elif col >= size:
        col = 0
    return row, col


size = int(input())
matrix = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col


total_coins = 0
path = []
path.append([player_row, player_col])
game_over = False
# commands = {"up", "down", "left", "right"}


while True:
    command = input()
    # if command not in commands:
    #     continue
    player_row, player_col = find_next_position(command, player_row, player_col)
    player_row, player_col = traverse(player_row, player_col, size)
    path.append([player_row, player_col])
    if matrix[player_row][player_col] == "X":
        total_coins //= 2
        game_over = True
        break
    elif matrix[player_row][player_col].isdigit():
        total_coins += int(matrix[player_row][player_col])
        matrix[player_row][player_col] = "P"
    if total_coins >= 100:
        break


if not game_over:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {total_coins} coins.")

print("Your path:")
for step in path:
    print(step)