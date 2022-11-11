movie_name = input()
number_of_days = int(input())
number_tickets = int(input())
price_of_ticket = float(input())
percent_for_the_cinema = int(input())

profit = number_tickets * price_of_ticket
profit *= number_of_days

cost_for_the_cinema = profit * percent_for_the_cinema / 100
profit -= cost_for_the_cinema
print(f"The profit from the movie {movie_name} is {profit:.2f} lv.")
