from abc import ABC, abstractmethod

from project.validator import Validator


class Supply(ABC):
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_if_name_is_empty_string(value, "Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        Validator.raise_error_if_num_is_les_than_0(value, "Energy cannot be less than zero.")
        self.__energy = value

    @abstractmethod
    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
