days_rest = int(input())
kind_of_room = input()
grade = input()

nights = days_rest - 1

if kind_of_room == "room for one person":
    price = nights * 18.00
    if grade == "positive":
        last_price = price + price * 25 / 100
        print(f"{last_price:.2f}")
    elif grade == "negative":
        last_price = price - price * 10 / 100
        print(f"{last_price:.2f}")
elif kind_of_room == "apartment":
    price = nights * 25.00
    if nights <= 10:
        prom_price = price - price * 30 / 100
        if grade == "positive":
            last_price = prom_price + prom_price * 25 / 100
            print(f"{last_price:.2f}")
        elif grade == "negative":
            last_price = prom_price - prom_price * 10 / 100
            print(f"{last_price:.2f}")
    elif 10 <= nights <= 15:
        prom_price = price - price * 45 / 100
        if grade == "positive":
            last_price = prom_price + prom_price * 25 / 100
            print(f"{last_price:.2f}")
        elif grade == "negative":
            last_price = prom_price - prom_price * 10 / 100
            print(f"{last_price:.2f}")
    elif nights > 15:
        prom_price = price - price * 50 / 100
        if grade == "positive":
            last_price = prom_price + prom_price * 25 / 100
            print(f"{last_price:.2f}")
        elif grade == "negative":
            last_price = prom_price - prom_price * 10 / 100
            print(f"{last_price:.2f}")
elif kind_of_room == "president apartment":
    price = nights * 35.00
    if nights <= 10:
        prom_price = price - price * 10 / 100
        if grade == "positive":
            last_price = prom_price + prom_price * 25 / 100
            print(f"{last_price:.2f}")
        elif grade == "negative":
            last_price = prom_price - prom_price * 10 / 100
            print(f"{last_price:.2f}")
    elif 10 <= nights <= 15:
        prom_price = price - price * 15 / 100
        if grade == "positive":
            last_price = prom_price + prom_price * 25 / 100
            print(f"{last_price:.2f}")
        elif grade == "negative":
            last_price = prom_price - prom_price * 10 / 100
            print(f"{last_price:.2f}")
    elif nights > 15:
        prom_price = price - price * 20 / 100
        if grade == "positive":
            last_price = prom_price + prom_price * 25 / 100
            print(f"{last_price:.2f}")
        elif grade == "negative":
            last_price = prom_price - prom_price * 10 / 100
            print(f"{last_price:.2f}")
