count = int(input())
my_dict = {}

for n in range(count):
    key = input()
    value = input()
    if key not in my_dict:
        my_dict[key] = []
    my_dict[key].append(value)

for word in my_dict:
    print(f'{word} - {", ".join(my_dict[word])}')
