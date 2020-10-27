from math import ceil
number_of_people = int(input())
tax = float(input())
price_per_chair = float(input())
price_per_umbrella = float(input())

total_entries = number_of_people * tax
people_with_chair = ceil(number_of_people * 0.75)
price_for_chairs = people_with_chair * price_per_chair
people_with_umbrella = ceil(number_of_people * 0.50)
price_for_umbrellas = people_with_umbrella * price_per_umbrella

grand_total = total_entries + price_for_chairs + price_for_umbrellas
print(f"{grand_total:.2f} lv.")