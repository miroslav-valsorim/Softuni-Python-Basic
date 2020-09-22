deposit_price = float(input())
months = int(input())
year_increase = float(input())

month_increase = deposit_price * year_increase / 100 / 12
total = deposit_price + months * month_increase

print(total)