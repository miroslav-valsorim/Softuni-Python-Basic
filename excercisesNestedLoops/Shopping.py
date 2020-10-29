budget = float(input())
number_of_cards = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

video_card = 250
total_video_cards = video_card * number_of_cards
processor_price = total_video_cards - total_video_cards * 65 / 100
ram_price = total_video_cards - total_video_cards * 90 / 100

total_ram = ram_price * number_of_ram
total_processor = number_of_processors * processor_price

grand_total = total_video_cards + total_processor + total_ram

if number_of_cards > number_of_processors:
    grand_total *= 0.85
else:
    grand_total = grand_total

diff = abs(budget - grand_total)
if budget >= grand_total:
    print(f"You have {diff:.2f} leva left!")
elif budget < grand_total:
    print(f"Not enough money! You need {diff:.2f} leva more!")