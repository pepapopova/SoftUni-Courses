def next_position(r, c, command):
    if command == "right":
        return r, c + 1
    elif command == "left":
        return r, c - 1
    elif command == "up":
        return r - 1, c
    elif command == "down":
        return r + 1, c


def get_children(r, c):
    children = [
        [r - 1, c],
        [r + 1, c],
        [r, c + 1],
        [r, c - 1]
    ]
    return children


presents = int(input())
size = int(input())

neighbourhood = []
santa_row = 0
santa_col = 0
nice_kids = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "S":
            santa_row = row
            santa_col = col
        elif row_elements[col] == "V":
            nice_kids += 1

    neighbourhood.append(row_elements)

counter_kids = 0
while True:
    command = input()
    if command == "Christmas morning":
        break
    neighbourhood[santa_row][santa_col] = "-"
    santa_row, santa_col = next_position(santa_row, santa_col, command)

    if neighbourhood[santa_row][santa_col] == "V":
        presents -= 1
        counter_kids += 1
    elif neighbourhood[santa_row][santa_col] == "C":
        presents_delivery = get_children(santa_row, santa_col)
        for cookie_row, cookie_col in presents_delivery:
            if neighbourhood[cookie_row][cookie_col] != "-":
                presents -= 1
            if neighbourhood[cookie_row][cookie_col] == "V":
                counter_kids += 1
            neighbourhood[cookie_row][cookie_col] = "-"

    neighbourhood[santa_row][santa_col] = "S"
    if presents == 0:
        break

if presents <= 0 and (nice_kids - counter_kids) > 0:
    print("Santa ran out of presents!")

for row in neighbourhood:
    print(*row, sep=" ")

if nice_kids - counter_kids > 0:
    print(f"No presents for {nice_kids - counter_kids} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")