budget = float(input())
category = input()
people = int(input())

vip_ticket = 499.99
normal_ticket = 249.99
ticket_price = 0

if people <= 4:
    money_left = budget - budget * 75 / 100
    if category == "VIP":
        tickets_price = vip_ticket
    elif category == "Normal":
        tickets_price = normal_ticket
elif 5 <= people <= 9:
    money_left = budget - budget * 60 / 100
    if category == "VIP":
        tickets_price = vip_ticket
    elif category == "Normal":
        tickets_price = normal_ticket
elif 10 <= people <= 24:
    money_left = budget - budget * 50 / 100
    if category == "VIP":
        tickets_price = vip_ticket
    elif category == "Normal":
        tickets_price = normal_ticket
elif 25 <= people <= 49:
    money_left = budget - budget * 40 / 100
    if category == "VIP":
        tickets_price = vip_ticket
    elif category == "Normal":
        tickets_price = normal_ticket
elif people >= 50:
    money_left = budget - budget * 25 / 100
    if category == "VIP":
        tickets_price = vip_ticket
    elif category == "Normal":
        tickets_price = normal_ticket

total_ticket_price = tickets_price * people
total = tickets_price + money_left
diff = abs(money_left - tickets_price)
if total <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
elif total > budget:
    print(f"Not enough money! You need {diff:.2f} leva.")


