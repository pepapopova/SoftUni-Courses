username = input()
password = input()
entry_password = input()
while entry_password != password:
    entry_password = input()

print(f"Welcome {username}!")