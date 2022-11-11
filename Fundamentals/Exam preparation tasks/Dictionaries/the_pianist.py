number_pieces = int(input())
pieces_dict = {}

for n in range(number_pieces):
    current_piece = input().split("|")
    piece = current_piece[0]
    composer = current_piece[1]
    key = current_piece[2]
    pieces_dict[piece] = {}
    pieces_dict[piece]['Composer'] = composer
    pieces_dict[piece]['Key'] = key

command = input()

while command != "Stop":
    current_command = command.split("|")
    current_piece = current_command[1]
    if current_command[0] == "Add":
        current_composer = current_command[2]
        current_key = current_command[3]
        if current_piece in pieces_dict:
            print(f"{current_piece} is already in the collection!")
        else:
            pieces_dict[current_piece] = {}
            pieces_dict[current_piece]['Composer'] = current_composer
            pieces_dict[current_piece]['Key'] = current_key
            print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
    elif current_command[0] == "Remove":
        if current_piece in pieces_dict:
            print(f"Successfully removed {current_piece}!")
            del pieces_dict[current_piece]
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")
    elif current_command[0] == "ChangeKey":
        new_key = current_command[2]
        if current_piece in pieces_dict:
            pieces_dict[current_piece]['Key'] = new_key
            print(f"Changed the key of {current_piece} to {new_key}!")
        else:
            print(f"Invalid operation! {current_piece} does not exist in the collection.")
    command = input()

for piece in pieces_dict:
    print(f"{piece} -> Composer: {pieces_dict[piece]['Composer']}, Key: {pieces_dict[piece]['Key']}")