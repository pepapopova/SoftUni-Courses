command = input()
followers_dict = {}

while command != "Log out":
    current_command = command.split(": ")
    username = current_command[1]
    if current_command[0] == "New follower":
        if username not in followers_dict:
            followers_dict[username] = {'Likes': 0, 'Comments': 0}
    elif current_command[0] == "Like":
        likes = int(current_command[2])
        if username not in followers_dict:
            followers_dict[username] = {'Likes': 0, 'Comments': 0}
            followers_dict[username]['Likes'] = likes
        else:
            followers_dict[username]['Likes'] += likes
    elif current_command[0] == "Comment":
        if username not in followers_dict:
            followers_dict[username] = {'Likes': 0, 'Comments': 0}
            followers_dict[username]['Comments'] = 1
        else:
            followers_dict[username]['Comments'] += 1
    elif current_command[0] == "Blocked":
        if username in followers_dict:
            del followers_dict[username]
        else:
            print(f"{username} doesn't exist.")
    command = input()

followers_count = len(followers_dict)
print(f"{followers_count} followers")
for follower in followers_dict:
    reactions = followers_dict[follower]['Likes'] + followers_dict[follower]['Comments']
    print(f"{follower}: {reactions}")