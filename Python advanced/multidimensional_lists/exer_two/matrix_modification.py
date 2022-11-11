def validation(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True


size = int(input())

matrix = []
for row in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()
    if command[0] == "END":
        for row in matrix:
            print(*row, sep= " ")
        break
    elif command[0] == "Add":
        row, col, value = [int(x) for x in command[1:]]
        if validation(row, col, size):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif command[0] == "Subtract":
        row, col, value = [int(x) for x in command[1:]]
        if validation(row, col, size):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")
