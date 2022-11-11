notebook = input().split(" ")

less_than_seven = False
count_team_a = 11
count_team_b = 11
new_list = []
red_cards_list = []

for card in notebook:
    if card not in red_cards_list:
        red_cards_list.append(card)
        card.split("-")
        if "A" in card:
            count_team_a -= 1
        if "B" in card:
            count_team_b -= 1
        if count_team_a < 7 or count_team_b < 7:
            less_than_seven = True
            break

print(f"Team A - {count_team_a}; Team B - {count_team_b}")
if less_than_seven:
    print("Game was terminated")