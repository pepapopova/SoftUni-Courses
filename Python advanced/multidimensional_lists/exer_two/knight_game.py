def find_count(board, row, col):
    moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
        [row + 1, col - 2],
        [row + 1, col + 2]

    ]

    result = 0
    for r, c in moves:
        if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == 'K':
            result += 1
    return result


board_size = int(input())
matrix = []
removed_knight_counter = 0

for _ in range(board_size):
    matrix.append(list(input()))

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(board_size):
        for col in range(board_size):
            if matrix[row][col] == "0":
                continue
            count = find_count(matrix, row, col)
            if count > best_count:
                best_count = count
                knight_col = col
                knight_row = row
    if best_count == 0:
        break
    matrix[knight_row][knight_col] = '0'
    removed_knight_counter += 1

print(removed_knight_counter)