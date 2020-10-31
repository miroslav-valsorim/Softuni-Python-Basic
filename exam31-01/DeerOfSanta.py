from math import floor
from math import ceil

days_missing = int(input())
food_in_kg = int(input())
food_for_first = float(input())
food_for_second = float(input())
food_for_third = float(input())

first = days_missing * food_for_first
second = days_missing * food_for_second
third = days_missing * food_for_third

total = first + second + third

diff = abs(food_in_kg - total)
if food_in_kg >= total:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")