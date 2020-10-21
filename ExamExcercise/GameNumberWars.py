player_one_name = input()
player_two_name = input()

player_one_points = 0
player_two_points = 0
isFinished = False

command = input()
while command != "End of game":
    player_one_number = int(command)
    player_two_number = int(input())

    if player_one_number > player_two_number:
        player_one_points += player_one_number - player_two_number
    elif player_two_number > player_one_number:
        player_two_points += player_two_number - player_one_number
    elif player_two_number == player_one_number:
        print("Number wars!")
        player_one_number = int(input())
        player_two_points = int(input())
        isFinished = True
        if player_one_number > player_two_number:
            print(f'{player_one_name} is winner with {player_one_points} points')
            break
        elif player_two_number > player_one_number:
            print(f'{player_two_name} is winner with {player_two_points} points')
            break
    command = input()
if not isFinished:
    print(f'{player_one_name} has {player_one_points} points')
    print(f'{player_two_name} has {player_two_points} points')
