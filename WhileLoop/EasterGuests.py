import math
from math import ceil

number_of_guests = int(input())
budget = float(input())

number_of_kozunak = number_of_guests / 3  #ceil
number_of_eggs_needed = number_of_guests * 2

kozunak_price = ceil(number_of_kozunak) * 4
egg_price = number_of_eggs_needed * 0.45

total = kozunak_price + egg_price

diff = total - budget

if budget >= total:
    print(f"Lyubo bought {ceil(number_of_kozunak)} Easter bread and {number_of_eggs_needed} eggs.")
    print(f"He has {abs(diff):.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {abs(diff):.2f} lv. more.")