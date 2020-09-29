town = input()
price = float(input())
commission = 0

if town == "Sofia":
    if 0 <= price <= 500:
        commission = price - price * 95 / 100
        print(f"{commission:.2f}")
    elif 500 <= price <= 1000:
        commission = price - price * 93 / 100
        print(f"{commission:.2f}")
    elif 1000 <= price <= 10000:
        commission = price - price * 92 / 100
        print(f"{commission:.2f}")
    elif price > 10000:
        commission = price - price * 88 / 100
        print(f"{commission:.2f}")
    else:
        print("error")
elif town == "Varna":
    if 0 <= price <= 500:
        commission = price - price * 95.5 / 100
        print(f"{commission:.2f}")
    elif 500 <= price <= 1000:
        commission = price - price * 92.5 / 100
        print(f"{commission:.2f}")
    elif 1000 <= price <= 10000:
        commission = price - price * 90 / 100
        print(f"{commission:.2f}")
    elif price > 10000:
        commission = price - price * 87 / 100
        print(f"{commission:.2f}")
    else:
        print("error")
elif town == "Plovdiv":
    if 0 <= price <= 500:
        commission = price - price * 94.5 / 100
        print(f"{commission:.2f}")
    elif 500 <= price <= 1000:
        commission = price - price * 92 / 100
        print(f"{commission:.2f}")
    elif 1000 <= price <= 10000:
        commission = price - price * 88 / 100
        print(f"{commission:.2f}")
    elif price > 10000:
        commission = price - price * 85.5 / 100
        print(f"{commission:.2f}")
    else:
        print("error")
else:
    print("error")

