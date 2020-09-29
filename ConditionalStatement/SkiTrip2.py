single = 18
apartment = 25
president = 35

stay = int(input())
nights = stay - 1
room_type = input()
review = input()

if room_type == "room for one person":
    total_cost = nights * single

elif room_type == "apartment":
    total_cost = nights * apartment
    if stay < 10:
        total_cost *= 0.7
    elif 10 <= stay <= 15:
        total_cost *= 0.65
    else:
        total_cost *= 0.5

elif room_type == "president apartment":
    total_cost = nights * president
    if stay < 10:
        total_cost *= 0.9
    elif 10 <= stay <= 15:
        total_cost *= 0.85
    else:
        total_cost *= 0.8

if review == "positive":
    final_cost = total_cost * 1.25
    print(f"{final_cost:.2f}")
else:
    final_cost = total_cost * 0.9
    print(f"{final_cost:.2f}")