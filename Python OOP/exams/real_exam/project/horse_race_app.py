from project.horse_factory import HorseFactory
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []
        self.horse_factory = HorseFactory()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if any(h.name == horse_name for h in self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")
        try:
            horse = self.horse_factory.create_horse(horse_type, horse_name, horse_speed)
            # we can make check if car is None
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."
        except RuntimeError:
            pass
        # horse = self.__create_horse_by_type(horse_type, horse_name, horse_speed)

        # if not horse:
        #     return

        # for horse in self.horses:
        #     if horse.name == horse_name:
        #         return f"Horse {horse_name} has been already added!"
        #
        # self.horses.append(horse)
        # return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if any(j.name == jockey_name for j in self.jockeys):
            return f"Jockey {jockey_name} has been already added!"

        jockey = Jockey(jockey_name, age)
        if not jockey:
            return
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

        # if not jockey:
        #     return

        # jockey = Jockey(jockey_name, age)
        # if not jockey:
        #     return
        # for jockey in self.jockeys:
        #     if jockey.name == jockey_name:
        #         raise Exception(f"Jockey {jockey_name} has been already added!")
        #
        # self.jockeys.append(jockey)
        # return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if any(r.race_type == race_type for r in self.horse_races):
            raise Exception(f"Race {race_type} has been already created!")

        horse_race = HorseRace(race_type)
        if not horse_race:
            return
        self.horse_races.append(horse_race)
        return f"Race {race_type} is created."

        # horse_race = HorseRace(race_type)
        # if not horse_race:
        #     return
        #
        # for race in self.horse_races:
        #     if race.race_type == race_type:
        #         raise Exception(f"Race {race_type} has been already created!")
        #
        # self.horse_races.append(horse_race)
        # return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        # horse = [h for h in self.horses if h.__class__.__name__ == horse_type][-1]
        horse = self.__find_the_last_horse_by_type(horse_type)
        if not horse or horse.is_taken:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        self.horses.remove(horse)
        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race_by_race_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.__find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."


    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_race_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda j: j.horse.speed, reverse=True)[0]

        return f"The winner of the {race_type} race, " \
               f"with a speed of {winner.horse.speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def __find_the_last_horse_by_type(self, horse_type):
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type:
                return horse

    def __find_race_by_race_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race