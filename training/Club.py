budget_wanted = float(input())

total = 0
money_full = False

command = input()
while command != "Party!":
    drink_name = command
    number_of_drinks = int(input())
    price = int(len(drink_name))

    drinks_price = price * number_of_drinks
    if drinks_price % 2 == 1:
        drinks_price -= drinks_price * 25 / 100
    else:
        drinks_price = drinks_price

    total += drinks_price
    if total >= budget_wanted:
        print(f"Target acquired.")
        money_full = True
        break

    command = input()
if command == "Party!" and total < budget_wanted:
    diff = budget_wanted - total
    print(f"We need {diff:.2f} leva more.")
if money_full or command == "Party!":
    print(f"Club income - {total:.2f} leva.")