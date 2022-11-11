size = int(input())
matrix = []

for _ in range(size):
    matrix.append([char for char in input()])

special_symbol = input()
is_found = False

for row_index in range(size):
    if is_found:
        break
    for column_index in range(size):
        if matrix[row_index][column_index] == special_symbol:
            is_found = True
            print(f"({row_index}, {column_index})")


if not is_found:
    print(f"{special_symbol} does not occur in the matrix")
