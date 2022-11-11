#while cycle - 100/100 correct
command = input()
max_goals = 0
done_hattrick = False
while command != "END":
    goals = int(input())
    if goals >= 10:
        best_player = command
        max_goals = goals
        done_hattrick = True
        break
    if goals > max_goals:
        max_goals = goals
        best_player = command
    if max_goals >= 3:
        done_hattrick = True
    command = input()


print(f"{best_player} is the best player!")
if done_hattrick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
