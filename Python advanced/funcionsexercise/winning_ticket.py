tickets = input().split(", ")
count = 0
is_winning = False
special_symbols = '@#$^'

for ticket in tickets:
    if len(ticket) != 20:
        print(f"invalid ticket")

        # for char in ticket:
        #     if char in '@#$^':
        #         count += 1
        #         if count == 20:
        #             print(f"ticket {ticket} - 10{char} Jackpot!")
    left_half = ticket[:10]
    right_half = ticket[10:]
    for winning_symbol in special_symbols:
        for repetition in range(10, 5, -1):
            winning_characters = winning_symbol * repetition
            if winning_characters in left_half and winning_characters in right_half:
                if len(winning_characters) == 10:
                    print(f'ticket "{ticket}" - 10{winning_symbol} Jackpot!')
                    break
                elif 6 <= len(winning_characters) <= 9:
                    print(f'ticket "{ticket}" - {repetition}{winning_symbol}')
                else:
                    print(f'ticket "{ticket}" - no match')
