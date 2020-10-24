number_of_cats = int(input())

group_one = 0
group_two = 0
group_three = 0
total_food = 0

for cats in range(1, number_of_cats + 1):
    grams_of_food = int(input())
    total_food += grams_of_food

    if 100 <= grams_of_food < 200:
        group_one += 1
    elif 200 <= grams_of_food < 300:
        group_two += 1
    elif 300 <= grams_of_food < 400:
        group_three += 1

kgs_of_food = total_food / 1000
price = kgs_of_food * 12.45
print(f"Group 1: {group_one} cats.")
print(f"Group 2: {group_two} cats.")
print(f"Group 3: {group_three} cats.")
print(f"Price for food per day: {price:.2f} lv.")