detergents = int(input())

liter_of_detergent = 750
sum_of_dishes = 0
sum_of_pots = 0
detergent_for_dish = 5
detergent_for_pot = 15
entries = 0
used_detergent = 0

total_detergent = liter_of_detergent * detergents

command = input()
while command != "End":
    utensils = int(command)
    entries += 1

    if entries % 3 == 0:
        sum_of_pots += utensils
        used_detergent += utensils * detergent_for_pot

    else:
        sum_of_dishes += utensils
        used_detergent += utensils * detergent_for_dish

    if used_detergent > total_detergent:
        diff = total_detergent - used_detergent
        print(f"Not enough detergent, {abs(diff)} ml. more necessary!")
        break

    command = input()

if command == "End":
    diff = total_detergent - used_detergent
    print(f"Detergent was enough!")
    print(f"{sum_of_dishes} dishes and {sum_of_pots} pots were washed.")
    print(f"Leftover detergent {abs(diff)} ml.")
