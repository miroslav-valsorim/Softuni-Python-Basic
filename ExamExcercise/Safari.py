# Цената на един литър гориво е 2.10 лв.
# Цената за екскурзовод е 100лв.
# В зависимост от деня има отстъпки от общата цена - за събота 10%, а за неделя 20%

budget = float(input())
fuel_needed = float(input())
day = input()

liter_of_fuel = 2.10
guide_price = 100

total_fuel_price = fuel_needed * liter_of_fuel
total_price = total_fuel_price + guide_price

discount = 0

if day == "Saturday":
    discount = total_price - total_price * 10 / 100
elif day == "Sunday":
    discount = total_price - total_price * 20 / 100

diff = budget - discount
if discount <= budget:
    print(f"Safari time! Money left: {abs(diff):.2f} lv.")
else:
    print(f"Not enough money! Money needed: {abs(diff):.2f} lv.")