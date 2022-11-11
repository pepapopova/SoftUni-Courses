import sys

number_movies = int(input())
counter = 0
total_ratings = 0
max_rating = -sys.maxsize
min_rating = sys.maxsize
highest_rating_movie = ""
lowest_rating_movie = ""
for movie in range(number_movies):
    movie_name = input()
    movie_rating = float(input())
    counter += 1
    total_ratings += movie_rating
    if movie_rating > max_rating:
        max_rating = movie_rating
        highest_rating_movie = movie_name
    if movie_rating < min_rating:
        min_rating = movie_rating
        lowest_rating_movie = movie_name

average_rating = total_ratings / counter

print(f"{highest_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{lowest_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
