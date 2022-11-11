def sum_corresponding(row, col, board, size):
    total_sum = int(board[row][size - 1]) + int(board[row][0]) + \
        int(board[0][col]) + int(board[size - 1][col])
    return total_sum


def find_score(row, col, board, size):
    if 0 <= row < size and 0 <= col < size:
        if board[row][col] == "T":
            result = sum_corresponding(row, col, board, size) * 3
        elif board[row][col] == "D":
            result = sum_corresponding(row, col, board, size) * 2
        elif board[row][col] == "B":
            result = 501
        else:
            result = int(board[row][col])
    else:
        result = 0
    return result


size = 7
board = []
score_player1 = 501
score_player2 = 501
player_1_throws = 0
player2_throws = 0

first_player, second_player = input().split(", ")
for row in range(size):
    board.append(input().split())

turn = 0


while score_player1 > 0 and score_player2 > 0:
    player_1_throws += 1
    current_player = first_player
    data = input().split(", ")
    first_player_row = int(data[0][1::])
    first_player_col = int(data[1][:-1])

    score_player1 -= find_score(first_player_row, first_player_col, board, size)
    if score_player1 <= 0:
        break

    player2_throws += 1
    current_player = second_player
    data = input().split(", ")
    second_player_row = int(data[0][1::])
    second_player_col = int(data[1][:-1])

    score_player2 -= find_score(second_player_row, second_player_col, board, size)
    if score_player2 <= 0:
        break


print(f"{current_player} won the game with {player_1_throws if current_player == first_player else player2_throws} throws!")