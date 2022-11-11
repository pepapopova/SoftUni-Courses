rows = int(input())
for row in range(1, rows + 1):
    current_row = [x for x in input()]
    for element in current_row:
        if element == "k":
            kate_position = current_row.index(element)
            kate_row = row
        if element == " ":
            way = current_row.index(element)
            current_row[kate_position], current_row[way] = current_row[way], current_row[kate_position]