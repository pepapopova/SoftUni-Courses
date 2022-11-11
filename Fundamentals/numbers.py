sequence = list(map(int, input().split(" ")))
average_value = sum(sequence) / len(sequence)
new_list = []
condition = True

new_list = [ num for num in sequence if num > average_value ]

new_list = sorted(new_list, reverse=True)
if len(new_list) > 5:
    del new_list[5:]
elif len(new_list) <= 0:
    print("No")
    condition = False

if condition:
    new_list_as_string = list(map(str, new_list))
    print(" ".join(new_list_as_string))