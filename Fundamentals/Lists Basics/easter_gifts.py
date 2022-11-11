gifts = input().split(" ")
command = input().split(" ")

while command[0] != "No":
    if command[0] == "OutOfStock":
        current_gift = command[1]
        for i in range(len(gifts)):
            if current_gift == gifts[i]:
                gifts[i] = "None"
    elif command[0] == "Required":
        current_gift = command[1]
        for i in range(len(gifts)):
            if int(command[2]) == i:
                gifts[i] = current_gift
    elif command[0] == "JustInCase":
        current_gift = command[1]
        gifts.pop()
        gifts.append(current_gift)
    command = input().split(" ")

for i in range(len(gifts)):
    if "None" in gifts:
        gifts.remove("None")

gifts = " ".join(gifts)
print(gifts)