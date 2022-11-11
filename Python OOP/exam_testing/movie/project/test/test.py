from project.movie import Movie

from unittest import TestCase, main


class MovieTest(TestCase):
    NAME = 'Walking dead'
    YEAR = 2012
    RATING = 8.7
    ACTORS = ['Brad Pit', 'Jason Mamoa']

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test_innit_when_all_attributes_are_correct(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_movie_name_setter_raises_error_when_empty_string(self):
        with self.assertRaises(ValueError) as error:
            Movie('', self.YEAR, self.RATING)
        self.assertEqual("Name cannot be an empty string!", str(error.exception))

    def test_movie_year_raises_error_when_below_1887(self):
        with self.assertRaises(ValueError) as error:
            Movie(self.NAME, 1870, self.RATING)
        self.assertEqual("Year is not valid!", str(error.exception))

    def test_add_actor_when_actor_is_not_in_movie_actors(self):
        self.movie.add_actor('Orlando Blum')
        self.assertEqual(['Orlando Blum'], self.movie.actors)

    def test_add_actor_when_actor_is_already_in_movie_actors(self):
        actor = 'Brad Pit'
        self.movie.actors = ['Brad Pit']
        result = self.movie.add_actor(actor)
        self.assertEqual(f"{actor} is already added in the list of actors!", result)

    def test_greater_than_when_first_movie__rating_greater(self):
        movie2 = Movie('Hit', 1999, 7)
        result = self.movie > movie2
        self.assertEqual(f'"{self.movie.name}" is better than "{movie2.name}"', result)

    def test_greater_than_when_other_movie_rating_is_greater(self):
        movie2 = Movie('Hit', 2021, 9)
        result = self.movie > movie2
        self.assertEqual(f'"{movie2.name}" is better than "{self.movie.name}"', result)

    def test_if_repr_gives_proper_result(self):
        self.movie.add_actor('Brad Pit')
        actors = ['Brad Pit']
        result = repr(self.movie)
        expected_result = f"Name: {self.NAME}\n" \
               f"Year of Release: {self.YEAR}\n" \
               f"Rating: {self.RATING:.2f}\n" \
               f"Cast: {', '.join(actors)}"
        self.assertEqual(expected_result, result)