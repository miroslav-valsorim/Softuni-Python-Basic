days_rest = int(input())
kind_of_room = input()
grade = input()

nights = days_rest - 1

if kind_of_room == "room for one person":
    price = nights * 18.00
    if grade == "positive":
        price *= 0.85
        print(f"{price:.2f}")
    elif grade == "negative":
        price *= 0.90
        print(f"{price:.2f}")
elif kind_of_room == "apartment":
    price = nights * 25.00
    if nights <= 10:
        price *= 0.70
        if grade == "positive":
            price *= 0.85
            print(f"{price:.2f}")
        elif grade == "negative":
            price *= 0.90
            print(f"{price:.2f}")
    elif 10 <= nights <= 15:
        price *= 0.65
        if grade == "positive":
            price *= 0.75
            print(f"{price:.2f}")
        elif grade == "negative":
            price = 0.90
            print(f"{price:.2f}")
    elif nights > 15:
        prom_price = price - price * 50 / 100
        if grade == "positive":
            price *= 0.75
            print(f"{price:.2f}")
        elif grade == "negative":
            price *= 0.90
            print(f"{price:.2f}")
elif kind_of_room == "president apartment":
    price = nights * 35.00
    if nights <= 10:
        price *= 0.90
        if grade == "positive":
            price = 0.75
            print(f"{price:.2f}")
        elif grade == "negative":
            price *= 0.90
            print(f"{price:.2f}")
    elif 10 <= nights <= 15:
        price *= 0.85
        if grade == "positive":
            price *= 0.75
            print(f"{price:.2f}")
        elif grade == "negative":
            price *= 0.90
            print(f"{price:.2f}")
    elif nights > 15:
        price *= 0.80
        if grade == "positive":
            price *= 0.75
            print(f"{price:.2f}")
        elif grade == "negative":
            price *= 0.90
            print(f"{price:.2f}")
