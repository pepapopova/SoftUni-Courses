from project.validator import Validator


class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        Validator.raise_error_if_name_is_empty_string(value, "Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        Validator.raise_error_if_num_is_below_restricted(value, 6, "Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}\nLiked movies:\n"
        if len(self.movies_liked) > 0:
            result += "\n".join([movie.details() for movie in self.movies_liked]) + '\n'
        else:
            result += "No movies liked." + '\n'
        result += "Owned movies:\n"
        if len(self.movies_owned) > 0:
            result += '\n'.join([movie.details() for movie in self.movies_owned])
        else:
            result += "No movies owned."
        return result.strip()



