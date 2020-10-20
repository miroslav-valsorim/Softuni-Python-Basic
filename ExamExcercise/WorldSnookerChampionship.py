type_of_competition = input()
tickets = input()
number_of_tickets = int(input())
photo = input()

price = 0

if type_of_competition == "Quarter final":
    if tickets == "Standard":
        price = 55.50
    elif tickets == "Premium":
        price = 105.20
    elif tickets == "VIP":
        price = 118.90
elif type_of_competition == "Semi final":
    if tickets == "Standard":
        price = 75.88
    elif tickets == "Premium":
        price = 125.22
    elif tickets == "VIP":
        price = 300.40
elif type_of_competition == "Final":
    if tickets == "Standard":
        price = 110.10
    elif tickets == "Premium":
        price = 160.66
    elif tickets == "VIP":
        price = 400

total_ticket_price = number_of_tickets * price


if total_ticket_price > 4000:
    total_ticket_price -= total_ticket_price * 25 / 100
    if photo == "Y":
        total_ticket_price = total_ticket_price
    else:
        total_ticket_price = total_ticket_price
elif total_ticket_price > 2500:
    total_ticket_price -= total_ticket_price * 10 / 100
    if photo == "Y":
        total_ticket_price += number_of_tickets * 40
    else:
        total_ticket_price = total_ticket_price

print(f"{total_ticket_price:.2f}")