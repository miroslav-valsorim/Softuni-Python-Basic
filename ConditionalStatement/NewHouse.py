type_flower = input()
number_of_flowers = int(input())
money = int(input())

rose = 5
dahlia = 3.80
tulip = 2.80
narcissus = 3
gladiolus = 2.50

price = 0
if type_flower == "Roses":
    if number_of_flowers > 80:
        price = rose * number_of_flowers
        price -= price * 10 / 100
    elif number_of_flowers <= 80:
        price = rose * number_of_flowers
elif type_flower == "Dahlias":
    if number_of_flowers > 90:
        price = dahlia * number_of_flowers
        price -= price * 15 / 100
    elif number_of_flowers <= 90:
        price = dahlia * number_of_flowers
elif type_flower == "Tulips":
    if number_of_flowers > 80:
        price = tulip * number_of_flowers
        price -= price * 15 / 100
    elif number_of_flowers <= 80:
        price = tulip * number_of_flowers
elif type_flower == "Narcissus":
    if number_of_flowers < 120:
        price = narcissus * number_of_flowers
        price += price * 15 / 100
    elif number_of_flowers >= 120:
        price = narcissus * number_of_flowers
elif type_flower == "Gladiolus":
    if number_of_flowers < 80:
        price = gladiolus * number_of_flowers
        price += price * 20 / 100
    elif number_of_flowers >= 80:
        price = gladiolus * number_of_flowers

if price <= money:
    money_left = money - price
    print(f"Hey, you have a great garden with {number_of_flowers} {type_flower} and {money_left:.2f} leva left.")
elif price > money:
    money_needed = price - money
    print(f"Not enough money, you need {money_needed:.2f} leva more.")