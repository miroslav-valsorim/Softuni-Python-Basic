budget = float(input())
number_of_serials = int(input())

total = budget
sum_of_series = 0

for series in range(1, number_of_serials + 1):
    name = input()
    price = float(input())

    if name == "Thrones":
        price /= 2
        total -= price
        sum_of_series += price
    elif name == "Lucifer":
        price -= price * 40 / 100
        total -= price
        sum_of_series += price
    elif name == "Protector":
        price -= price * 30 / 100
        total -= price
        sum_of_series += price
    elif name == "TotalDrama":
        price -= price * 20 / 100
        total -= price
        sum_of_series += price
    elif name == "Area":
        price -= price * 10 / 100
        total -= price
        sum_of_series += price
    else:
        total -= price
        sum_of_series += price

if sum_of_series > budget:
    diff = sum_of_series - budget
    print(f"You need {diff:.2f} lv. more to buy the series!")
else:
    money_left = total
    print(f"You bought all the series and left with {total:.2f} lv.")