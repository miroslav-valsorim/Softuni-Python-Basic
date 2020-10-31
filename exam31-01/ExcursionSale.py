number_of_sea_excursion = int(input())
number_of_mountain_excursion = int(input())

sea_ticket = 680
mountain_ticket = 499

profit = 0
Done = False

command = input()
while command != "Stop":
    season = command

    if season == "sea" and number_of_sea_excursion == 0:
        command = input()
        continue
    elif season == "mountain" and number_of_mountain_excursion == 0:
        command = input()
        continue

    if season == "sea":
        number_of_sea_excursion -= 1
        profit += sea_ticket
    elif season == "mountain":
        number_of_mountain_excursion -= 1
        profit += mountain_ticket

    if number_of_sea_excursion == 0 and number_of_mountain_excursion == 0:
        print(f"Good job! Everything is sold.")
        Done = True
        break
    command = input()
#if command == "stop" or Done:
print(f"Profit: {profit} leva.")