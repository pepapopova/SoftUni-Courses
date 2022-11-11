from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.movie import Movie
from project.user import User


class MovieApp():
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if self.__find_user_by_username(username):
            raise Exception("User already exists!")
        user = User(username, age)
        self.users_collection.append(user)
        return f"{user.username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)
        if not user:
            raise Exception("This user does not exist!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception(f"Movie already added to the collection!")
        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{user.username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **movie_attributes):
        user = self.__find_user_by_username(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for attribute, value in movie_attributes.items():
            setattr(movie, attribute, value)
        return f"{user.username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner != user:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)
        if movie.owner == user:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user_by_username(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        result = ''
        for movie in sorted(self.movies_collection, key=lambda m: (-m.year, m.title)):
            result += movie.details() + '\n'

        return result.strip()

    def __str__(self):
        users_result = f"All users: {', '.join([u.username for u in self.users_collection])}" if len(self.users_collection) > 0 else "All users: No users."
        movies_result = f"All movies: {', '.join([m.title for m in self.movies_collection])}" if len(self.movies_collection) > 0 else "All movies: No movies."
        return users_result + '\n' + movies_result

    def __find_user_by_username(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user


movie_app = MovieApp()
print(movie_app.register_user('Martin', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Martin', movie))
print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))
user2 = movie_app.users_collection[1]
movie2 = Action('Free Guy', 2021, user2, 16)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.like_movie('Alexandra', movie))
print(movie_app.dislike_movie('Martin', movie2))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.delete_movie('Alexandra', movie2))
movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.display_movies())
print(movie_app)
print(user)