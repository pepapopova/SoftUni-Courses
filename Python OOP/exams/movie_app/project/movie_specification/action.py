from project.movie_specification.movie import Movie
from project.validator import Validator


class Action(Movie):
    def __init__(self, title, year, owner, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        Validator.raise_error_if_num_is_below_restricted(value, 12, 'Action movies must be restricted for audience under 12 years!')
        self.__age_restriction = value

    def details(self):
        return f'Action - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, \
Likes:{self.likes}, Owned by:{self.owner.username}'
