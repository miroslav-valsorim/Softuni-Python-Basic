budget = float(input())
season = input()

money = 0

if budget <= 100:
    if season == "winter":
        money = budget * 0.70
        print(f"Somewhere in Bulgaria")
        print(f"Hotel - {money:.2f}")
    elif season == "summer":
        money = budget * 0.30
        print(f"Somewhere in Bulgaria")
        print(f"Camp - {money:.2f}")
elif budget <= 1000:
    if season == "winter":
        money = budget * 0.80
        print(f"Somewhere in Balkans")
        print(f"Hotel - {money:.2f}")
    elif season == "summer":
        money = budget * 0.40
        print(f"Somewhere in Balkans")
        print(f"Camp - {money:.2f}")
elif budget > 1000:
    if season == "winter":
        money = budget * 0.90
        print(f"Somewhere in Europe")
        print(f"Hotel - {money:.2f}")
    elif season == "summer":
        money = budget * 0.90
        print(f"Somewhere in Europe")
        print(f"Hotel - {money:.2f}")