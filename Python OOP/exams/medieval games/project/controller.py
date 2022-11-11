class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player.name)
        return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

        #self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if not player:
            return
        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return
        index, supply = self.__find_supply_by_index(sustenance_type)
        if supply is None:
            return Exception(f"There are no {sustenance_type.lower()} supplies left!")
        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        player.stamina = min(supply.energy + player.stamina, 100)
        self.supplies.pop(index)
        return f"{player.name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self.__find_player_by_name(first_player_name)
        player2 = self.__find_player_by_name(second_player_name)
        result = ''
        if player1.stamina == 0:
            result += f"Player {first_player_name} does not have enough stamina.\n"
        if player2.stamina == 0:
            result += f"Player {second_player_name} does not have enough stamina."
        if result:
            return result.strip()

        first_player = player1 if player1.stamina > player2.stamina else player2
        second_player = player2 if player2.stamina < player1.stamina else player1

        second_player.stamina -= (0.5 * first_player.stamina)
        if second_player.stamina <= 0:
            second_player.stamina = 0
            return f"Winner: {first_player.name}"

        first_player.stamina -= (0.5 * second_player.stamina)
        if first_player.stamina <= 0:
            first_player.stamina = 0
            return f"Winner: {second_player.name}"

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player, 'Food')
            self.sustain(player, 'Drink')

    def __str__(self):
        result = ''
        #return = '\n'.join([str(x) for x in self.players]) + '\n' + '\n'.join([x.details() for x in self.supplies])
        for player in self.players:
            result += str(player) + '\n'
        for supply in self.supplies:
            result += supply.details() + '\n'
        return result.strip()

    def __find_player_by_name(self, username):
        for player in self.players:
            if player.name == username:
                return player

    def __find_supply_by_index(self, sustenance_type):
        for index in range(len(self.supplies) -1, -1, -1):
            supply = self.supplies[index]
            if supply.__class__.__name__ == sustenance_type:
                return (index, supply)
            return (-1, None)