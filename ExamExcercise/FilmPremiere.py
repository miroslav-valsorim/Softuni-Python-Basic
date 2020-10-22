projection = input()
movie_packet = input()
number_of_tickets = int(input())

price = 0

if projection == "John Wick":
    if movie_packet == "Drink":
        price = 12
    elif movie_packet == "Popcorn":
        price = 15
    elif movie_packet == "Menu":
        price = 19
elif projection == "Star Wars":
    if movie_packet == "Drink":
        price = 18
    elif movie_packet == "Popcorn":
        price = 25
    elif movie_packet == "Menu":
        price = 30
elif projection == "Jumanji":
    if movie_packet == "Drink":
        price = 9
    elif movie_packet == "Popcorn":
        price = 11
    elif movie_packet == "Menu":
        price = 14

total = price * number_of_tickets

if projection == "Star Wars" and number_of_tickets >= 4:
    discount = total - total * 30 / 100
elif projection == "Jumanji" and number_of_tickets == 2:
    discount = total - total * 15 / 100
else:
    discount = total

print(f"Your bill is {discount:.2f} leva.")
