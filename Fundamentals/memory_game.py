elements = input().split(" ")
command = input()
moves = 0
condition = False

while command != "end":
    index_guess = list(map(int, command.split(" ")))
    first_index = index_guess[0]
    second_index = index_guess[1]
    moves += 1
    if first_index == second_index or first_index >= len(elements) or second_index >= len(elements) or first_index < 0 or second_index < 0:
        middle_index = len(elements) // 2
        elements.insert(middle_index, "-" + str(moves) + "a")
        elements.insert(middle_index, "-" + str(moves) + "a")
        print(f"Invalid input! Adding additional elements to the board")
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        element_to_remove = elements[first_index]
        elements.remove(element_to_remove)
        elements.remove(element_to_remove)
    elif elements[first_index] != elements[second_index]:
        print("Try again!")
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        condition = True
        break
    command = input()

if not condition:
    print("Sorry you lose :(")
    print(" ".join(elements))