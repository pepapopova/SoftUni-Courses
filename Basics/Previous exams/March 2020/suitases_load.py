#while cycle - 100/100 correct
trunk_capacity = float(input())
command = input()
count = 0
bags_space = 0
bags_are_loaded = True

while command != "End":
    bag_size = float(command)
    count +=1
    if count % 3 == 0:
        bag_size *= 1.1
    bags_space += bag_size
    if bags_space > trunk_capacity:
        bags_are_loaded = False
        count -= 1
        break
    command = input()

if bags_are_loaded:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {count} suitcases loaded.")
