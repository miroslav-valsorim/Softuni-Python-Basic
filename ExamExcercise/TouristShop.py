budget = float(input())
all_deal_price = 0
deal = 0
entries = 0
command = input()
while command != "Stop":
    product_name = command
    product_price = float(input())
    entries += 1
    if entries % 3 == 0:
        deal = product_price / 2
        all_deal_price += product_price / 2
    else:
        deal = product_price
        all_deal_price += product_price
    budget -= deal
    if budget < 0:
        print(f"You don't have enough money!")
        print(f"You need {abs(budget):.2f} leva!")
        break
    command = input()

diff = budget - all_deal_price
if command == 'Stop':
    print(f"You bought {entries} products for {all_deal_price:.2f} leva.")