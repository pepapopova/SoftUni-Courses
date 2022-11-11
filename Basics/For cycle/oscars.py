actor_name = str(input())
academy_points = float(input())
jury = int(input())
total_jury_points = 0

for person in range(jury):
    current_jury = str(input())
    jury_points = float(input())
    total_jury_points += len(current_jury) * jury_points / 2
    total_points = academy_points + total_jury_points
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    diff = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")