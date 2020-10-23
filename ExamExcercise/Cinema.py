cinema_capacity = int(input())

ticket = 5
total = 0
capacity_counter = 0
money_per_group = 0

command = input()
while command != "Movie time!":
    number_of_people = int(command)

    money_per_group += number_of_people * ticket
    if number_of_people % 3 == 0:
        money_per_group -= 5

    if capacity_counter >= cinema_capacity:
        print(f"The cinema is full.")
        break

    command = input()

if command == "Movie time!":
    spots_left = cinema_capacity - capacity_counter
    print(f"There are {spots_left} seats left in the cinema.")

print(f"Cinema income - {money_per_group} lv.")