from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

total_matches = 0

while females and males:
    current_male = males.pop()
    if current_male <= 0:
        continue
    elif current_male % 25 == 0:
        males.pop()
        continue
    current_female = females.popleft()
    if current_female <= 0:
        males.append(current_male)
        continue
    elif current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue
    if current_female != current_male:
        males.append(current_male - 2)
    else:
        total_matches += 1

reversed_males = reversed(males)

print(f"Matches: {total_matches}")
if males:
    print(f"Males left: {', '.join([str(x) for x in reversed_males])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")
