jobs = [int(x) for x in input().split(", ")]
index = int(input())
break_point = jobs[index]
total_cycles = 0

for cycle in jobs:
    if cycle < break_point:
        total_cycles += cycle

for ind in range(index + 1):
    if jobs[ind] == break_point:
        total_cycles += break_point

print(total_cycles)