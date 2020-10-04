ages = int(input())
laundry_price = float(input())
price_per_toy = int(input())

total_money = 0
total_toys = 0
birthday_money = 0

for age in range(1, ages + 1):
    if age % 2 == 0:
        birthday_money += 10
        total_money += birthday_money - 1
    else:
        total_toys += 1

money_from_toys = total_toys * price_per_toy
total_money += money_from_toys

diff = abs(laundry_price - total_money)

if total_money >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")