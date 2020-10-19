import math
from math import ceil
from math import floor

price_for_tennis_rocket = float(input())
number_of_tennis_rockets = int(input())
number_of_shoes = int(input())

shoes_price = price_for_tennis_rocket / 6

all_rockets_rice = number_of_tennis_rockets * price_for_tennis_rocket
price_for_all_shoes = number_of_shoes * shoes_price
price_for_other_equipment = (all_rockets_rice + price_for_all_shoes) * 0.2
total = all_rockets_rice + price_for_all_shoes + price_for_other_equipment

djokovic_price = total / 8
sponsor_price = total - djokovic_price

print(f"Price to be paid by Djokovic {floor(djokovic_price)}")
print(f"Price to be paid by sponsors {ceil(sponsor_price)}")