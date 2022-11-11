aim = 10000
total_steps = 0
reach_goal = True
while total_steps < aim:
    command = input()
    if command == "Going home":
        command = int(input())
        total_steps += int(command)
        if total_steps < aim:
            reach_goal = False
            break
        else:
            break
    total_steps += int(command)

diff = abs(total_steps - aim)
if reach_goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")