town = input()
packet = input()
vip = input()
days = int(input())

price = 0
if days <= 0:
    print(f"Days must be positive number!")
else:

    if town == "Bansko" or town == "Borovets":

        if packet == "noEquipment":
            price = 80
            if vip == "yes":
                price -= price * 0.05
            else:
                price = price
        elif packet == "withEquipment":
            price = 100
            if vip == "yes":
                price -= price * 0.10
            else:
                price = price

    elif town == "Varna" or town == "Burgas":

        if packet == "noBreakfast":
            price = 100
            if vip == "yes":
                price -= price * 0.07
            else:
                price = price
        elif packet == "withBreakfast":
            price = 130
            if vip == "yes":
                price -= price * 0.12
            else:
                price = price

    grand_total = price * days

    if days > 7:
        grand_total -= price

    if town == "Bansko" or town == "Borovets" or town == "Varna" or town == "Burgas":
        if packet == "noEquipment" or packet == "withEquipment" or packet == "noBreakfast" or packet == "withBreakfast":
            if vip == "yes" or vip == "no":
                print(f"The price is {grand_total:.2f}lv! Have a nice time!")
    else:
        print(f"Invalid input!")