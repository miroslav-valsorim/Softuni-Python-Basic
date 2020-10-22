#Бюджет на филма – реално число в диапазона [100 000.0… 2 000 000.0]
# Дестинация – текст, с възможности "Dubai", "Sofia" и "London"
# Сезон – текст, с възможности "Summer" и "Winter"
#. Брой дни – цяло число в диапазона [1… 40]

movie_budget = float(input())
destination = input()
season = input()
days = int(input())

price = 0
sale = 0

if destination == "Dubai":
    if season == "Summer":
        price = 40000
    elif season == "Winter":
        price = 45000
elif destination == "Sofia":
    if season == "Summer":
        price = 12500
    elif season == "Winter":
        price = 17000
elif destination == "London":
    if season == "Summer":
        price = 20250
    elif season == "Winter":
        price = 24000

total_price = price * days

if destination == "Dubai":
    sale = total_price - total_price * 30 / 100
elif destination == "Sofia":
    sale = total_price + total_price * 25 / 100
else:
    sale = total_price

diff = sale - movie_budget
if sale <= movie_budget:
    print(f"The budget for the movie is enough! We have {abs(diff):.2f} leva left!")
else:
    print(f"The director needs {abs(diff):.2f} leva more!")