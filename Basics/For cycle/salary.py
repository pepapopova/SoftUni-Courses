tabs = int(input())
salary = int(input())
fine_face = 150
fine_insta = 100
fine_reddit = 50
total_fine = 0

for n in range(tabs):
    if total_fine >= salary:
        break
    current_tab = input()
    if current_tab == "Facebook":
        total_fine += fine_face
    elif current_tab == "Instagram":
        total_fine += fine_insta
    elif current_tab == "Reddit":
        total_fine += fine_reddit

if total_fine >= salary:
    print(f"You have lost your salary.")
else:
    diff = salary - total_fine
    print(f"{diff:.0f}")