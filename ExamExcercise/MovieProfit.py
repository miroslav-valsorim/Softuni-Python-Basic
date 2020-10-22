movie_name = input()
days = int(input())
number_of_tickets = int(input())
price_for_ticket = float(input())
percentage_for_cinema = int(input())

price_for_all_tickets_for_day = number_of_tickets * price_for_ticket
income_for_period = price_for_all_tickets_for_day * days
percentage = income_for_period * percentage_for_cinema / 100
total_income = income_for_period - percentage

print(f"The profit from the movie {movie_name} is {total_income:.2f} lv.")