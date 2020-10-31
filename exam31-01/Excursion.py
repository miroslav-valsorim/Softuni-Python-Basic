night = 20
transport = 1.60
museum = 6

number_of_people = int(input())
number_of_nights = int(input())
number_of_cards = int(input())
number_of_tickets = int(input())

all_nights = night * number_of_nights
all_cards = transport * number_of_cards
all_museum = museum * number_of_tickets

total_per_person = all_nights + all_cards + all_museum
grand_total = total_per_person * number_of_people

total = grand_total + grand_total * 25 / 100

print(f"{total:.2f}")