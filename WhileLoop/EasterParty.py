number_of_guests = int(input())
price_for_person = float(input())
budget = float(input())

for_person_discount = 0

cake_price = budget - budget * 90 / 100

if 10 <= number_of_guests <= 15:
    for_person_discount = price_for_person - price_for_person * 15 / 100
elif 15 < number_of_guests <= 20:
    for_person_discount = price_for_person - price_for_person * 20 / 100
elif number_of_guests > 20 :
    for_person_discount = price_for_person - price_for_person * 25 / 100
else:
    for_person_discount = price_for_person

total_for_people = for_person_discount * number_of_guests
total = total_for_people + cake_price

diff = budget - total

if total <= budget:
    print(f"It is party time! {abs(diff):.2f} leva left.")
else:
    print(f"No party! {abs(diff):.2f} leva needed.")