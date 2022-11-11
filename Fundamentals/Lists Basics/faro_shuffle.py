deck = input().split(' ')
shuffles = int(input())
middle_index = len(deck) // 2
first_half = deck[:middle_index]
second_half = deck[middle_index:]
new_deck = list()
for k in range(shuffles):
    new_deck.clear()
    for i in range(len(first_half)):
        new_deck.append(first_half[i])
        new_deck.append(second_half[i])
    first_half = new_deck[:middle_index]
    second_half = new_deck[middle_index:]
print(new_deck)