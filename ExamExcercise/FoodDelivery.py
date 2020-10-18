number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vege_menu = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vege_menu = 8.15

total_chicken = chicken_menu * number_of_chicken_menu
total_fish = fish_menu * number_of_fish_menu
total_vege = vege_menu * number_of_vege_menu

sum_of_all = total_chicken + total_fish + total_vege
desert_price = sum_of_all - sum_of_all * 80 / 100
delivery = 2.50

total = sum_of_all + desert_price + delivery

print(f"Total: {total:.2f}")