path = input().split("\\")
file = path[-1].split(".")
file_name = file[0]
file_type = file[1]

print(f"File name: {file_name}")
print(f"File extension: {file_type}")