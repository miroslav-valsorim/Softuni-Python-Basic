cake = 45
waffle = 5.80
pancake = 3.20

days = float(input())
confectioner = float(input())
number_of_cake = float(input())
number_of_waffle = float(input())
number_of_pancake = float(input())

cakes = cake * number_of_cake
waffles = waffle * number_of_waffle
pancakes = pancake * number_of_pancake
price_for_day = (cakes + waffles + pancakes) * confectioner
campaign = price_for_day * days
last_price = campaign - campaign * 12.5/100

print(last_price)
