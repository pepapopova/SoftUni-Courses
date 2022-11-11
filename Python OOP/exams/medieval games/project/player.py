from project.validator import Validator


class Player:
    used_names = set()

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_error_if_name_is_empty_string(value, "Name not valid!")
        if value in self.used_names:
            raise Exception(f"Name {value} is already used!")
        self.used_names.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_error_if_num_is_below_restricted(value, 12, "The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        Validator.raise_error_if_num_is_not_in_range(value, 0, 100, "Stamina not valid!")
        self.__stamina = value

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    @property
    def need_sustenance(self):
        return self.stamina < 100