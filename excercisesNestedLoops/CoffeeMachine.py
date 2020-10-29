product = input()
sugar = input()
number_of_drinks = int(input())

price = 0

if product == "Espresso":
    if sugar == "Without":
        price = 0.90
    elif sugar == "Normal":
        price = 1.00
    elif sugar == "Extra":
        price = 1.20
elif product == "Cappuccino":
    if sugar == "Without":
        price = 1.00
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60
elif product == "Tea":
    if sugar == "Without":
        price = 0.50
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70

total = price * number_of_drinks

if sugar == "Without":
    total *= 0.65
if product == "Espresso" and number_of_drinks >= 5:
    total *= 0.75
if total > 15:
    total *= 0.80

print(f"You bought {number_of_drinks} cups of {product} for {total:.2f} lv.")
