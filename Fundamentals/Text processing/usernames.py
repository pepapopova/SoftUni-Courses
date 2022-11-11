usernames = input().split(", ")

for username in usernames:
    condition = username.isalnum() or "_" in username or "-" in username
    if 3 <= len(username) <= 16 and condition:
        print(username)