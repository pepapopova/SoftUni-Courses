number_snowballs = int(input())
best_value = 0
best_snowball_data = ''

for num in range(number_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_value = (weight / time) ** quality
    if current_value > best_value:
        best_value = int(current_value)
        best_snowball_data = f"{weight} : {time} = {best_value} ({quality})"


print(best_snowball_data)