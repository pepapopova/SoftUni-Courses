def check_win_black(matrix, row, col):
    if 0 <= col - 1 < len(matrix):
        if matrix[row + 1][col - 1] == "w":
            return row + 1, col - 1
    if 0 <= col + 1 < len(matrix):
        if matrix[row + 1][col + 1] == "w":
            return row + 1, col + 1
    return False


def check_win_white(matrix, row, col):
    if 0 <= col - 1 < len(matrix):
        if matrix[row - 1][col - 1] == "b":
            return row - 1, col - 1
    if 0 <= col + 1 < len(matrix):
        if matrix[row - 1][col + 1] == "b":
            return row - 1, col + 1
    return False


size = 8
legend = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h"
}

rows_legend = {
    0: 8,
    1: 7,
    2: 6,
    3: 5,
    4: 4,
    5: 3,
    6: 2,
    7: 1
}

board = []
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "b":
            black_row, black_col = row, col
        elif row_elements[col] == "w":
            white_row, white_col = row, col
    board.append(row_elements)

while True:

    if check_win_white(board, white_row, white_col):
        win_row, win_col = check_win_white(board, white_row, white_col)
        print(f"Game over! White win, capture on {legend[win_col]}{rows_legend[win_row]}.")
        break

    white_row -= 1
    board[white_row][white_col] = "w"

    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {legend[white_col]}{rows_legend[white_row]}.")
        break

    if check_win_black(board, black_row, black_col):
        win_row, win_col = check_win_black(board, black_row, black_col)
        print(f"Game over! Black win, capture on {legend[win_col]}{rows_legend[win_row]}.")
        break

    black_row += 1
    board[black_row][black_col] = "b"

    if black_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {legend[black_col]}{rows_legend[black_row]}.")
        break

