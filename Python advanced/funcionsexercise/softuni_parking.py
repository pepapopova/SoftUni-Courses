number_commands = int(input())
registered_names = {}

for n in range(number_commands):
    data = input().split(" ")
    command = data[0]
    username = data[1]
    if command == "register":
        if username not in registered_names:
            registered_names[username] = data[2]
            print(f"{username} registered {data[2]} successfully")
        else:
            print(f"ERROR: already registered with plate number {registered_names[username]}")
    elif command == "unregister":
        if username not in registered_names:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            registered_names.pop(username)

for username, plate in registered_names.items():
    print(f"{username} => {plate}")
