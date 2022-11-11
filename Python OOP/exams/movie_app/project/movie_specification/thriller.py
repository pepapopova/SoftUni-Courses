from project.movie_specification.movie import Movie
from project.validator import Validator


class Thriller(Movie):
    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validator.raise_error_if_num_is_below_restricted(value, 16, 'Thriller movies must be restricted for audience under 16 years!')
        self.__age_restriction = value

    def details(self):
        return f'{self.__class__.__name__} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, \
Likes:{self.likes}, Owned by:{self.owner.username}'
