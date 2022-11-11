lines = input().split("|")

result = []

for index in range(len(lines) - 1, -1, -1):
    current_elements = lines[index].strip().split()
    result.extend(current_elements)

print(" ".join(result))