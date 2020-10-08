months = int(input())

water_price = 20
internet_price = 15

electricity_bill = 0
water_bill = 0
internet_bill = 0
others = 0
sum_of_others = 0
average = 0
all_consumables = 0

for year_months in range(1, months + 1):
    electricity = float(input())

    electricity_bill += electricity
    water_bill = months * water_price
    internet_bill = months * internet_price
    all_consumables = electricity + water_price + internet_price
    others = all_consumables + all_consumables * 20 / 100
    sum_of_others += others
average = (sum_of_others + electricity_bill + water_bill + internet_bill) / months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {sum_of_others:.2f} lv")
print(f"Average: {average:.2f} lv")


