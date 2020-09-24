from math import floor
from math import ceil

days = int(input())
food_in_kg = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog = days * dog_food_per_day
cat = days * cat_food_per_day
turtle = days * turtle_food_per_day / 1000
all_pets = dog + cat + turtle

if food_in_kg >= all_pets:
    food_left = food_in_kg - all_pets
    print(f"{floor(food_left)} kilos of food left.")
else:
    food_left = all_pets - food_in_kg
    print(f"{ceil(food_left)} more kilos of food are needed.")