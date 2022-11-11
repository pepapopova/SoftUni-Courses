first_player, second_player = input().split(", ")
size = 6
board = []
counter_first = 0
counter_second = 0

for row in range(size):
    row_elements = input().split()
    board.append(row_elements)

while True:
    first_row, first_col = eval(input())
    if counter_first == 1:
        counter_first = 0
        pass
    else:
        if board[first_row][first_col] == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        elif board[first_row][first_col] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        elif board[first_row][first_col] == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            counter_first = 1

    second_row, second_col = eval(input())
    if counter_second == 1:
        counter_second = 0
        pass
    else:
        if board[second_row][second_col] == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        elif board[second_row][second_col] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        elif board[second_row][second_col] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            counter_second = 1
