money = float(input())
year_to_live = int(input())

years_old = 0
money_left = 0
years_old = 18

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        money -= 12000
    else:
        money -= (12000 + years_old * 50)
    years_old += 1


if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
elif money < 0:
    print(f"He will need {abs(money):.2f} dollars to survive.")
