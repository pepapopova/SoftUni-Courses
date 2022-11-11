# def get_next_col(alice_row, alice_col, command):
#     if command == 'right':
#         return alice_row, alice_col + 1
#     elif command == "left":
#         return alice_row, alice_col - 1
#     elif command == "up":
#         return alice_row - 1, alice_col
#     elif command == "left":
#         return alice_row + 1, alice_col

size = int(input())

matrix = []

alice_row = 0
alice_col = 0
for row in range(size):
    current_element = input().split()
    for col in range(size):
        if current_element[col] == "A":
            alice_col = col
            alice_row = row
    matrix.append(current_element)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}
collected_bags = 0
has_won = False

while True:
    command = input()
    matrix[alice_row][alice_col] = "*"
    alice_row, alice_col = directions[command](alice_row, alice_col)
    # alice_row, alice_col = get_next_col(alice_row, alice_col, command)
    if alice_row < 0 or alice_col < 0 or alice_row >= size or alice_col >= size:
        break
    if matrix[alice_row][alice_col] == "R":
        matrix[alice_row][alice_col] = "*"
        break
    if matrix[alice_row][alice_col].isdigit():
        collected_bags += int(matrix[alice_row][alice_col])
    matrix[alice_row][alice_col] = '*'
    if collected_bags >= 10:
        has_won = True
        break

if has_won:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=" ")