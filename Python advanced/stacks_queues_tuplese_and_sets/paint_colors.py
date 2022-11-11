from collections import deque
main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

string = deque(input().split())

collected_colors = []

while string:
    first = string.popleft()
    second = string.pop() if string else ""

    result = first + second
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    result = second + first
    if result in main_colors or result in secondary_colors:
        collected_colors.append(result)
        continue

    first = first[:-1]
    second = second[:-1]
    # if there is an empty string and we want to give us it without the last element it will give empty string again
    if first:
        string.insert(len(string)//2, first)
    if second:
        string.insert(len(string)//2, second)

final_colors = []
# for color in collected_colors:
#     if color in main_colors:
#         final_colors.append(color)
#     if color in secondary_colors:
#         if color == "orange":
#             if "red" in collected_colors and "yellow" in collected_colors:
#                 final_colors.append(color)
#         elif color == "purple":
#             if "red" in collected_colors and "blue" in collected_colors:
#                 final_colors.append(color)
#         elif color == "green":
#             if "yellow" in collected_colors and "blue" in collected_colors:
#                 final_colors.append(color)



forming_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["blue", "yellow"]
}

for color in collected_colors:
    if color in main_colors:
        final_colors.append(color)
        continue
    is_collected = True
    for helper_colors in forming_colors[color]:
        if helper_colors not in collected_colors:
            exis_collected = False
            break
    if is_collected:
        final_colors.append(color)

print(final_colors)