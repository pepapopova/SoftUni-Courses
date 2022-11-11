from collections import deque

first_player, second_player = input().split(", ")
size = 6
board = []
players = deque(first_player, second_player)
for row in range(size):
    board.append(input().split())

while True:
    current_player = players.popleft()
    players.append(current_player)
    first_row, first_col = eval(input())
    if board[first_row][first_col] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif board[first_row][first_col] == "T":
        print(f"{current_player} is out of the game! The winner is {players.pop()}.")
        break
    elif board[first_row][first_col] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        takes_rest = True
