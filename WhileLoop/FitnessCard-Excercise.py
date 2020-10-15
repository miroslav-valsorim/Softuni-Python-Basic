money_available = float(input())
gender = input()
age = int(input())
type_of_sport = input()

price = 0

if gender == "f":
    if type_of_sport == "Gym":
        price = 35
    elif type_of_sport == "Boxing":
        price = 37
    elif type_of_sport == "Yoga":
        price = 42
    elif type_of_sport == "Zumba":
        price = 31
    elif type_of_sport == "Dances":
        price = 53
    elif type_of_sport == "Pilates":
        price = 37

elif gender == "m":
    if type_of_sport == "Gym":
        price = 42
    elif type_of_sport == "Boxing":
        price = 41
    elif type_of_sport == "Yoga":
        price = 45
    elif type_of_sport == "Zumba":
        price = 34
    elif type_of_sport == "Dances":
        price = 51
    elif type_of_sport == "Pilates":
        price = 39

if age <= 19:
    price -= price * 20 / 100

if money_available >= price:
    print(f"You purchased a 1 month pass for {type_of_sport}.")
else:
    diff = money_available - price
    print(f"You don't have enough money! You need ${abs(diff):.2f} more.")