bough_food_in_kg = int(input())

food_in_grams = bough_food_in_kg * 1000

sum_of_food = 0

command = input()
while command != "Adopted":
    food_per_day = int(command)
    sum_of_food += food_per_day

    command = input()

    if command == "Adopted":
        diff = sum_of_food - food_in_grams
        if sum_of_food <= food_in_grams:
            print(f"Food is enough! Leftovers: {abs(diff)} grams.")
            break
        elif sum_of_food > food_in_grams:
            diff = sum_of_food - food_in_grams
            print(f"Food is not enough. You need {abs(diff)} grams more.")
            break