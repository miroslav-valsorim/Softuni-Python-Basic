budget = int(input())
season = input()
fishers = int(input())

rent = 0

if season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Spring":
    rent = 3000
elif season == "Winter":
    rent = 2600

if fishers <= 6:
    rent -= rent * 10 / 100
elif 7 < fishers <= 11:
    rent -= rent * 15 / 100
elif fishers >= 12:
    rent -= rent * 25 / 100

if season != "Autumn" and fishers % 2 == 0:
    rent -= rent * 5 / 100
else:
    rent = rent

if rent <= budget:
    last_price = budget - rent
    print(f"Yes! You have {last_price:.2f} leva left.")
elif rent > budget:
    last_price = rent - budget
    print(f"Not enough money! You need {last_price:.2f} leva.")