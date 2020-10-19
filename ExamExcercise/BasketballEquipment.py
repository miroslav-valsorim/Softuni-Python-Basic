year_tax = int(input())

basketball_shoes = year_tax - year_tax * 40 / 100
basketball_kit = basketball_shoes - basketball_shoes * 20 / 100
basketball_ball = basketball_kit / 4
basketball_accessories = basketball_ball / 5

total_cost = year_tax + basketball_shoes + basketball_kit + basketball_ball + basketball_accessories
print(f"{total_cost:.2f}")