# def movement(up_space, down_space, col, row, matrix):
#     points = 0
#     for space in range(1, up_space + 1):
#         points += int(matrix[row - space][col])
#     for space in range(1, down_space + 1):
#         points += int(matrix[row + space][col])
#     return points
#
#
# def won_points(aimed_row, aimed_col, board, size):
#     if 0 <= aimed_row < size and 0 <= aimed_col < size:
#         if board[aimed_row][aimed_col] == "B":
#             up_space = aimed_row if aimed_row > 0 else 0
#             down_space = size - aimed_row - 1 if aimed_row <= size - 1 else 0
#             won = movement(up_space, down_space, aimed_col, aimed_row, board)
#             board[aimed_row][aimed_col] = "X"
#             return won
#         return 0
#     return 0

def won_points(aimed_row, aimed_col, board, size):
    total_result = 0
    if 0 <= aimed_row < size and 0 <= aimed_col < size:
        if board[aimed_row][aimed_col] == "B":
            for j in range(size):
                if board[j][aimed_col] != "B":
                    total_result += int(board[j][aimed_col])
            board[aimed_row][aimed_col] = "X"
    return total_result

size = 6
throws = 3

board = []
total_points_won = 0

for row in range(6):
    board.append(input().split())
# board = [input().split() for x in range(size)]


for throw in range(throws):
    aimed_row, aimed_col = eval(input())
    # aimed_row = int(data[0][1::])
    # aimed_col = int(data[1][:-1])
    total_points_won += won_points(aimed_row, aimed_col, board, size)

won_prize = ""

if 100 <= total_points_won <= 199:
    won_prize = "Football"
elif 200 <= total_points_won <= 299:
    won_prize = "Teddy Bear"
elif total_points_won >= 300:
    won_prize = "Lego Construction Set"

if won_prize:
    print(f"Good job! You scored {total_points_won} points, and you've won {won_prize}.")
else:
    print(f"Sorry! You need {abs(total_points_won - 100)} points more to win a prize.")