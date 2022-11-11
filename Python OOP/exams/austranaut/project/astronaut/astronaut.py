from abc import ABC, abstractmethod

from project.core.validator import Validator


class Astronaut(ABC):
    OXYGEN_PER_BREATHE = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_len_is_less_than(value.strip(), 1,
                                            "Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= self.OXYGEN_PER_BREATHE

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def details(self):
        backpack_details = ', '.join(self.backpack) if len(self.backpack) > 0 else 'None'
        result = f'Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {backpack_details}'
        return result

