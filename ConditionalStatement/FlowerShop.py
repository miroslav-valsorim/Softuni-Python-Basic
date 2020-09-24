from math import floor
from math import ceil

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
present_price = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cacti_price = 8

all_mag = magnolias * magnolias_price
all_hya = hyacinths * hyacinths_price
all_rose = roses * roses_price
all_cacti = cacti * cacti_price
all_price = all_mag + all_hya + all_rose + all_cacti
tax = all_price - all_price * 5 / 100

if present_price <= tax:
    last_price = tax - present_price
    print(f"She is left with {floor(last_price)} leva.")
else:
    last_price = present_price - tax
    print(f"She will have to borrow {ceil(last_price)} leva.")