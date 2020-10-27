budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percentage_for_things = int(input())

if number_of_nights > 7:
    price_per_night -= price_per_night * 0.05
else:
    price_per_night = price_per_night

total_for_nights = price_per_night * number_of_nights
more_stuff = budget * percentage_for_things / 100

total = total_for_nights + more_stuff

diff = abs(total - budget)
if total <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
