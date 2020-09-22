def read_lines(iterations):
    array = []

    for arg in range(iterations):
        array.append(float(input()))

    return array


trip, number_of_puzzle, number_of_talking_doll, number_of_teddy_beat, \
number_of_minions, number_of_trucks = read_lines(6)

puzzle_price, talking_doll_price, teddy_bear_price, minion_price, truck_price = 2.60, 3, 4.1, 8.2, 2

puzzle = number_of_puzzle * puzzle_price
talking_doll = number_of_talking_doll * talking_doll_price
teddy_bear = number_of_teddy_beat * teddy_bear_price
minion = number_of_minions * minion_price
truck = number_of_trucks * truck_price

total_price = puzzle + talking_doll + teddy_bear + minion + truck
total_toys = number_of_puzzle + number_of_talking_doll + number_of_teddy_beat + number_of_minions + number_of_trucks

if total_toys >= 50:
    discount_price = total_price - total_price * 25 / 100
    rent = discount_price - discount_price * 10 / 100

    if rent >= trip:
        money_left = rent - trip
        print(f"Yes! {abs(money_left):.2f} lv left.")
    elif rent <= trip:
        money_left_one = rent - trip
        print(f"Not enough money! {abs(money_left_one):.2f} lv needed.")
elif total_toys <= 50:
    no_discount = total_price
    rent = no_discount - no_discount * 10 / 100

    if rent >= trip:
        money_left_two = rent - trip
        print(f"Yes! {abs(money_left_two):.2f} lv left.")
    elif rent <= trip:
        money_left_three = rent - trip
        print(f"Not enough money! {abs(money_left_three):.2f} lv needed.")
