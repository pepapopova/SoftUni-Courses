command = input()
key_words = 'dog, cat, movie, coding'
coffee_counter = 0

while command != "END":
    if command in key_words.upper():
        coffee_counter += 2
    elif command in key_words:
        coffee_counter += 1
    else:
        coffee_counter += 0
    command = input()
if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)