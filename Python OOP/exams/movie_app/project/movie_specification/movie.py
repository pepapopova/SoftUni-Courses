from abc import ABC, abstractmethod

from project.validator import Validator


class Movie(ABC):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction

        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        Validator.raise_error_if_name_is_empty_string(value, "The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        Validator.raise_error_if_num_is_below_restricted(value, 1888, "Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if value.__class__.__name__ != 'User':
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @abstractmethod
    def details(self):
        pass