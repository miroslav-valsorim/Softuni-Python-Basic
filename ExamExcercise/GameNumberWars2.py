name_first_player = input()
name_second_player = input()

points_first = 0
points_second = 0

is_finished = False

card_first = input()
while card_first != 'End of game':
    card_first = int(card_first)
    card_second = int(input())
    if card_first > card_second:
        points_first += card_first - card_second
    elif card_first < card_second:
        points_second += card_second - card_first
    elif card_first == card_second:
        print(f'Number wars!')
        card_first = int(input())
        card_second = int(input())
        is_finished = True
        if card_first > card_second:
            print(f'{name_first_player} is winner with {points_first} points')
            break
        elif card_second > card_first:
            print(f'{name_second_player} is winner with {points_second} points')
            break
    card_first = input()
if not is_finished:
    print(f'{name_first_player} has {points_first} points')
    print(f'{name_second_player} has {points_second} points')