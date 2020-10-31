number_of_people = int(input())
season = input()

price = 0

if season == "spring":
    if number_of_people <= 5:
        price = 50.00
    elif number_of_people > 5:
        price = 48.00
elif season == "summer":
    if number_of_people <= 5:
        price = 48.50
    elif number_of_people > 5:
        price = 45.00
elif season == "autumn":
    if number_of_people <= 5:
        price = 60.00
    elif number_of_people > 5:
        price = 49.50
elif season == "winter":
    if number_of_people <= 5:
        price = 86.00
    elif number_of_people > 5:
        price = 85.00

total = price * number_of_people

if season == "summer":
    total -= total * 15 / 100
elif season == "winter":
    total += total * 8 / 100
else:
    total = total

print(f"{total:.2f} leva.")

