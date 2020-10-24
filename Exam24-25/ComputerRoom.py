month = input()
number_of_hours = int(input())
number_of_people = int(input())
time_of_day = input()

price = 0

if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price = 10.50
    elif time_of_day == "night":
        price = 8.40
elif month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price = 12.60
    elif time_of_day == "night":
        price = 10.20

if number_of_people >= 4:
    price -= price * 10 / 100

if number_of_hours >= 5:
    price /= 2

total = (price * number_of_people) * number_of_hours

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total:.2f}")