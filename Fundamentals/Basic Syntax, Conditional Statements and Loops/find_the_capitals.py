string = input()
list1 = []

for i in range(len(string)):
    if string[i].isupper():
        list1.append(i)

print(list1)
